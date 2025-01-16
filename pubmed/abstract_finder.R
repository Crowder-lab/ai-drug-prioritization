#!/usr/bin/env Rscript

library(httr2)
library(readr)
library(stringr)
library(xml2)

entrez_request <- function(request_type, query_parameters, api_key = NULL) {
  base <- "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
  filename <- paste0("e", request_type, ".fcgi")
  api_parameter <- if (!is.null(api_key)) paste0("&api_key=", api_key) else ""
  url <- paste0(
    base,
    filename,
    "?db=pubmed",
    api_parameter,
    query_parameters
  )

  response <- request(url) %>% req_perform()
  return(response)
}

# get api key if available
my_key <- str_replace_all(read_file("api_key.txt"), "[\r\n]*", "")

# esearch
term <- "mapk8ip3"
output <- entrez_request(
  "search",
  paste0("&term=", term, "&usehistory=y"),
  my_key
) %>% resp_body_string()
web <- str_extract(output, "<WebEnv>(\\S+)</WebEnv>", group = 1)
key <- str_extract(output, "<QueryKey>(\\d+)</QueryKey>", group = 1)

# efetch
query <- paste0(
  "&query_key=", key,
  "&WebEnv=", web,
  "&rettype=abstract",
  "&retmode=xml"
)
output <- entrez_request(
  "fetch",
  query,
  my_key
) %>% resp_body_xml()
write_xml(output, "data.xml")
