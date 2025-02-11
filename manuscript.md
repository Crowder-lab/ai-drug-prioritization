# A Novel Method for Prioritization in Rare Disease Drug Repurposing

## Abstract

## Introduction

Rare disease is not rare. Over 6000 recognized rare diseases are extrapolated to affect at least 250 million people worldwide {{ref}}. Many rare diseases still lack effective treatments or cures, often due to the high cost of drug development, small patient populations for clinical trials, and limited research interest {{ref}}.

Drug repurposing is an important tool used to treat rare disease. Using an existing medication avoids the high costs of developing new drugs. It is not a perfect solution, however. For each rare disease, there are many FDA approved drugs that have an effect, but few of them will be a perfect cure. Each drug has positives and negatives that affect their usefulness for a given disease.

Drug repurposing prioritization helps get drugs into patients faster. Testing the effectiveness of drugs that are more likely to be beneficial first means more cost savings, faster turnarounds, and more patients that can be helped.

This paper uses the genetic disease caused by mutations in the MAPK8IP3 gene to illustrate its methods. MAPK8IP3 controls the production of the protein JIP3 in humans {{ref}}. JIP3 helps axonal transport and other stuff {{ref}}. Patients with mutations in MAPK8IP3 have delayed neurodevelopment and myelination, and other bad things {{ref}}.

## Materials and Methods

### Therapeutic Rationale

The molecular mechanisms of a genetic disease form the basis for its therapeutic rationale. The symptoms should be treated as well, but targeting the cause of the symptoms will provide more comprehensive benefits for the patient {{ref}}. The protein created by MAPK8IP3, JIP3, mediates retrograde axonal transport of lysosomes {{ref}}. This was determined by PubMed search, Clinvar, and Varsome. Most recorded mutations in MAPK8IP3 are missense loss of function mutations, so MAPK8IP3 should be upregulated to improve symptoms. Other therapeutic rationales include increasing axonal lysosome transport through other means.

### Finding Drugs

The simplest way to find drugs is by direct search. Given a protein and whether it needs to be up or downregulated, NIH Translator or Drug Gene Budger can be used to find drugs that likely have the desired effects {{ref}}. PubMed can be used to find secondary pathways that connect to or regulate the protein of interest, and search those as well.

The drug list can be expanded by investigating treatments that provide symptomatic relief and improve patient quality of life. Literature, mediKanren, and clinician recommendations are the best sources for these drugs.

### Categorization

Drugs are categorized by therapeutic rationale. The rationale can be tagged as each drug is found, or can be found afterwards. Reading PubMed papers, DrugBank info, and Drugs.com info give a good idea of the different effects of a drug. These can then be matched up to the rationale list generated earlier.

### Data Collection

Prioritizing drugs requires a lot of data. After surveying clinicians, FDA approval, cost, side effects, pediatric safety, prescription frequency, bioavailability, and crossing the blood-brain barrier were determined to be the most important factors in if they would prescribe a drug for repurposing. Our prioritization program pulls FDA approval and cost from DrugBank, bioavailability and crossing the blood-brain barrier are predicted from SMILES by Maplight-GNN, side effects are extracted from SPLs sourced from DailyMed, and pediatric safety and prescription frequency have yet to be figured out.

### Prioritization

Clinicians were also surveyed for how to rank each datum. They responded ... because ...

Each drug repurposing candidate is ranked overall and within its category. This allows for intelligent prioritization of testing. Prioritization can be done by which category is most promising for treatment or using a 'shotgun' approach and trying the best drug from each category.

### Implementation

A pipeline has been used to screen the most promising drugs determined by the program. Using zebrafish (*danio rerio*) as a model organism for their fast breeding and ease of genetic modification different drugs can be tested {{ref}}. Drugs are tested at 0.1, 1, and 10 uM concentrations as is the standard {{ref}}. Many assays are available, and our MAPK8IP3 screening assays test social behavior and morphology which are common indicators of the mutation.

Zebrafish are bred to have the desired mutation. The embryos are then raised in the desired drug and concentration. Zantiks and MicroTracker are used to run our assays {{ref}}. Data analysis is done using R and GraphPad prism {{ref}}.
