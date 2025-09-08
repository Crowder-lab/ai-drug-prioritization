#!/usr/bin/env hy

(import xml.etree.ElementTree :as ET)

(require hyrule [-> doto meth ncut])
(import catboost :as cb)
(import hyrule [flatten])
(import numpy :as np)
(import pandas :as pd)
(import rdkit [Chem RDLogger])
(import tqdm [tqdm])

(import maplight-gnn)


(defclass DrugBank []
  (setv namespaces {"" "http://www.drugbank.ca"})

  (defmacro ap-find [element name if-found]
    `(do
       (setv it (.find ~element ~name self.namespaces))
       (if-let it ~if-found)))

  (defmacro if-let [maybe execute]
    `(when (is-not ~maybe None)
       ~execute))

  (meth __init__ [@filename @ids @id-types names]
    (setv @names (.str.lower names))
    (setv @get-ids {"cas-number"        @cas-number
                    "ChEBI"             @chebi
                    "ChEMBL"            @chembl
                    "drugbank-id"       @drugbank
                    "InChIKey"          @inchikey
                    "PubChem Compound"  @pubchem-compound
                    "PubChem Substance" @pubchem-substance
                    "unii"              @unii}))

  (meth get-matches []
    (for [#(_ element) (tqdm (ET.iterparse @filename ["end"]))]
      ;; don't care about non-drug entries
      (when (!= (cut element.tag 24 None) "drug")
        (continue))
      (setv matches (@check-match element))
      ;; make sure there are matches before doing more work
      (when (not (matches.any))
        (continue))
      (yield #(matches element))))

  (meth check-match [element]
    (setv matches (pd.Series False :index @ids.index))
    (for [#(id-type id-func) (.items @get-ids)]
      (setv id-val (id-func element))
      (when (is id-val None) (continue))
      (setv id-type-matches (= @id-types id-type))
      (setv id-val-matches (= @ids id-val))
      ;(when (> (.sum id-val-matches) 0)
      ;  (print "START")
      ;  (print f"current id type: {id-type}")
      ;  (print f"current name: {(@name element)}")
      ;  (print (get @id-types id-val-matches))
      ;  (print (get @names id-val-matches))
      ;  (print "END"))
      (setv id-full-matches (& id-type-matches id-val-matches))
      (setv matches (| matches id-full-matches)))
    ;; names can't use the same logic as the other id types
    ;(setv #(generic-names brand-names) (@all-names element))
    ;(setv matches (| matches (@names.isin generic-names)))
    ;(setv matches (| matches (@names.isin brand-names)))
    (return matches))

  (meth all-names [element]
    (setv generic-names (set))
    (setv brand-names (set))
    (setv main-name (@name element))
    (when (is-not main-name None) (generic-names.add (.lower main-name)))
    (ap-find element "synonyms"
      (for [synonym (.iter it)]
        (when (and (is-not synonym None) (is-not synonym.text None))
          (generic-names.add (.lower synonym.text)))))
    (ap-find element "products"
      (for [product (.iter it)]
        (setv brand-name (product.find "name" @namespaces))
        (if-let brand-name (brand-names.add (.lower brand-name.text)))))
    (setv generic-names (tuple (filter (fn [s] (not-in "\n" s)) generic-names)))
    (setv brand-names (tuple (filter (fn [s] (not-in "\n" s)) brand-names)))
    (return #(generic-names brand-names)))

  (meth cas-number [element]
    (ap-find element "cas-number" it.text))

  (meth chebi [element]
    (@from-external-identifiers element "ChEBI"))

  (meth chembl [element]
    (@from-external-identifiers element "ChEMBL"))

  (meth drugbank [element]
    (ap-find element "drugbank-id" it.text))

  (meth fda-approval [element]
    (ap-find element "groups" (in "approved" (tuple (it.itertext)))))

  (meth inchikey [element]
    (@from-calculated-properties element "InChIKey"))

  (meth indication [element]
    (ap-find element "indication" it.text))

  (meth mechanism [element]
    (ap-find element "mechanism-of-action" it.text))

  (meth name [element]
    (ap-find element "name" it.text))

  (meth prices [element]
    (ap-find element "prices"
      (do
        (setv prices (list))
        (for [price-element (it.iterfind "price" @namespaces)]
          (setv price (price-element.find "cost" @namespaces))
          (if-let price (.append prices (+ price.text (price.attrib.get "currency")))))
        (return prices))))

  (meth pubchem-compound [element]
    (@from-external-identifiers element "PubChem Compound"))

  (meth pubchem-substance [element]
    (@from-external-identifiers element "PubChem Substance"))

  (meth smiles [element]
    (@from-calculated-properties element "SMILES"))

  (meth unii [element]
    (ap-find element "unii" it.text))

  (meth from-external-identifiers [element resource-type]
    (ap-find element "external-identifiers"
      (for [external-identifier (it.iterfind "external-identifier" @namespaces)]
        (when (= (external-identifier.findtext "resource" :namespaces @namespaces) resource-type)
          (return (external-identifier.findtext "identifier" :namespaces @namespaces))))))

  (meth from-calculated-properties [element kind-type]
    (ap-find element "calculated-properties"
      (for [property (it.iterfind "property" @namespaces)]
        (when (= (property.findtext "kind" :namespaces @namespaces) kind-type)
          (return (property.findtext "value" :namespaces @namespaces)))))))


(defclass DataAugmenter []
  (meth __init__ [@filename @id-col-name @id-type-col-name @name-col-name]
    (setv @drug-list None)
    (setv @admet-models None))

  (defmacro create-var-column [var-name col-name]
    `(do
       (setv ~var-name ~col-name)
       (setv (get self.drug-list ~var-name) (self.drug-list.apply (fn [_] (list)) :axis 1))))

  (meth add-to-column [col-name analysis-function matches element]
    (setv (ncut @drug-list.loc matches col-name)
      (.apply (ncut @drug-list.loc matches col-name)
        (fn [x]
          (setv new-vals (flatten (analysis-function element)))
          (if (isinstance new-vals list)
            (.extend x new-vals)
            (.append x new-vals))
          x))))

  (meth unwrap-list [x]
  ;; [x] -> x
  ;; [ ] -> None
    (if (isinstance x list)
      (if (> (len x) 0)
        (get x 0)
        None)
      x))

  (meth load-drug-queries []
    (cond
      (@filename.endswith ".csv")
      (with [f (open @filename "r")]
        (setv @drug-list (pd.read-csv f)))
      (@filename.endswith ".json")
      (with [f (open @filename "r")]
        (setv @drug-list (pd.read-json f :orient "records")))
      True
      (raise (ValueError "Data file must be .csv or .json")))
    (return self))

  (meth load-admet-models [models]
    (setv @admet-models (dict))
    (for [#(name path) (models.items)]
      (setv model (cb.CatBoostClassifier))
      (model.load-model path)
      (setv (get @admet-models name) model))
    (return self))

  (meth save-drug-info [filename]
    (when (is @drug-list None)
      (raise (ValueError "drug-list must be loaded first.")))
    (with [f (open filename "w")]
      (@drug-list.to-json f :orient "records" :indent 2)))

  (meth match-drugbank [filename]
    (when (is @drug-list None)
      (raise (ValueError "drug-list is not defined. Call load-drug-queries before match-drugbank.")))
    ;; make sure the provided columnss are strings and not lists of strings
    (setv id-col      (.apply (get @drug-list @id-col-name)      @unwrap-list))
    (setv id-type-col (.apply (get @drug-list @id-type-col-name) @unwrap-list))
    (setv name-col    (.apply (get @drug-list @name-col-name)    @unwrap-list))
    (setv (get @drug-list @id-col-name)      id-col)
    (setv (get @drug-list @id-type-col-name) id-type-col)
    (setv (get @drug-list @name-col-name)    name-col)
    ;; column making for what we're about to store
    ;;                 variable name       column title
    (create-var-column @all-names-column   "DrugBank:All Names")
    (create-var-column @cas-column         "DrugBank:CAS Registry Number")
    (create-var-column @fda-column         "DrugBank:FDA Approved")
    (create-var-column @indication-column  "DrugBank:Indication")
    (create-var-column @mechanism-column   "DrugBank:Mechanism")
    (create-var-column @name-column        "DrugBank:Main Name")
    (create-var-column @price-column       "DrugBank:Prices")
    (create-var-column @smiles-column      "DrugBank:SMILES")
    (create-var-column @unii-column        "DrugBank:UNII")
    ;; make a column to say if this drug has already been matched to DrugBank
    (create-var-column @match-found-column "DrugBank:Match Found")
    (setv (get @drug-list @match-found-column) False)
    ;; go through matches and add info to the correct columns
    (setv drugbank (DrugBank filename id-col id-type-col name-col))
    (for [#(matches element) (drugbank.get-matches)]
      ;; only match things once
      (setv new-matches (& matches (- (get @drug-list @match-found-column))))
      (setv (get @drug-list @match-found-column) (| new-matches (get @drug-list @match-found-column)))
      ;; add new data to matched rows
      ;;              column             drugbank function
      (@add-to-column @all-names-column  drugbank.all-names new-matches element)
      (@add-to-column @cas-column        drugbank.cas-number new-matches element)
      (@add-to-column @fda-column        drugbank.fda-approval new-matches element)
      (@add-to-column @indication-column drugbank.indication new-matches element)
      (@add-to-column @mechanism-column  drugbank.mechanism new-matches element)
      (@add-to-column @name-column       drugbank.name new-matches element)
      (@add-to-column @price-column      drugbank.prices new-matches element)
      (@add-to-column @smiles-column     drugbank.smiles new-matches element)
      (@add-to-column @unii-column       drugbank.unii new-matches element))
    (setv (get @drug-list @name-column) (.apply (get @drug-list @name-column) @unwrap-list)))

  (meth make-main-name-col []
    (when (is @drug-list None)
      (raise (ValueError "drug-list is not defined. Call load-drug-queries before deduplicate.")))
    (when (not-in "DrugBank:Main Name" @drug-list.columns)
      (raise (ValueError "DrugBank data does not exist yet. Run match-drugbank to create it.")))
    ;; find out which rows have a filled DrugBank: Main Name
    (setv name-column (.notna (get @drug-list @name-column)))
    (setv (get @drug-list "Main Name") None)
    ;; set from DrugBank if possible, otherwise fall back to provided name
    (setv (ncut @drug-list.loc (- name-column) "Main Name") (get @drug-list @name-col-name))
    (setv (ncut @drug-list.loc name-column "Main Name") (get @drug-list @name-column))
    (setv (get @drug-list "Main Name") (.str.lower (get @drug-list "Main Name")))
    (print f"MISSING NAMES: {(.sum (.isna (get @drug-list "Main Name")))}"))

  (meth deduplicate []
    (when (is @drug-list None)
      (raise (ValueError "drug-list is not defined. Call load-drug-queries before deduplicate.")))
    (when (not-in "DrugBank:Main Name" @drug-list.columns)
      (raise (ValueError "DrugBank data does not exist yet. Run match-drugbank to create it.")))
    (when (not-in "Main Name" @drug-list.columns)
      (raise (ValueError "Combined 'Main Name' column does not exist yet. Run make-main-name-col to create it.")))
    (setv name-column (.notna (get @drug-list "Main Name")))
    (setv no-name-rows (get @drug-list (- name-column)))
    (setv name-rows (get @drug-list name-column))
    (setv deduplicated-rows
      (-> name-rows
        (.groupby "Main Name")
        (.agg
          (fn [x]
            ;; make a list out of all the items in x
            (setv y [])
            (for [item x]
              (if (isinstance item list)
                (y.extend item)
                (y.append item)))
            ;; turn that into a set to deduplicate it
            (setv z (set y))
            ;; get rid of None elements
            (z.discard None)
            (cond
              ;; turn into bare elements if possible
              (= (len z) 0) None
              (= (len z) 1) (.pop z)
              ;; else return the whole set
              True z)))
        (.reset-index)))
    ;; print a record of what was deduplicated
    (setv merged-list (pd.concat #(no-name-rows deduplicated-rows) :ignore-index True))
    (print "DRUGS REMOVED IN DEDUPLICATION:")
    (print (get (get @drug-list (- (.isin (get @drug-list "Main Name") (get merged-list "Main Name")))) ["Main Name" @name-col-name @all-names-column @name-column @match-found-column]))
    (setv @drug-list merged-list))

  (meth predict-admet []
    (when (is @drug-list None)
      (raise (ValueError "drug-list is not defined. Call load-drug-queries before predict-admet.")))
    (when (is @admet-models None)
      (raise (ValueError "admet-models is not defined. Call load-admet-models before predict-admet.")))
    (when (not-in "DrugBank:SMILES" @drug-list.columns)
      (raise (ValueError "SMILES data does not exist yet. Run match-drugbank to create it.")))
    (RDLogger.DisableLog "rdApp.*")
    ;; unwrap smiles
    (setv (get @drug-list @smiles-column) (.apply (get @drug-list @smiles-column) @unwrap-list))
    (setv smiles-mask (.notna (get @drug-list @smiles-column)))
    (setv smiles (ncut @drug-list.loc smiles-mask @smiles-column))
    (setv molecules (smiles.apply Chem.MolFromSmiles))
    (setv molecules-mask (.notna molecules))
    (setv fingerprints (@get-fingerprints (get molecules molecules-mask)))
    (setv combined-mask (pd.Series False :index @drug-list.index))
    (setv (ncut combined-mask.loc (. (get smiles molecules-mask) index)) True)
    (for [#(name model) (@admet-models.items)]
      (setv predictions (model.predict-proba fingerprints))
      (setv (ncut @drug-list.loc combined-mask name) (ncut predictions : 1))))

  (meth get-fingerprints [molecules]
    (setv fingerprints (list))
    (fingerprints.append (maplight-gnn.get-morgan-fingerprints molecules))
    (fingerprints.append (maplight-gnn.get-avalon-fingerprints molecules))
    (fingerprints.append (maplight-gnn.get-erg-fingerprints molecules))
    (fingerprints.append (maplight-gnn.get-rdkit-features molecules))
    (fingerprints.append (maplight-gnn.get-gin-supervised-masking molecules))
    (np.concatenate fingerprints :axis 1)))


(when (= __name__ "__main__")
  (setv augmenter
    ;(-> (DataAugmenter "data/src/drug_list.csv" "CAS Number" "id_type" "Canonical Name")
    (-> (DataAugmenter "data/translator_drugs.json" "result_id" "id_type" "result_name")
      (.load-drug-queries)
      (.load-admet-models
        {"Blood Brain Barrier" "data/admet/bbb_martins-0.916-0.002.dump"
         "P-glycoprotein Inhibition" "data/admet/pgp_broccatelli-0.938-0.0.dump"
         "Human Intestinal Absorption" "data/admet/hia_hou-0.989-0.001.dump"
         "Drug Induced Liver Injury" "data/admet/dili-0.918-0.005.dump"})))
  ;(setv (get augmenter.drug-list "id_type") "cas-number")
  (doto augmenter
    (.match-drugbank "data/src/drugbank.xml")
    (.make-main-name-col)
    (.deduplicate)
    (.predict-admet)
    ;(.save-drug-info "data/drug_list.json")))
    (.save-drug-info "data/translator_drug_list.json")))
