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

(defn unwrap-list [x]
  """
  [x] -> x
  [ ] -> None
  """
  (if (isinstance x list)
    (if (> (len x) 0)
      (get x 0)
      None)
    x))

(defn is-safe [chatgpt-output]
  (setv correct-regexp (re.compile r"<explain>.*</explain>.*<answer>.*</answer>" re.DOTALL))
  (setv answer-regexp (re.compile r"<answer>(.*)</answer>" re.DOTALL))
  (if (re.match correct-regexp chatgpt-output)
    (!= (.find (.lower (get (re.search answer-regexp chatgpt-output) 0)) "yes") -1)
    False))

;;; open extra data
;(with [f (open "data/src/pubmed_answers.json" "r")]
;  (setv answers (json.load f)))
;(with [f (open "../PubMed-Embedding-Project/drug_names.txt" "r")]
;  (setv drug-names (list (map (fn [s] (cut s None -1)) (.readlines f)))))

;;; open augmented drug data
;(with [f (open "data/drug_list.json" "r")]
;  (setv initial-data (pd.read-json f)))
(with [f (open "data/translator_drug_list.json" "r")]
  (setv translator-data (pd.read-json f)))
(setcol translator-data "Clinician Recommendation" False)
(setcol translator-data "Screened" False)

;;; combine drug data
;(setcol initial-data    "Data Source" "original")
(setcol translator-data "Data Source" "translator")
;(setv same-cols
;  (list
;    (set.intersection
;      (set (. initial-data columns))
;      (set (. translator-data columns)))))
;(setv data (pd.concat #((get initial-data same-cols) (get translator-data same-cols)) :ignore-index True))
(setv data translator-data)

;(setcol data "Pediatric Safety" False)
;(for [#(drug-name answer) (zip drug-names answers)]
;  (setv (ncut data.loc (= (get data "DrugBank:Main Name") drug-name) "Pediatric Safety") (is-safe (get answer "answer"))))

(setcol data "score" 0)

;;; exclude completely for these
(setv very-large-number 1e9)
(-=
  (ncut data.loc
    (&
      (< (get data "Blood Brain Barrier") 0.5)
      (< (get data "P-glycoprotein Inhibition") 0.5))
    "score")
  very-large-number)
(-= (ncut data.loc (< (get data "Human Intestinal Absorption") 0.5) "score") very-large-number)
(-= (ncut data.loc (> (get data "Drug Induced Liver Injury") 0.5) "score") very-large-number)

;;; 1: FDA approved
(addcol data "score" 
  (.fillna 
    (.apply
      (get data "DrugBank:FDA Approved")
      unwrap-list)
    False))

;;; 1: cost less than $500
(setcol data "Less than $500"
  (<
    (.apply (get data "DrugBank:Prices")
      (fn [l]
        (when (isinstance l str)
          (setv l [l]))
        (when (or (is l None) (= (len l) 0))
          (setv l ["InfUSD"]))
        (->> l
          (map (fn [s] (float (s.removesuffix "USD"))))
          (tuple)
          (max))))
    500))
(addcol data "score" (get data "Less than $500"))

;;; 1: Safe in children
;(addcol data "score" (get data "Pediatric Safety"))

;;; override clinician recommended to top
;(setv (ncut data.loc (get data "Clinician Recommendation") "score") very-large-number)

;;; sort by score
(data.sort-values
  :by "score"
  :ascending False
  :inplace True)

(with [f (open "data/ranked.csv" "w")]
  (.to-csv data f :index False))
