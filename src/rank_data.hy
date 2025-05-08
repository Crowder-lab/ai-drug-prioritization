#!/usr/bin/env hy

(require hyrule [-> ->> ap-each ncut])
(import numpy :as np)
(import pandas :as pd)

(defmacro setcol [df col-name equals]
  `(setv (get ~df ~col-name) ~equals))

(defmacro addcol [df col-name add]
  `(+= (get ~df ~col-name) ~add))

(with [f (open "data/translator_drug_list.json" "r")]
  (setv data (pd.read_json f)))
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

;;; 0.2: each search term it appeared in
(addcol data "score"
  (.apply (get data "search term")
    (fn [x]
      (when (isinstance x str)
        (setv x [x]))
      (* 0.2 (len x)))))

(with [f (open "data/translator_ranked.csv" "w")]
  (data.to_csv f))
