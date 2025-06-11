#!/usr/bin/env hy

(import json)

(import matplotlib [pyplot :as plt])
(import numpy :as np)
(import seaborn :as sns)

(sns.set-theme)

(with [f (open "data/regular_spl_setids_list.json" "r")]
  (setv data (json.load f)))
;(with [f (open "data/smaller_spl_setids_list.json" "r")]
;  (setv small-data (json.load f)))

(setv shortest-name-length
  (np.asarray
    (tuple
      (map
        (fn [d] (min (tuple (map len (get d "Names List")))))
        data))))

(setv num-setids
  (np.asarray
    (tuple
      (map
        (fn [d] (len (get d "SETID")))
        data))))

;(setv small-shortest-name-length
;  (np.asarray
;    (tuple
;      (map
;        (fn [d] (min (tuple (map len (get d "Names List")))))
;        small-data))))
;
;(setv small-num-setids
;  (np.asarray
;    (tuple
;      (map
;        (fn [d] (len (get d "SETID")))
;        small-data))))

;(for [id (np.setdiff1d (np.where num-setids) (np.where small-num-setids))]
;  (print (get (get data id) "DrugBank Name")))

(setv to-plot (np.where (< shortest-name-length 100)))

(for [#(drug length) (zip data shortest-name-length)]
  (when (= length 3)
    (print (get drug "All Names"))))

(sns.swarmplot 
  :x (get shortest-name-length to-plot) 
  :y (get num-setids to-plot)
  :log-scale #(False True))
(plt.show)
