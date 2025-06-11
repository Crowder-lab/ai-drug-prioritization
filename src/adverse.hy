#!/usr/bin/env hy

(require hyrule [ncut])
(import pandas :as pd)
(import tqdm [tqdm])

(defmacro setkey [object key equals]
  `(setv (get ~object ~key) ~equals))

(defn col-types [df col-name]
  (setv types (set))
  (for [row (get df col-name)]
    (types.add (type row)))
  (return types))

(with [f (open "data/dailymed/rxnorm_mappings.txt" "r")]
  (setv dailymed (pd.read-csv f :sep "|")))

(with [f (open "data/translator_drug_list.json" "r")]
  (setv drug-list (pd.read-json f)))

;(with [f (open "data/drug_list.json" "r")]
;  (setv drug-list (pd.read-json f)))

(setkey drug-list "Names List"
  (.apply (get drug-list "All Names")
    (fn [x]
      (if (isinstance x str)
        [x]
        x))))

(setkey dailymed "rxstring"
  (.str.lower (get dailymed "RXSTRING")))

(setv drug-to-setids (dict))

(setv all-drug-names (set))
(for [names (get drug-list "Names List")]
  (all-drug-names.update
    (lfor
      name names
      (.lower name))))

(for [drug-name-lower (tqdm all-drug-names)]
  (setv mask
    (.str.contains
      (get dailymed "rxstring")
      drug-name-lower
      :regex False
      :na False))
  (setkey drug-to-setids drug-name-lower
    (.tolist (ncut dailymed.loc mask "SETID"))))

(setv result-setids [])
(for [#(names fda-approved) (zip (get drug-list "Names List") (get drug-list "FDA Approved"))]
  (setv setids (set))
  (when fda-approved
    (for [name names]
      (setv name-lower (.lower name))
      (when (in name-lower drug-to-setids)
        (setids.update (get drug-to-setids name-lower)))))
  (result-setids.append (list setids)))

(setkey drug-list "SETID" result-setids)

(with [f (open "data/translator_spl_setids_list.json" "w")]
  (drug-list.to-json f :orient "records"))
