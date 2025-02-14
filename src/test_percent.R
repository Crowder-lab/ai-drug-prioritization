#!/usr/bin/env Rscript

library(jsonlite)
library(tidyverse)
library(readxl)

# load drug screen data
all_drug_screens_file <- "data/src/all_drug_screens.xlsx"
drug_screens_2023 <- read_excel(all_drug_screens_file,
  sheet = "2023 Drug Screens",
  n_max = 62
)
drug_screens_2024 <- read_excel(all_drug_screens_file,
  sheet = "2024 Drug Screens"
)
drug_screens_2025 <- read_excel(all_drug_screens_file,
  sheet = "2025 drug screens"
)

# load list of analyzed drugs and unroll generic names
drug_list <- read_json("data/drug_list.json", simplifyDataFrame = TRUE) %>%
  as_tibble() %>%
  arrange(`Generic Name`)

# combine with corrected names
drug_screens <- bind_rows(
  drug_screens_2023 %>%
    select(
      drug_name = `Drug Name`,
      status = `Phenotype Improved`,
    ),
  drug_screens_2024 %>%
    select(
      drug_name = Drug,
      status = `Map 1 Status`,
    ),
  drug_screens_2025 %>%
    select(
      drug_name = Drug,
      status = `Map 1 Status`,
    )
)

# convert drug screen data to which ones have been screened
drugs_done <- drug_screens %>%
  mutate(drug_name = str_to_lower(drug_name)) %>%
  group_by(drug_name) %>%
  summarize(unfinished = any(is.na(status)))

# match full list with screened drugs
drug_list <- drug_list %>%
  mutate(name_in_list = mapply(function(generic_name, drugbank_names) {
    generic_lower <- str_to_lower(generic_name)
    drugbank_lower <- str_to_lower(drugbank_names)
    any(drugs_done$drug_name == generic_lower) ||
      any(drugs_done$drug_name == drugbank_lower)
  }, `Generic Name`, `DrugBank Generic Names`)) %>%
  group_by(`Generic Name`) %>%
  summarize(in_screening_list = any(name_in_list))

write_csv(filter(drug_list, !in_screening_list), "data/extra/again.csv")
