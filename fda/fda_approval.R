#!/usr/bin/env Rscript

library(dplyr)
library(readr)
library(stringr)
library(tidyverse)

options(tibble.print_max = Inf)

match_drugs <- function(query, reference) {
  matches <- reference %>%
    left_join(query, by = "generic_name", suffix = c("", "_query")) %>%
    left_join(query, by = "brand_name", suffix = c("", "_query")) %>%
    filter(!is.na(generic_name_query) | !is.na(brand_name_query)) %>%
    select(generic_name, brand_name) %>%
    unique()

  return(matches)
}

fda_list <- read_tsv("Products.tsv") %>%
  select(generic_name = ActiveIngredient, brand_name = DrugName) %>%
  mutate(across(everything(), tolower))
drug_list <- read_csv("drug_list.csv") %>%
  select(generic_name = `Generic Name`, brand_name = `Brand Name`) %>%
  mutate(across(everything(), tolower))

matches <- match_drugs(drug_list, fda_list)

matches
