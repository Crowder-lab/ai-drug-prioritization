#!/usr/bin/env Rscript

library(readr)
library(stringr)
library(tidyverse)

match_drug <- function(query, reference) {

}

fda_list <- read_tsv("Products.txt") %>%
  select(generic_name = ActiveIngredient, brand_name = DrugName)
drug_list <- read_csv("drug_list.csv") %>%
  select(generic_name = `Generic Name`, brand_name = `Brand Name`)
