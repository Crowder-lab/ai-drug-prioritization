#!/bin/sh

jq -rf src/json_to_csv.jq data/drug_list.json > data/drug_list.csv
