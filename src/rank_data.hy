#!/usr/bin/env hy

(require hyrule [-> ->> ap-each ncut])
(import numpy :as np)
(import pandas :as pd)

(defmacro setcol [df col-name equals]
  `(setv (get ~df ~col-name) ~equals))

(defmacro addcol [df col-name add]
  `(+= (get ~df ~col-name) ~add))

(with [f (open "data/translator_drug_list.json" "r")]
  (setv data (pd.read-json f)))
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

;;; 1: No liver injury
(+= (ncut data.loc (< (get data "Drug Induced Liver Injury") 0.5) "score") 1)

;;; sort by score
(data.sort-values
  :by "score"
  :ascending False
  :inplace True)

;;; move the relevant columns to the front
(setv cols-to-move
  ["DrugBank Name"
   "score"
   "FDA Approved" 
   "Less than $100"
   "Less than $1000"
   "Blood Brain Barrier"
   "P-glycoprotein Inhibition"
   "Human Intestinal Absorption"
   "Drug Induced Liver Injury"
   "search term"])
(setv data 
  (get data 
    (+ 
      cols-to-move 
      (lfor 
        col (. data columns) 
        :if (not-in col cols-to-move) 
        col))))

;;; remove original list data
(with [f (open "data/ranked.csv" "r")]
  (setv original-data (pd.read-csv f)))
(setv original-mask
  (.isin (get data "DrugBank Name") (get original-data "DrugBank Name")))
(setv data (get data (= original-mask False)))

(with [f (open "data/translator_ranked.csv" "w")]
  (.to-csv data f :index False))
