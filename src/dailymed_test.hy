#!/usr/bin/env hy

(import json)
(import requests)


(setv response (requests.get "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/1efe378e-fee1-4ae9-8ea5-0fe2265fe2d8.xml"))
(print (. response text))
