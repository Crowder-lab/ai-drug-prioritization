#!/bin/sh

jq '.[]' data/drug_list.json | bat --language json --style plain
