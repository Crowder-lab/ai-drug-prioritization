#!/usr/bin/env hy

(import json)
(import re)

(require hyrule [-> ->> ap-each ncut])
(import numpy :as np)
(import pandas :as pd)

(defmacro setcol [df col-name equals]
  `(setv (get ~df ~col-name) ~equals))

(defmacro addcol [df col-name add]
  `(+= (get ~df ~col-name) ~add))

(defn is-safe [chatgpt-output]
  (setv correct-regexp (re.compile r"<explain>.*</explain>.*<answer>.*</answer>" re.DOTALL))
  (setv answer-regexp (re.compile r"<answer>(.*)</answer>" re.DOTALL))
  (if (re.match correct-regexp chatgpt-output)
    (!= (.find (.lower (get (re.search answer-regexp chatgpt-output) 0)) "yes") -1)
    False))

(with [f (open "data/src/pubmed_answers.json" "r")]
  (setv answers (json.load f)))
(with [f (open "../PubMed-Embedding-Project/drug_names.txt" "r")]
  (setv drug-names (list (map (fn [s] (cut s None -1)) (.readlines f)))))

(with [f (open "data/drug_list.json" "r")]
  (setv data (pd.read_json f)))

(setcol data "Pediatric Safety" False)
(for [#(drug-name answer) (zip drug-names answers)]
  (setv (ncut data.loc (= (get data "Canonical Name") drug-name) "Pediatric Safety") (is-safe (get answer "answer"))))

(setcol data "score" 0)

;;; exclude completely for these
(setv very-large-number 1e9)
(ap-each
  #("Bioavailability" "Blood Brain Barrier" "Human Intestinal Absorption")
  (-= (ncut data.loc (< (get data it) 0.5) "score") very-large-number))

;;; 1: FDA approved
(addcol data "score" (.fillna (get data "FDA Approved") False))

;;; 1: cost less than $100
(setcol data "Less than $100"
  (<
    (.apply (get data "Prices")
      (fn [l]
        (when (isinstance l str)
          (setv l [l]))
        (when (or (is l None) (= (len l) 0))
          (setv l ["InfUSD"]))
        (->> l
          (map (fn [s] (float (s.removesuffix "USD"))))
          (tuple)
          (max))))
    100))
(addcol data "score" (get data "Less than $100"))

;;; 1: cost less than $1000
(setcol data "Less than $1000"
  (<
    (.apply (get data "Prices")
      (fn [l]
        (when (isinstance l str)
          (setv l [l]))
        (when (or (is l None) (= (len l) 0))
          (setv l ["InfUSD"]))
        (->> l
          (map (fn [s] (float (s.removesuffix "USD"))))
          (tuple)
          (max))))
    1000))
(addcol data "score" (get data "Less than $1000"))

;;; 1: Safe in children
(addcol data "score" (get data "Pediatric Safety"))

;;; sort by score
(data.sort_values
  :by "score"
  :ascending False
  :inplace True)

(with [f (open f"data/ranked.csv" "w")]
  (.to_csv data f))
