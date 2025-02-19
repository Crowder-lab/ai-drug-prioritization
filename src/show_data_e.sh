#!/bin/sh

jq '.' < data/drug_list.json | rg -v 'Unnamed: [0-9]+' | bat --language json
