::: {#main}
# The Algorithm for Precision Medicine {#thealgorithmforprecisionmedicine}

The Algorithm for Precision Medicine is a plan to guide patients and
their caregivers on challenging diagnostic and therapeutic odysseys.

The Algorithm is an evolving distillation of my experience in diagnosing
and then identifying treatments for [my son
Bertrand](http://bertrand.might.net/), and then as [Director of the Hugh
Kaul Precision Medicine Institute at UAB](http://matt.might.net/), where
I've been focused on developing strategies and infrastructure to
identify treatments for the patients that reach out.

Bertrand passed away unexpectedly on October 23rd 2020, so I'm
maintaining this guide on [his site](http://bertrand.might.net/) to keep
his [legacy](http://bertrand.might.net/#life) of science in the service
of patients alive.

If you find this guide helpful, I encourage you to give to the [Bertrand
Might Endowment for Hope at UAB](http://bertrand.might.net/#hopefund), a
permanent endowment whose interest each year goes toward science in the
service of diagnosis and treatment of patients like Bertrand.

As it stands, this document is very much an evolving draft.

I released it as a draft publicly on what would have been Bertrand's
13th birthday because I felt it already had plenty of value for anyone
in a similar situation to where I once was.

I'm keeping it posted even as a draft and updating it regularly because
I don't want the perfect to become the enemy of the good (enough).

Honestly, I haven't had time to fully update it with respect to all of
the advances in my understanding and all of the advances in science and
medicine since then.

But, everything I learned at least has a place-holder in this document
now.

[Feedback on how to improve this document](http://matt.might.net/) is
most welcome, as there will be substantial additions, structural
re-organization, clean-up and revision.

In a real sense, this document will never be finished, so please check
back.

## Summary

[Precision medicine](#define-precision-medicine) focuses on the use of
data (often large molecular data sets) to precisely identify and address
the root cause of disease in a patient.

The term *algorithm* in this case borrows from the notion of a
step-by-step process in computer science.

As presented, The Algorithm for Precision Medicine is meant for patients
with presumed or diagnosed rare genetic disorders.

At a very high level, the Algorithm has two phases:

1.  Identify the molecular cause(s) of a patient's disease.
2.  Identify treatments for the molecular cause(s) of a patient's
    disease.

While the Algorithm as presented is tailored to rare genetic disorders,
it generalizable to help with more common or complex conditions (such as
cancers) where more than one gene or biological process is involved.

[]{#audience}

## Audience and purpose {#audienceandpurpose}

This is a living document that will be updated indefinitely.

It is meant for patients or caregivers that need to go beyond what
medicine has to offer in terms of finding treatments.

The language in this guide is targeted at early-stage undergraduates in
biomedical sciences with some but perhaps not extensive training in
biology.

Given that most patients or families have no such training, there is a
comprehensive [Q&A](#qa) meant to bring patients and their families up
to speed on the relevant terms and concepts. In fact, non-biologists may
benefit from reading the entire [Q&A](#qa) first.

Terms that may not be familiar to readers are often linked to their
entry in the [Q&A](#qa). You may want to open these up in a new tab as
you read.

To make the guide more accessible, I have sometimes used terms more
intuitive to a lay audience (such as *mutation*) at first instead of the
more precise term often used by professionals (such as *variant* or
*allele*).

Most probably don't need to read this document in its entirety. For
example, if you already have a genetic diagnosis, there's no need to
read the material on obtaining a diagnosis.

A second goal of this document is to provide undergraduates in
biomedical sciences the information they need to serve as guides for
patients and families navigating diagnostic or therapeutic odysseys.

More specifically, the Algorithm seeks to identify the set of available
next step(s) a patient could take, whether clinical or scientific, *en
route* to either a diagnosis or a therapy.

If you're already trained in a (non-biomedical) technical field, then I
recommend [Quickstart Molecular
Biology](https://www.amazon.com/Quickstart-Molecular-Biology-Introductory-Mathematicians/dp/1621820343?crid=1JGTQXK17TJOT&keywords=quickstart+molecular+biology&qid=1658339748&sprefix=quickstart+molecul%2Caps%2C78&sr=8-1&linkCode=ll1&tag=mmamzn06-20&linkId=f25ba58292bb573e6898fadca3b20a05&language=en_US&ref_=as_li_ss_tl)
to get up to speed rapidly:

[![](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1621820343&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=mmamzn06-20&language=en_US){border="0"}](https://www.amazon.com/Quickstart-Molecular-Biology-Introductory-Mathematicians/dp/1621820343?crid=1JGTQXK17TJOT&keywords=quickstart+molecular+biology&qid=1658339748&sprefix=quickstart+molecul%2Caps%2C78&sr=8-1&linkCode=li3&tag=mmamzn06-20&linkId=304e695567cfcde849c64c26bebbf2e7&language=en_US&ref_=as_li_ss_il){target="_blank"}![](https://ir-na.amazon-adsystem.com/e/ir?t=mmamzn06-20&language=en_US&l=li3&o=1&a=1621820343){width="1"
height="1" border="0"
style="border:none !important; margin:0px !important;"}

If you have a technical background, you can digest this book in about a
day.

[]{#disclaimer}

## Disclaimer

Before you read any further, please realize that this document has been
constructed by the father of a [patient with an ultra-rare genetic
disorder](http://bertrand.might.net/) -- not a licensed medical
professional.

It is a distillation of many years of experience after [my
son](http://bertrand.might.net/) was diagnosed as the first patient with
his particular genetic disorder and since I switched careers from
academic computer science to academic medicine.

As a result, it is critical to validate any information in this article
with a trained medical professional and a scientific team with relevant
domain expertise.

**If the process described herein leads you to make predictions about
potential diagnoses or treatments, do *not* use them in any way without
consulting a qualified health care provider.**

For patients and their advocates, my hope is that this guide will serve
as a launching point for questions and discussions with professionals,
and that it will save individuals on similar journies significant time.

## Precision medicine in a nutshell {#precisionmedicineinanutshell}

This section provides a very high-level summary of the entire Algorithm
for Precision Medicine.

The first phase of the Algorithm for Precision Medicine is the
diagnostic phase -- [the identification of the (ideally root) molecular
cause(s) of a disease](#process-obtaining-genetic-diagnosis).

In rare genetic disorders, the root molecular cause is usually a
mutation in a gene or two mutations in the same gene.

The second phase of the algorithm is the therapeutic phase: in which
knowledge of the molecular cause(s) of a patient's disease enables the
discovery of therapies.

At a high level, the therapeutic phase of the algorithm for precision
medicine has two (and not mutually exclusive) internal algorithms: a
rational algorithm and an empirical algorithm.

The rational algorithm attempts to *predict* or *design* a treatment
(often computationally) based on a root [mechanism of
harm](#mechanism-of-harm).

The empirical algorithm attempts to find a treatment through
experimentation such as drug screening.

In practice, these two branches will interleave with each other, as the
rational approach may lead to a question best answered experimentally or
an experiment may enable a new rational prediction about therapies.

The rational can also serve as a filter for the empirical: instead of
testing all existing drugs empirically, only drugs predicted to work
under with the rational algorithm can then be tested empirically for
validation.

### Summary: The Rational Algorithm for Precision Therapeutics {#summary:therationalalgorithmforprecisiontherapeutics}

The [Rational Algorithm for Precision
Therapeutics](#process-identifying-therapeutics-rationally) proceeds
from the root molecular cause(s) of the disease toward rational
predictions of how to reverse those causes, and it has two major phases:

1.  For each [mechanism of harm](#mechanism-of-harm), [determine the
    impact on that mechanism](#process-analyzing-impact), that is,
    whether it results in:

    -   overactivity;
    -   underactivity;
    -   absence of activity; or
    -   introduction of toxicity

    for each biological process involved.

2.  Reverse the impact on those mechanisms of harm, which may involve:

    -   decreasing activity;
    -   increasing activity;
    -   compensating for or replacing the absence of activity; or
    -   elimination of toxic activity.

Within the rational algorithm, there are also some strategies that only
apply to specific types of genetic defects or specific classes of
proteins -- for example, [readthrough compounds for premature stop
mutations](#readthrough-therapeutics).

The class of therapies considered under this rational approach include
both small molecules and gene-based therapies.

Gene-based therapies include replacing a missing gene (gene therapy or
biologics); fixing a broken gene (gene editing); or dynamically altering
a broken gene (such as with antisense oligonucleotides).

As a word of caution, of the gene-based approaches, only antisense
oligonucleotides are approaching tractability at the level of single
patients at present.

### Summary: The Empirical Algorithm for Precision Therapeutics {#summary:theempiricalalgorithmforprecisiontherapeutics}

The empirical algorithm for precision medicine attempts to identify both
drugs and drug targets with experimentation:

1.  Create a [precision disease model](#precision-disease-model) that
    represent a patient's disease.

2.  Phenotype the precision disease model.

3.  Screen potential therapies against the disease model.

4.  If no potential therapies are identified, then run experiments to
    identify drug *targets*, and then feed these drug targets back into
    the high-level Algorithm for Precision Medicine to find potential
    therapies.

5.  Adapt potential therapies identified via the model to human beings.

## Key learnings {#keylearnings}

If you want to skip reading the rest of the document, here are the key
learnings from my experience when it comes to precision medicine:

1.  **Once it 'seems genetic,' conduct exome or genome sequencing.**
    Don't waste time with gene panels and gene tests during the
    diagnostic odyssey.

<!-- -->

1.  **Don't stop at a 'negative' result with sequencing.** If sequencing
    doesn't find an answer, have the sequencing data evaluated by other
    teams and at regular intervals over time as the literature advances
    understanding. Plenty of patients get a diagnosis from a different
    team or at a later date from the same data. When genomic sequencing
    fails, ask if transcriptomic sequencing may help.

2.  **Your geneticist may not be the best scientist to work on your
    condition.** I was lucky that the geneticists that discovered my
    son's disease told me that they were not the right scientists to
    carry forward research on the disease, and instead routed me to a
    glycobiologist that could. After the diagnosis, the key next step is
    to identify the best scientist for the relevant biology. I've seen
    an alarming number of families fund research for the geneticist that
    diagnosed their child. To be blunt, with rare and notable
    exceptions, once the geneticist has made the diagnosis, their work
    toward identifying a treatment is done.

3.  **Build community *and* collegiality.** It's really hard to do this
    alone, so you'll want as many other patients with you as you can
    get. But beware the systemic divisiveness that sets in within even
    the smallest rare disease communities. I've seen disease after
    disease where warring factions in the community end up becoming more
    focused on who will get credit for a cure that never comes than
    actually finding the cure. This internecine warfare is measured in
    the bodies of dead patients whose lives were cut short by hamstrung
    science. Commit to openness and collaboration, even if you're the
    only one that does. In the end, it doesn't matter who finds the cure
    -- only that it is found.

4.  **You don't have to understand a disease to find a treatment for
    it.** Most drugs are identified by creating a model of the disease
    and then testing lots of drugs against the model, so a perfectly
    reasonable strategy is to build a model, and then screen on it; then
    build another one and screen again. It is possible go all the way to
    a drug in humans without knowing exactly why it works.

5.  **Invest more in the translational over the basic.** Building on the
    last point, while there is always a chance that basic science could
    leap from understanding to treatment, this is rarely the case. Focus
    on the end point: finding a treatment, and work backward through
    what is necessary to do that. Basic science may not be on the path
    at all. From a portfolio-balancing perspective, 80% translational
    research and 20% basic research is probably about the right mixture.

6.  **Repurposing an exsisting drug is the most realistic option for
    most patients.** Developing novel therapies is time-consuming and
    costly. Finding an existing drug that ameliorates aspects of the
    condition is probably going to be the most time- and cost-effective
    approach. Many become enamored with gene therapy at first, only to
    find that the path toward seeing it in a human being is too long and
    too costly to help in time.

7.  **Cells, fish, flies and mice are not people.** Just because
    something works in cells in a dish or in a model doesn't mean it's
    going to work well or work safely in a human. (That said, these
    models are still highly effective and efficient routes to finding
    treatments.). There may be a long process of medicinal chemistry to
    take something from the bench to the bedside. Getting a compound
    that works to all the right tissues at the right (and safe)
    concentrations is a major challenge. They key questions once a drug
    "works" on cells or mice are: (0) What is the anticipated dose? (1)
    Does the drug work at a concentration that corresponds to safe
    dosing in humans? (2) Will the drug reach the right places, e.g.,
    the brain? (3) How long would the drug remain at active
    concentrations in the body for the anticipated dose? (4) What safety
    issues come with long-term use of the drug at the anticipated dose?

8.  **Better is good enough.** Many patients and parents assume that
    only a cure is acceptable, and while a cure is absolutely worth
    aiming for and the goal of this document, you may still find that if
    you fall short and "merely" improve quality of life for the patient,
    that being *better* (if not *cured*) is actually a substantial
    improvement in the quality of life for the caregiver.

9.  **Regulatory hurdles may be greater than scientific ones.** All
    patients need to advocate with their legislators to mandate that
    regulators provide broader regulatory flexbility for rare and
    life-threatening illnesses.

10. **Spend time with your child.** If you're a parent or grandparent
    intent on racing toward the cure or treatment for a child, please
    remember to also spend as much time with them as you can. This is a
    difficult journey and while hope is always appropriate, and while
    science always delivers in the long run, it may not deliver on time.
    Balance the time on the quest for treatment against the value of the
    time you may never get back.

## Following The Algorithm for Precision Medicine {#followingthealgorithmforprecisionmedicine}

The Algorithm for Precision Medicine is best understood as a collection
of individual processes that are connected together.

In some cases, one process requires another.

In others, one process leads to another.

Some of these processes are useful for the diagnostic phase (e.g.
analyzing genetics); some are useful for the therapeutic phase (e.g.
conducting drug screens); some are useful for both phases (e.g. building
model organisms).

The entry point into the Algorithm is obtaining a molecular (e.g.
genetic) diagnosis, and there is a [process defined for obtaining a
genetic diagnosis](#process-obtaining-genetic-diagnosis).

After the molecular diagnosis is made, the Algorithm shifts to the
[process for finding precision
therapeutics](#process-identifying-precision-therapeutics).

[]{#guide}

[]{#process-obtaining-genetic-diagnosis} []{#genome-sequencing}

## Process: Obtaining a genetic diagnosis {#process:obtainingageneticdiagnosis}

[Exome](#exome) and [genome](#genome) [sequencing](#sequencing) are
powerful techniques for diagnosing [conditions with a suspected genetic
cause](#genetic-disorder).

For these conditions, sequencing has the advantage of being able to look
at all genes simultaneously.

For many patients on diagnostic odysseys, sequencing is their only hope
of ending them.

Genetic panels, which look at a subset of all genes, and chromosomal
analyses, which look at higher-level abnormalities in chromosomal
structure (such as deletions, duplications and re-arrangements), may
also be used.

Sequencing can find genetic changes, or [mutations](#mutation), of
interest. (Geneticists often use the closely related word *variant* to
describe a specific genetic change or mutation.)

For patients that have been on intractable diagnostic odysseys, the
NIH-funded [Undiagnosed Diseases
Network](http://undiagnosed.hms.harvard.edu/) specializes in using
advanced precision medicine to deliver diagnoses. In Alabama, patients
can apply for [Undiagnosed Diseases
Program](https://www.uab.edu/medicine/genetics/patient-care/clinical-services/undiagnosed-diseases)
at UAB.

After genetic analysis, an important next step to [interpret the meaning
of the mutations](#variant-interpretation) discovered.

### Next steps if there is no diagnosis {#nextstepsifthereisnodiagnosis}

Unfortunately, genetic analysis does not always lead to a diagnosis.

In some cases, there are multiple plausible candidate mutations, but
none can be definitively linked to the condition, and in others, no
plausible candidate mutations are found.

-   If plausible but not definitive candidates emerge among the
    mutations, then the next steps are to determining which approaches
    were used to analyze [pathogenicity](#pathogenic), and attempting
    those which were not, which may include techniques less common in a
    clinical setting, including:

    1.  [structural analysis](#process-analyzing-protein-structure) of
        the protein;
    2.  [conducting functional studies](#functional-studies-mutations);
        and
    3.  [finding additional patients](#finding-patients).

-   If no plausible candidates are identified, then next steps are:

    1.  to use [genome](#genome) sequencing if [exome](#exome)
        sequencing was used;
    2.  to consider [somatic mosaicism](#somatic-mosaicism) and other
        potentially confounding factors;
    3.  to pursue other "omics" beyond genomics, including
        [transcriptomics](#transcriptomics) and
        [proteomics](#proteomics); and
    4.  to consider whether there are epigenetic modifications that
        could be driving disease.

-   While unconventional, [crowd-sourcing](#crowd-sourcing) the
    interpretation of a mutation or genotype over social media (such as
    in a blog post), may yield insight.

[]{#process-analyzing-impact} []{#variant-interpretation}
[]{#mutation-analysis}

## Process: Interpreting genetic findings {#process:interpretinggeneticfindings}

At the conclusion of a genetic analysis, a patient may have a diagnostic
report that contains several [mutations](#mutation) identified. (Reports
usually call mutations *variants*.)

The report may label these according to their
[pathogenicity](#pathogenic) as:

-   benign,
-   likely benign,
-   uncertain significance,
-   likely pathogenic, or
-   pathogenic.

Since every human being has many [mutations](#mutation) within their
genome, merely finding mutations in a patient's genome is not grounds
for concluding that those mutations are the cause of a
[condition](#genetic-disorder).

In fact, most mutations are benign on their own -- or not
disease-causing if only one allele is affected -- so it is important to
consider combinations of mutations as well.

Each mutation (or the [genotype](#genotype) collectively) must be
interpreted to determine whether or not it could plausibly contribute to
the [phenotype](#phenotype) of the patient.

### Types of interpretation: Pathogenicity and impact {#typesofinterpretation:pathogenicityandimpact}

When the interpretation of a genotype is meant to determine whether it
is disease-causing or not, it is referred to as interpretation of
[pathogenicity](#pathogenic).

Determining pathogenicity is key to obtaining a diagnosis.

A *deeper* interpretation of a genotype -- functional impact analysis --
tries to figure out how the genotype alters the function of the affected
gene, which can be broadly one of four possibilities:

-   gain of function / overactivity, in which activity increases;
-   partial loss of function / underactivity, in which activity
    decreases;
-   total loss of function / absence, in which function is lost (or
    almost entirely lost); or
-   toxification, in which the mutant gene product is actively toxic
    when present.

Impact analysis is crucial *after* pathogenicity has been determined on
the road to finding a therapy, as it is the basis for the [Rational
Algorithm for Precision
Therapeutics](#process-identifying-therapeutics-rationally).

In some cases, however, impact analysis maybe necessary to support a
determination of pathogenicity: finding that a mutation significantly
alters the function of a gene raises the likelihood that it is
pathogenic.

### Methods for interpretation of pathogenicity and/or impact {#methodsforinterpretationofpathogenicityandorimpact}

While there are some principles that can aid in interpreting the
pathogenicity and/or impact of mutations, it is a challenging task, and
while there are techniques to aid, there is not a universal process
guaranteed to reach a conclusion.

Achieving consistent interpretations of genotypes is a significant
challenge at present.

For pathogenicity, the [ACMG variant analysis
guidelines](http://www.nature.com/gim/journal/v17/n5/full/gim201530a.html)
provide a baseline set of techniques and resources to use during the
interpretation of variants.

Several methods may aid the process of interpretating pathogenicity:

1.  [Finding additional patients](#aid-finding-patients).
2.  [Assessing segregation and inheritance
    patterns](#aid-assessing-inheritance).
3.  [Analyzing frequency in the population](#aid-analyzing-frequency).
4.  [Analyzing conservation](#aid-analyzing-conservation).

Several methods may help with interpreting pathogenicity or impact:

1.  [Exploring the type of mutation and functional
    predictions](#aid-functional-impact).
2.  [Conducting functional studies](#aid-functional-studies).

[]{#aid-finding-patients}

### Aiding interpretation: Finding additional patients {#aidinginterpretation:findingadditionalpatients}

Given the difficulty of interpreting [mutations](#mutation), finding
another patient with a matching or similar [genotype](#genotype) is a
powerful means of confirming [pathogenicity](#pathogenic).

Searching for additional cases in databases such as
[PubMed](http://www.ncbi.nlm.nih.gov/pubmed),
[ClinVar](http://www.ncbi.nlm.nih.gov/clinvar/),
[DECIPHER](https://decipher.sanger.ac.uk/),
[OMIM](http://www.omim.org/),
[HGMD](http://www.hgmd.cf.ac.uk/ac/index.php),
[MyGene2](https://mygene2.org/) and
[dbGaP](http://www.ncbi.nlm.nih.gov/gap) may be able to find another
case for a [gene](#gene) of interest.

Less conventional resources, such as [Google](http://www.google.com/)
and [Wikipedia](http://www.wikipedia.org/), should also be searched in
case clinicians, researchers or even patients themselves have posted
relevant information online about a gene or variant.

When searching less structured resources, it is important to consider
all names for a gene (in both humans and other organisms).

For example, the equivalent of the gene NGLY1 is called PNGase in other
organisms (and more recently is sometimes erroneously called CDGIV or
CDG1V).

If one specific variant is strongly suspected to be pathogenic, putting
up a website / social media page for the gene and the variant may
attract other patients looking for information on that gene because it
has showed up in a genetic report for them as well.

[]{#aid-assessing-inheritance}

### Aiding interpretation: Assessing segregation and inheritance patterns {#aidinginterpretation:assessingsegregationandinheritancepatterns}

If more than one relative is impacted (such as two siblings), combining
genotypic and phenotypic data from multiple relatives -- both healthy
and affected -- can aid in determining the pathogenicity of a mutation
and the [pattern of inheritance](#pattern-of-inheritance) of a
condition.

If a condition is [dominant](#dominant), then relatives with a causative
pathogenic allele should present with the condition. The caveat is that
not all pathogenic alleles are fully [penetrant](#penetrance), meaning
that sometimes, people with pathogenic alleles don't present with a
condition.

If a condition is [autosomal recessive](#recessive), then only relatives
with two causative pathogenic alleles should present with the condition.

Reasoning backward, potential patterns of inheritance also provide
grounds for additional scrutiny. For example:

-   Because of their rarity, cases where both [alleles](#variant) of an
    [autosomal](#autosome) gene harbor an apparent loss of function
    mutation (either in [compound heterozygous](#compound-heterozygous)
    form or [homozygous](#zygosity) form) should raise suspicion of a
    possible [recessive](#recessive) disorder.

-   If a mutation is [*de novo*](#de-novo) -- meaning the mutation does
    not exist in either parent -- then it warrants greater scrutiny.

[]{#aid-analyzing-frequency}

### Aiding interpretation: Population frequency {#aidinginterpretation:populationfrequency}

The frequency of an allele in a genomic population database such as
[gnomad](https://gnomad.broadinstitute.org/) also hints at
pathogenicity: pathogenic alleles tend to be rarer.

[]{#aid-analyzing-conservation}

### Aiding interpretation: Analyzing conservation {#aidinginterpretation:analyzingconservation}

Evolutionary conservation, examined using tools such as the [UCSC genome
browser](http://genome.ucsc.edu/), can also be supporting evidence of
pathogenicity.

For example, if a particular [amino acid](#amino-acid) remains the same
in versions of the gene across species, it is an indication that natural
selection is protecting against change in that amino acid, and changes
to such an amino acid are more likely to be pathogenic.

Looking at genes that co-evolve with a gene of interest with [ERC
analysis](http://csb.pitt.edu/erc_analysis/) may also yield clues as to
the functional role of the gene.

### Aiding interpretation: Predicting damage to function {#aidinginterpretation:predictingdamagetofunction}

Before getting into more fine-grained interpretation regarding
functional impact, it may be possible to predict whether or not a
mutation is "damaging."

Tools such as [PolyPhen2](http://genetics.bwh.harvard.edu/pph2/),
[MutationTaster](http://www.mutationtaster.org/),
[SIFT](http://sift.jcvi.org/), and the [Ensembl variant
predictor](http://useast.ensembl.org/Homo_sapiens/Tools/VEP) will
attempt to predict the effect of mutations for [proteins](#protein),
although a geneticist or genetic counselor needs to audit the results.

Related genes should be studied as well for known or suspected
pathogenicity. The [STRING database](http://string-db.org/) and
[Genemania](http://www.genemania.org/) report potential interactions
between [proteins](#protein) that could suggest additional hypotheses
and analyses.

Searching [Google](http://www.google.com/) and
[PubMed](http://www.ncbi.nlm.nih.gov/pubmed) may identify animal or cell
models with mutations in a gene of interest demonstrating an effect
relevant to the clinical presentation.

[]{#aid-functional-impact}

### Aiding interpretation: Predicting functional impact of a genotype {#aidinginterpretation:predictingfunctionalimpactofagenotype}

In predicting the functional impact of a genotype, the goal is to
determine whether the genotype results in:

1.  overactivity;
2.  underactivity;
3.  absence of activity; or
4.  introduction of toxic activity.

Many [genetic disorders](#genetic-disorder) can be lumped into one of
four classes according to their impact on the function of a gene: gain
of function (overactivity); partial loss of function (underactivity);
total loss of function (absence of activity); or introduction of
dominant-negative toxicity (toxic activity).

A total loss of function often results when:

1.  both alleles for a gene in an [autosomal recessive](#recessive)
    disorder are impacted by loss of function mutations;

2.  the only allele in an [X-linked](#x-linked) disorder is impacted by
    a loss of function mutation;

A partial loss of function often results one when one allele in a
[haploinsufficient](#haplosufficient) gene suffers a loss of function
mutation.

A gain of function results when a mutation causes an *increase* in
activity.

Introduction of toxicity through a mutation can happen in several ways.

For example, if a protein is critical in complex or polymer formation,
if one allele is damaged, it can result damaged complexes and poylmers.

It's also possible that a mutation can cause a protein to become
aggregation-prone, and the aggregates themselves could become harmful.

Determining the functional impact in the mechanism of harm enables
application of the [Rational Algorithm for Precision
Therapeutics](#process-identifying-therapeutics-rationally) as a next
step.

## Aiding interpretation: Examining mutation type {#aidinginterpretation:examiningmutationtype}

In same cases, the *type* of a mutation can directly predict the impact:

-   A [premature stop mutation](#premature-stop) usually leads to loss
    of function for a [protein](#protein) encoded by that
    [allele](#variant).

-   A [frameshift mutation](#frameshift) usually lead to the loss of
    function for a protein encoded by that [allele](#variant).

-   An [in-frame mutation](#in-frame) or [missense mutation](#missense)
    may not lead to loss of function, but it deserves closer scrutiny
    if:

    -   it is in a [domain of function](#domain); or

    -   it is in a [codon](#standard-genetic-code) that impacts
        [post-translational
        modification](#post-translational-modification); or

    -   it is in a [codon](#standard-genetic-code) that impacts
        [post-primary protein structure](#primary-protein-structure);

    -   it changes the side-chain family of the [amino
        acid](#amino-acid).

-   A [synonymous mutation](#synonymous) should not impact
    [protein](#protein) function, but it may damage [RNA
    splicing](#splicing), and in rare cases, a synonymous mutation can
    alter translational dynamics just enough to alter folding of a
    protein.

Given the location and type of the mutation, expertise in the structure
of the protein or the gene may yield insight into its potential impact.

#### Case: Mutations in a functional domain {#case:mutationsinafunctionaldomain}

Mutations within a [domain of function](#domain) should be viewed with
increased suspicion, as these have a greater chance of disrupting the
activity of the protein.

Consult the [NCBI protein
database](http://www.ncbi.nlm.nih.gov/protein/) or for known domains for
a protein.

[Computer modeling](#process-analyzing-protein-structure) may be able to
predict alteration of [binding affinity](#binding-affinity) for binding
partners of the domain.

#### Case: Mutations impacting post-translational modification {#case:mutationsimpactingpost-translationalmodification}

A mutation (especially a [missense mutation](#missense) or an [in-frame
mutation](#in-frame)) that enables or disables [post-translational
modifications](#post-translational-modification) warrants greater
scrutiny for [pathogenicity](#pathogenic).

There are a variety of tools for predicting [post-translational
modification
sites](http://www.expasy.org/proteomics/post-translational_modification).

For example, the loss of a [phosphorylation](#define-phosphorylation)
site that is used to inhibit activity could lead to gain of function.

#### Case: Mutations impacting post-primary structure {#case:mutationsimpactingpost-primarystructure}

A mutation (especially a [missense mutation](#missense) or an [in-frame
mutation](#in-frame)) that could potentially modify the secondary,
tertiary or quaternary structure of a protein (or resulting
[complex](#protein-complex)) warrants scrutiny for
[pathogenicity](#pathogenic).

[Analyzing protein structure](#process-analyzing-protein-structure) is a
complex process that includes both computational and experimental
methods.

For example, two cysteines distant from one another in the sequence can
form disulfide bonds within a protein as it folds. Changing either
cysteine into a different amino acid breaks the ability to form the
disulfide bond.

#### Case: Mutations that impact splicing {#case:mutationsthatimpactsplicing}

Mutations (including intronic mutations) that damage [RNA](#RNA)
[splicing](#splicing) (which might even appear to be
[synonymous](#synonymous) in some cases) can severely limit or eliminate
production of the [protein](#protein).

The tool [ESE2](http://rulai.cshl.edu/tools/ESE2/) can help identify
splicing errors.

[Transcriptomics](#transcriptomics) may help to identify splice-altering
variants directly.

#### Case: Mutations in non-coding regions {#case:mutationsinnon-codingregions}

Mutations outside of the [exome](#exome) can be difficult to interpret.

For example, if a mutation were to occur in the promoter region for a
gene, it could disrupt [transcription](#transcription) of the gene,
leading to loss of function for that [allele](#variant).

[]{#aid-functional-studies} []{#functional-studies-mutations}

### Aiding interpretation: Functional studies {#aidinginterpretation:functionalstudies}

Functional studies of mutations in a laboratory may help determine
pathogenicity.

Functional studies involve analysis of a [precision disease
model](#precision-disease-model) -- cell lines or even whole [model
organisms](#process-creating-model-organisms), such as a mouse, fly or
worm -- that represent the disease in an easier-to-study system.

A model organism or cell line (if not from the patient) can be
genetically modified to have a genotype similar or equivalent to the one
under investigation.

In practice, functional studies require [identifying an
expert](#identifying-an-expert) in the [gene](#gene) or related genes to
design an experiment that would support or refute
[pathogenicity](#pathogenic) for the [genotype](#genotype).

For example, if a mouse bearing the mutation(s) (or equivalent) presents
with a [phenotype](#phenotype) corresponding to the patient, then this
is supporting evidence of [pathogenicity](#pathogenic).

For interpretation, the [Monarch
Initiative](http://monarchinitiative.org/) can compare phenotypes across
species.

If studying cell lines with an [assay](#assay) related to activity of
the gene reveals that the mutation has caused gain of function for the
gene involved, then the mutation should draw additional scrutiny.

If no [assays](#assay) exist to examine the direct or indirect
hypothesized [mechanisms of harm](#mechanism-of-harm), it may be
necessary to [discover an assay](#discovering-assays).

[Identifying an expert](#identifying-an-expert) will be critical to any
of these tasks.

### Aiding interpretation: Special case: Impact on a transporter protein {#aidinginterpretation:specialcase:impactonatransporterprotein}

If a mechanism of harm for the disorder disrupts a [transporter
protein](#transporter-protein) (such as an [ion channel](#ion-channel)),
the defect may increase, decrease or halt the flow of a molecule across
a membrane.

A damaging mutation in a transporter protein means the protein is broken
in some way. Since a membrane [transporter
protein](#transporter-protein) acts like an automatic door, there are
three ways that a door can suffer a "loss of function":

1.  gain of conductance: a door that is stuck open lets in too much;

2.  loss of conductance: a door that is stuck closed lets in too little;
    or

3.  loss of selectivity: a door that now lets the wrong things in or
    out.

When dealing with a defect in a membrane transporter, is absolutely
critical to know whether the defect is causing a *gain* in traffic or a
*loss* in traffic -- or a change in traffic.

In addition, defects related to the ligand in a ligand-gated transporter
protein offer the possibility of intervening at the level of the ligand
rather than the channel.

Cystic fibrosis -- as a total loss of function (in the sense of closure)
in a chloride channel -- is an example of a transporter protein defect
with a recent track record of success in finding treatments.

[]{#analyzing-chromosomal-abnormality}

### Interpreting chromosomal abnormalities {#interpretingchromosomalabnormalities}

High-resolution karyotyping and next-generation sequencing can also
detect chromosomal abnormalities.

Chromosomal abnormalities usually impact many genes simultaneously,
leading to duplicated copies of many genes or deleted copies of many
genes (or both).

The next step is to determine which genes have been impacted, and then
to attempt \[molecular therapeutics\] on a gene-by-gene basis.

Using the [UCSC genome browser](http://genome.ucsc.edu/), one can look
up the genes found in the affected regions.

A diagnostic report should indicate the specific abnormality:

-   In a chromosomal deletion, the set of genes in the fragment have
    been deleted.

-   In a chromosomal duplication, the set of genes in the fragment have
    been duplicated.

-   In a chromosomal translocation, fragments of two chromosomes have
    swapped, which may be balanced (indicating no genes lost or
    duplicated) or unbalanced (indicating possible duplicated and lost
    genes).

A diagnostic report should also include the regions impacted in
[cytogenetic notation](#cytogenetic-notation).

[]{#investigational-studies-mechanism}

## Process: Investigating the mechanism(s) of harm / Conducting basic science {#process:investigatingthemechanismsofharmconductingbasicscience}

While it is critical to identify the root cause of a disease by
[interpreting genetic findings](#process-analyzing-impact), there may be
benefit to continuing a basic scientific investigation beyond variant
interpretation or variant impact analysis.

Specifically, it is also useful (when feasible) to unearth the
downstream mechanisms of harm that emerge from this root cause.

For example, if a patient has seizures, the underlying genotype by
itself may not explain how this ultimately disrupts physiology enough to
cause them.

Determining the [pathogenicity](#pathogenic) of a mutation often does
not involve causally linking the underlying gene or variant to all of
the high-level symptoms of the patient. (For example, when a second case
is identified to confirm the cause, there may still be no knowledge as
to *why* it is causal.)

It may be difficult to treat a disease if the [chain of
events](#mechanism-of-harm) (starting with a mutation) that cause harm
to the patient are not understood: the root cause itself may be
extremely challenge to address therapeutically.

The [chain of causality](#mechanism-of-harm) between a pathogenic
genotype and a high-level symptom may be lengthy, but each link in the
chain offers yet another opportunity to attempt the identification of
therapeutics.

Targeting a later link in the chain is easier than targeting the initial
cause, with the expectation that focusing on downstream mechanisms may
bring less general relief.

Investigational studies can proceed bottom-up from the cell biology, or
they can move top-down from the natural history studies and model
organisms.

Ideally, these studies should move in both directions and generate
hypotheses for the other to test.

Unfortunately, investigational studies like these are more basic than
translational science in nature, and so require careful partnership with
basic scientists with the appropriate expertise.

**It is critical to note that it is entirely possible in many cases to
identify a treatment without uncovering any links in the chain of
causality between root cause and symptom.**

If resources are constrained (as they usually are), there is likely more
payoff to proceeding directly to [techniques to identify
therapies](#process-identifying-precision-therapeutics) than in basic
scientific studies.

A notable exception to this rule are [natural history
studies](#process-conducting-natural-history-studies), which while basic
in nature, may have significant value both scientifically and with
regulators toward the end of the therapeutic identification process, as
studies proceed toward clinical trials in human beings.

If there is to be a significant effort in basic science, then it is
useful to:

1.  [conduct natural history studies of
    patients](#process-conducting-natural-history-studies);

2.  [identify or develop assays to measure mechanisms of
    harm](#discovering-assays);

3.  [identify biomarkers](#identifying-biomarkers);

4.  [establish cell lines](#creating-cell-lines);

5.  [establish biobanks](#creating-biobanks);

6.  [conduct investigational studies into phenotypic
    modifiers](#investigational-studies-modifier); and

7.  [establish or enhance the patient community](#finding-patients).

Most of these tasks will require [identifying an
expert](#identifying-an-expert).

In some cases, the function of a protein whose activity has been altered
will help determine the next steps in the chain of causality.

### Determining downstream mechanisms of harm with kinases {#determiningdownstreammechanismsofharmwithkinases}

If a [kinase](#define-kinase) has altered activity, then the immediate
downstream targets which it phosphorylates are also likely to have
altered activity.

Thus finding the targets of a kinase are the next step in determining
mechanisms of harm.

[]{#process-analyzing-protein-structure}

## Process: Analyzing protein structure {#process:analyzingproteinstructure}

In the search for both a diagnosis and a therapy, it is sometimes useful
to analyze (or "solve") the 3D structure of a protein.

For example, [computer modeling can look for drugs that interact with
the 3D structure of a protein](#process-virtual-screening).

In some cases, it is useful to see how the 3D structure of a protein has
been impacted by a mutation: understanding how the shape of a protein
changes after mutation can indicate how the behavior of the protein has
changed (or not changed).

For example, if a critical amino acid in the pore of an ion channel
changes from a negative side chain to a positive side chain, it could
have a significant impact on the ability of the appropriate ions to flow
through the channel.

Analyzing protein structure is a rich field of study, with multiple
methods available, including:

-   [homology modeling](#homology-modeling), in which known a structure
    for the protein (or similar protein, even perhaps from another
    species) is modified to account for the mutation;

-   [protein folding](#protein-folding), in which the structure of the
    protein is solved from scratch computationally; and

-   [crystallography](#crystallography), in which physical methods are
    used to determine the structure of the protein.

[]{#finding-patients}

## Process: Finding other patients and building community {#process:findingotherpatientsandbuildingcommunity}

It is difficult to find a therapy for a single patient.

A community is useful not only for the resources and talents its members
bring, but because it takes a community of patients to isolate the core
[phenotype](#phenotype) of a disorder.

Examining the frequency of potentially pathogenic [alleles](#variant) in
a database like [gnomad](https://gnomad.broadinstitute.org/) or the
[Exome Variant Server](http://evs.gs.washington.edu/EVS/) allows
estimation of the number of other patients in the world.

There are several genetic databases available to search for a matching
patient, such as:

-   [dbGaP](http://www.ncbi.nlm.nih.gov/gap);
-   [ClinVar](http://www.ncbi.nlm.nih.gov/clinvar/); and
-   [DECIPHER](https://decipher.sanger.ac.uk/).

And, there is a large collection of such databases pooled together
through [MatchMaker Exchange](http://www.matchmakerexchange.org/).

[Using the internet and social media can also help to identify these
patients](http://matt.might.net/articles/rare-disease-internet-matchmaking/).

When encountering a possible new patient, it is important to realize
that matching on the same gene in a diagnostic report does not
automatically imply that he or she has the same disease.

For each potential second patient, his or her [genotype must be
examined](#mutation-analysis) to ensure that it is sufficiently similar
and that the presumed [pattern of inheritance](#pattern-of-inheritance)
matches.

For example, if a disorder is recessive, it is important to ensure that
the second patient is not simply a [carrier](#carrier).

See also:

-   [A guide to rare-disease matchmaking on the
    internet](http://matt.might.net/articles/rare-disease-internet-matchmaking/).

### Next steps {#nextsteps}

As a patient community begins to grow, there are important next steps to
be taken in parallel, including:

-   [conducting natural history
    studies](#process-conducting-natural-history-studies);

-   creating non-profit foundations to fund research; and

-   establishing a patient registry.

[]{#process-conducting-natural-history-studies}

## Process: Conducting natural history studies {#process:conductingnaturalhistorystudies}

A natural history study for a cohort of patients is a scientific study
that observes how phenotypes evolve for each patient individually and
collectively over time.

It is important to study many patients, because the phenotype for most
conditions varies, and a natural history study will help identify the
core of the phenotype.

Regulatory agencies such as FDA prefer having strong, longitudinal
natural history data for clinical trials.

Natural history studies are critical for:

-   being able to predict the progression of a condition;
-   associating genotype with phenotype;
-   identifying the core features of a disorder; and
-   uncovering [biomarkers](observable).

Treatment strategies directed at the core features of a disorder are
more likely to bring broad relief, while identification of ancillary
genes that modify the phenotype may provide therapeutic insights and
targets.

Deep phenotyping as part of natural history studies can also uncover
potential [biomarkers](#biomarker) for use while [conducting clinical
trials](#conducting-clinical-trials).

[]{#process-creating-model-organisms}

## Process: Creating a model organism {#process:creatingamodelorganism}

Creating [model organisms](#model-organism) -- such as flies, mice,
worms and yeast -- can aid [interpretation of
variants](#variant-interpretation) during diagnosis, in understanding
the [mechanism of harm](#mechanism-of-harm), in screening for potential
drugs and in [validating compounds](#validating-compounds).

If a [model organism](#model-organism) recapitulates the phenotype of a
patient, then it is evidence that the modeled genotype is pathogenic.

Even if a model organism does not share the same phenotype as human
patients, it may still be useful for scientific investigations, so long
as it has an observable phenotype.

If a [model organism](#model-organism) responds to a therapy, then it
can aid in [validating predicted therapeutics](#validating-compounds).

The choice of [model organism](#model-organism) in disease research is
guided by the exhibition of a strong phenotype for the disorder and/or
its correspondence with the human phenotype.

After the construction of a model organism, a critical next step is to
characterize the phenotype of the model.

For example, zebrafish can exhibit seizures, and checking for these is
part of the phenotyping process.

Characterizing the phenotype of a model organism may be significantly
more labor than creating the initial organism itself, but it is a
critical step, since it is difficult to test therapeutics without a
robust phenotype.

Many academic laboratories and institutes such as [Jackson
Laboratories](http://www.jax.org/) can construct and phenotype model
organisms.

In the context of human disease, there are three categories of model
organisms commonly employed:

-   [knockout](#knockout) organisms in which a gene is removed;

-   [knock down](#knockdown) organisms in which a gene's expression is
    reduced; and

-   [knock-in](#knockin) organisms in which an allele is added or
    replaced.

[]{#process-identifying-precision-therapeutics}

## Process: Identifying precision therapeutics {#process:identifyingprecisiontherapeutics}

With a [mechanism of harm](#mechanism-of-harm) identified, it is
possible to consider the identification of therapeutics to target that
mechanism.

Broadly speaking, there are two approaches for identifying precision
therapeutics: [the rational
approach](#process-identifying-therapeutics-rationally) and [the
empirical approach](#process-identifying-therapeutics-empirically).

Both approaches may be pursued in parallel.

If resource constraints force them to be ordered, the rational approach
may work better for disorders in which the goal is to modulate a
specific molecular activity, while the empirical approach may work
better when the root mechanism of harm is an absence of activity or an
introduced toxicity.

The empirical approach also eliminates the need to conduct variant
impact analysis, so if resolving the specific impact of a variant is
going to be time-consuming or costly, then the empirical approach may be
a reasonable bypass.

[]{#process-identifying-therapeutics-rationally}

## Process: Identifying therapeutics rationally / The Rational Algorithm for Precision Therapeutics {#process:identifyingtherapeuticsrationallytherationalalgorithmforprecisiontherapeutics}

Rational identification of therapeutics involves [understanding the
functional impact of the mechanism of harm](#process-analyzing-impact),
and then identifying therapies that invert the impact.

These therapies include small molecules, but also more complex
gene-based strategies such as gene therapy, gene editing or antisense
oligonucleotides.

Before the rational approach can begin, it is critical to understand the
*impact* associated with the mechanism of harm.

In general, for each mechanism of harm, there are four possible impacts
on the associated biological process, and four corresponding rational
strategies to identify therapies:

-   Overactivity requiring inhibition: if a biological process has
    become overactive, then it must be inhibited. [Jump to activating or
    inhibiting a target](#process-inhibiting-or-activating-a-target).

-   Underactivity requiring activation: if a biological process has
    become underactive, then it must be activated. [Jump to activating
    or inhibiting a target](#process-inhibiting-or-activating-a-target).

-   Absence of activity requiring compensation: if a biological process
    has become absent, then there must be compensation for the absence
    -- up to and including replacement of the missing activity. [Jump to
    compensating for absence of
    function](#process-compensating-for-absence-of-function).

-   Toxic activity requiring elimination: if a biological process has
    introduced active toxicity, then it must be eliminated. [Jump to
    eliminating toxic activity](#process-eliminating-toxic-activity).

While the initial genotype may itself be a target or suggest targets, it
is also possible to [conduct
transcriptomics](#process-finding-therapies-with-transcriptomics) to
identify additional targets for input the rational approach.

It is also possible to consider rational strategies that target specific
aspects of the type of the gene involved, such as:

-   [targeting a
    genotype](#process-developing-genotype-directed-therapies);
-   targeting a receptor defect;
-   targeting gene regulatory defects;
-   targeting a structural protein defect;
-   targeting a non-coding RNA defect;
-   targeting a proteinopathy.

### Targeting a receptor defect {#targetingareceptordefect}

If a mechanism of harm impacts a [receptor](#receptor), then modulating
the activity of the receptor applies if the receptor is not gone, and
there are additional possibilities due to special properties of
receptors.

Receptors are more complex in their interactions than enzymes, because
they have a baseline level of activity -- [constitutive
activity](#constitutive-activity) -- even in the absence of the ligand
(agonist) which stimulates them.

With a partial loss of function, a next step is look for
[agonists](#agonists) of the receptor.

In the case of a gain of function, increasing
[antagonists](#antagonists) may help, but increasing [inverse
agonists](#inverse-agonists) may help as well.

Receptors can also be viewed as the starting points of the metabolic
pathways that they kick off, so it may be easier to target a metabolic
pathway behind the receptor than the receptor defect itself.

For any compound suggested by these strategies, the next step is
[compound validation](#validating-compounds).

### Targeting a kinase defect {#targetingakinasedefect}

Kinases phosphorylate other proteins, which may either activate or
inhibit them.

If the mechanism of harm involves altered activity in a kinase, then
looking into the downstream targets of the kinase (as the next links in
the mechanisms of harm) for modulation may be useful.

### Targeting gene regulatory defects {#targetinggeneregulatorydefects}

Apart from a genetic disorder's primary [mechanism of
harm](#mechanism-of-harm), disregulation of other genes can account for
harm in these disorders as well.

Most genes have a role to play in the [regulation of other
genes](#gene-regulation): increasing expression expression of one gene
may increase or decrease the expression of another gene.

As a result, altering the expression of the protein impacted by a
mutation can have downstream effects through [gene regulatory
networks](#gene-regulatory-network).

In addition, some genes -- such as those involved in chromatin
modification or histone/DNA methylation -- engage in regulation of other
genes as their primary function.

To target the primary effects of a mutation in a regulatory gene and the
downstream effects of other mutations,
[transcriptomics](#process-finding-therapies-with-transcriptomics) and
[proteomics](#proteomics-therapeutics) can reveal the extent to which
other genes have been disregulated, and can suggest therapeutic
strategies for restoring a baseline gene expression profile.

### Targeting a structural protein defect {#targetingastructuralproteindefect}

If a mechanism of harm disrupts a protein whose primary purpose is
structural (as in dystrophin), then it is challenging to replace the
structure.

The [Duchenne Muscular Dystrophy
community](http://www.parentprojectmd.org/) is an exemplar in developing
strategies for tackling the absence of a structural protein.

Given the pharmacological challenges in therapeutically delivering a
structural protein, strategies focusing on the mutation such as
[exon-skipping](#exon-skipping-therapeutics) and
[readthrough](#readthrough-therapeutics) are next steps, assuming the
mutations are in scope.

Though difficult, investments in basic science for
[gene-editing](#gene-therapeutics) may be advisable.

If it is suspected that the mutant protein would have some value, but
protein quality control mechanisms are too aggressively degrading the
protein, then a next step is to [search for
stabilizers](#finding-mutant-stabilizers) for the mutant protein.

### Targeting a non-coding RNA defect {#targetinganon-codingrnadefect}

If the primary cause of a disorder is an error (or a loss) of
[non-coding RNA](#non-coding-RNA) -- which is presumed to be rare
relative to disorders caused by defects in proteins -- then there are
two additional high-level strategies:

1.  delivering the missing non-coding RNA; and

2.  editing the defects in the non-coding region.

RNA is straightforward to synthesize, but targeted delivery and
retaining bioavailability is a significant challenge in the [application
of medicinal chemistry](#apply-medicinal-chemistry).

However, [targeted gene-editing](#gene-therapeutics) has additional
(likely more difficult) challenges.

### Targeting a proteinopathy {#targetingaproteinopathy}

If a mechanism of harm disturbs [protein folding](#protein-folding), in
some cases, the new foldings (or foldings to which they have become
susceptible), are actively malignant.

In many cases, cells can detect misfolded and/or mutant proteins through
quality control mechanisms, and degrade them.

In some diseases, improper protein folding causes toxic protein
aggregation.

For instance, amyloid misfolding features in diseases such as prion
disease, amyloidosis, Alzheimer's, Huntington and Parkinson's, as it
allows aggregation of misfolded proteins.

In disorders in which misfolding is driving malignant behavior, several
high-level strategies are in scope, including:

-   identifying compounds that can stabilize the misfolded protein;

-   creating monoclonal [antibodies](#antibodies) to target malignant
    proteins;

-   [activating chaperones that aid
    folding](#process-inhibiting-or-activating-a-target); and

-   [activating processes that degrade misfolded
    proteins](#process-inhibiting-or-activating-a-target).

Heat shock proteins aid protein folding and are often naturally
upregulated when a cell is stressed (although heat shock therapeutics
have been challenging to develop due to toxicity).

Autophagy is the process by which cells digest defective or excessive
components, and upregulation of this process may be beneficial in
proteinopathies.

If protein aggregration specifically is problematic, then an additional
strategy is to characterize sites on the protein that allow aggregates
to form and to identify inhibitors that can interfere with these sites,
with the aim of preventing aggregates from forming.

For any identified compound, the next step is [compound
validation](#validating-compounds).

### Targeting the phenotype {#targetingthephenotype}

It is possible to bypass the primary mechanisms and instead look for
therapeutics based on [biomarkers](observable) and/or
[phenotypes](#phenotype) in cells and/or model organisms.

-   At the level of a patient, phenotypic targeting is simply
    symptomatic treatment. For instance, if a symptom of the disorder is
    epilepsy, one can try known anticonvulsants.

-   If [investigational studies](#investigational-studies-mechanism)
    into the mechanism of harm have found a phenotype in model
    organisms, then a next step is [model-organism
    screening](#model-organism-screening).

[]{#process-inhibiting-or-activating-a-target}

## Process: Inhibiting or activating a target {#process:inhibitingoractivatingatarget}

In the course of identifying therapeutics, a specific gene may become a
target for inhibition or activation.

There are broadly two ways to lower the function of a gene by degree:
(1) reducing expression of the gene and (2) physically interfering with
the activity of the gene product via chemical inhibition.

For the first approach -- moduling gene expression -- [developing an
antisense oligonucleotide](#process-developing-aso) is a self-contained
approach that may be pursued in parallel.

Correspondingly, there are broadly two ways to raise the function of a
gene by degree: increasing expression of the gene and (2) physically
catalyzing or increasing the activity of the gene product via chemical
activation.

If the gene in question is an enzyme, increasing the concentration of
the precursors to the catalyzed reaction may make more efficient use of
the existing enzyme.

As a warning, if the gene remains fully functional even with low levels
of the protein present, then reducing gene expression may not be a
practical strategy for inhibition. This is common for enzymes, where
even small amounts of protein can be sufficient for "normal" function.

Computational approaches may help chemical identify strategies for
activation or inhibition including:

-   [Mining biomedical knowledge](#process-mining-biomedical-knowledge)
-   [Virtual drug screening](#process-virtual-screening)

Of course, [conducting chemical drug
screens](#process-screening-for-candidate-compounds) may also be in
scope for identifying inhibitors.

In some cases, it may not be possible to directly inhibit or activate a
specific target, but it may be possible to inhibite or activate a
*regulatory modulator* of that target.

For example, RHOBTB2 has no known direct inhibitors, but E2F1 regulates
RHOBTB2, and celecoxib can inhibit E2F1. Thus, celecoxib may be an
indirect inhibitor of RHOBTB2.

[]{#partial-loss-of-function-strategies}

### Specific strategies for reversing underactivity {#specificstrategiesforreversingunderactivity}

If there is diminished -- but not lost -- activity for a gene, then the
high-level strategy is to increase activity.

When there is residual activity, there are additional strategies to be
considered in addition to those for [total loss of
function](#total-loss-of-function-strategies):

-   If residual activity is insufficient for downstream processes, it
    may also be useful to consider to increasing the inputs to the
    activity; that is, increasing the number of substrates or agonists
    in an attempt to resolve the insufficiencies.

-   It may be possible to use a [splice-enhancing antisense
    oligonucleotide](https://stm.sciencemag.org/content/scitransmed/12/558/eaaz6100.full.pdf?ijkey=N5jj5tKEmu0oY&keytype=ref&siteid=scitransmed)
    to increase the expression of a wild-type allele -- to compensate
    for insufficient activity from a mutant allele.

Under either approach, the next step is to [validate any
candidates](#validating-compounds).

[]{#gain-of-function-strategies}

### Specific strategies for reversing overactivity {#specificstrategiesforreversingoveractivity}

If a disorder is caused by a gain of function in a gene or is aggravated
by activity in another gene, then a rational high-level strategy is to
suppress activity in that gene or in a relevant pathway.

If upstream or downstream elements in the affected pathways are known,
then applying the same gain of function strategies to each element in
the pathway may serve to counteract a gain of function upstream or
downstream.

If no inhibitor, blocker or antagonist is known, then [structure-based
drug development and virtual screening](#virtual-screening) are
potential next steps.

It is also possible to consider the design of knock-down antisense
oligonucleotides that lower the expression of the target gene.

Knock-down antisense oligonucleotides may target only the mutant allele,
or they can be designed to also lower wild-type gene expression as well.

For any compounds that turn up, the next step is [compound
validation](#validating-compounds).

[]{#process-mining-biomedical-knowledge}

## Process: Mining biomedical knowledge for activators and inhibitors {#process:miningbiomedicalknowledgeforactivatorsandinhibitors}

Natural language processing makes it possible to mine the entirety of
the published literature for references to a compound being an activator
or inhibitor of a specific target.

Many biomedical datasets have condensed drug-gene relationships to
identify potential or actual activation or inhibition, including:

-   [SemMedDB](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3509487/)
-   [Connectivity Map](https://www.broadinstitute.org/cmap/)
-   [Drug Gene Budger](https://maayanlab.cloud/DGB/)
-   [ChEMBL](https://www.ebi.ac.uk/chembl/)
-   [DrugBank](https://go.drugbank.com/)
-   [Guide to Pharmacology](http://www.guidetopharmacology.org/)

There are several tools capable of mining biomedical knowledge for such
hits as well, including
[mediKanren](http://minikanren.org/workshop/2020/minikanren-2020-paper10.pdf).
mediKanren is a free tool developed by my institue at UAB.

[]{#predicting-expression-therapeutics}

## Process: Predicting compounds to modify gene expression {#process:predictingcompoundstomodifygeneexpression}

To predict which compounds may be able to upregulate the expression of a
target gene, the [Connectivity
Map](https://www.broadinstitute.org/cmap/) -- or
[cMap](https://www.broadinstitute.org/cmap/) -- [LINCS
cloud](http://www.lincscloud.org/) databases contain the result of
experiments measuring the effect of a library of compounds on RNA
expression for many genes.

In some cases, the target gene may not be present in the databases, but
if the target gene is regulated by another gene in the database, then
one can attempt to indirectly regulate the target gene.

Any hits produced through this approach should proceed to [compound
validation](#validating-compounds).

[]{#total-loss-of-function-strategies}
[]{#process-compensating-for-absence-of-function}

## Process: Compensating for absence of function {#process:compensatingforabsenceoffunction}

A total loss of function in a [gene](#gene) most commonly happens in
[recessive](#recessive) disorders with two loss-of-function alleles or
in [X-linked](#x-linked) disorders with a single loss-of-function
allele.

The result is an absence of function in the gene -- or significantly
diminished activity.

There are three general strategies for correcting for the absence of
function:

1.  restoring the lost function;
2.  adapting to lost function; and
3.  empirically screening for or testing potential rescues.

Given the difficulty compensating for lost function with rational
approaches, [empirical approaches to identifying
therapies](#process-identifying-therapeutics-empirically) may have
higher yield.

### General approaches to restoring lost function {#generalapproachestorestoringlostfunction}

If one of the mutations involved is premature stop, then [identifying a
readthrough therapy](#readthrough-therapeutics) is a potential strategy.

If one of the mutations is in an exon not critical to the function of
the protein, then [exploring exon-skipping antisense oligonucleotide
therapeutics](#exon-skipping-therapeutics) is a next step.

If issues regarding delivery to the right tissues and any issues
surrounding gene-dose toxicity can be resolved, then developing a gene
therapy is hypothetically in scope as a next step.

If a missing protein could be delivered from another tissue, then
[exploring genetically-motivated
transplantation](#genetic-transplantation) is a possible next step.

If the missing protein is an enzyme, and if the missing enzyme could be
delivered to the correct part of the cell, then the next steps include
enzyme synthesis and development of [enzyme replacement
therapy](#enzyme-replacement-therapy).

### General approaches to adapting to lost function {#generalapproachestoadaptingtolostfunction}

In some cases, another gene or pathway may provide a degree of
redundancy with some function that has been lost.

Thus, a next step for disorders with a total loss of function is basic
scientific studies to look for compensatory genes or pathways.

If total loss of function is leading to insufficiency or absence or
excess of a particular metabolite (as in conditions where there is total
loss of an enzyme), then another next step is to [explore a metabolic
diet](#metabolic-diet).

Pathway databases such as [BioCyc](http://www.biocyc.org/) may help
identify additional targets for intervention with metabolic diets.

Even if an insufficient or absent metabolite cannot be obtained through
diet, then it could become a target for [drug development via medicinal
chemistry](#apply-medicinal-chemistry).

More generally, [using transcriptomics to identify
therapies](#process-finding-therapies-with-transcriptomics) may identify
downstream processes that have been disrupted by the missing gene, which
may in turn suggest additional strategies for identifying therapies.

### Screening for correctors {#screeningforcorrectors}

If there exists a disease model, then [empirical approaches to
identifying compounds that rescue the
model](#process-identifying-therapeutics-empirically) may be more
productive when attempt to account for lost function.

[]{#process-eliminating-toxic-activity}

## Process: Eliminating toxic activity {#process:eliminatingtoxicactivity}

If a specific molecular function must be ablated due to its toxicity,
then allele-specific knockdown antisense oligonucleotides or antibody
therapies are in scope.

Given the difficulty of eliminating the function of a specific allele,
[empirical approaches to identifying
therapies](#process-identifying-therapeutics-empirically) may be useful.

[]{#process-identifying-therapeutics-empirically}

## Process: Identifying therapeutics empirically / The Empirical Algorithm for Precision Therapeutics {#process:identifyingtherapeuticsempiricallytheempiricalalgorithmforprecisiontherapeutics}

With knowledge of the root molecular cause of a disease, it is possible
to construct [precision disease models](#precision-disease-model) and
then test or screen drugs against them.

This empirical approach has the following steps:

1.  Create a [precision disease model](#precision-disease-model) that
    represents a patient's disease.

2.  Phenotype the precision disease model.

3.  [Screen potential
    therapies](#process-screening-for-candidate-compounds) against the
    disease model.

4.  If no potential therapies are identified, then [run experiments to
    identify drug *targets*](#investigational-studies-modifier), and
    then feed these drug targets back into the high-level Algorithm for
    Precision Medicine to find potential therapies.

5.  [Adapt potential therapies identified via the model to human beings
    with medicinal chemistry](#applying-medicinal-chemistry).

[]{#discovering-assays}

## Process: Identifying assays {#process:identifyingassays}

For each [mechanism of harm](#mechanism-of-harm), investigational
studies should aim to discover laboratory assays that can observe the
hypothesized or confirmed mechanism.

An assay is, effectively, a standardized laboratory experiment with a
well-defined readout for its result.

The purpose of an assay is to measure a specific feature of a biological
system.

For example:

-   Protein-expression assays measure the amount of a particular protein
    present in a sample (usually with an [antibody](#antibody)).

-   Enzymatic activity assays measure the level of activity or function
    present for a particular enzyme.

-   Electrophysiological assays measure electrical properties of cells.
    (Genetic epilepsies may benefit from this broad category of assay.)

Having a suite of assays that can probe different links of the mechanism
of harm are critical for validating compounds predicted to have
therapeutic benefit.

For example, a good assay might fluoresce in the presence of a compound
that corrects some aspect of the mechanism of harm.

Assays are helpful for [validating proposed
compounds](#validating-compounds).

Precise assays are also a prerequisite for [conducting high-throughput
screening](#process-conducting-high-throughput-screening).

There are roughly three kinds of assays, in order of increasing
complexity:

-   cell-free assays isolate the key components of a cellular or
    chemical process;

-   cell-based assays operate on patient cells or on cells that model
    the disease; and

-   model-organism-based assays observe the phenotype of a model
    organism.

Lower-complexity assays tend to be more economical for [conducting
high-throughput
screening](#process-conducting-high-throughput-screening) techniques,
while higher-complexity techniques tend to produce stronger candidates.
(For instance, if a compound works on a model organism, at least some
aspect of the delivery challenge in medicinal chemistry has been
solved.)

### A word of caution on assay development {#awordofcautiononassaydevelopment}

Designing scientific experiments to measure a feature of interest is a
fundamentally creative process, so assay discovery is subject to the
same constraints that govern scientific progress itself.

Designing an assay will require [finding an
expert](#identifying-an-expert) in the relevant biology.

While it is hard to systematize or automate the process of assay
discovery, [Recursion Pharmaceuticals](http://www.recursionpharma.com/)
has computer vision algorithms that attempt to discover cell-based
assays when there are morphological changes to the cell as the result of
a disorder.

[]{#identifying-biomarkers}

## Process: Identifying biomarkers {#process:identifyingbiomarkers}

Basic research into the mechanism of harm should also be aimed at
identifying

Biomarkers help measure the effectiveness of therapeutic approaches
directly or indirectly, and are essential when [conducting clinical
trials](#conducting-clinical-trials).

[Conducting natural history
studies](#process-conducting-natural-history-studies) may be very
helpful in identifying biomarkers.

[]{#creating-cell-lines}

## Process: Establishing cell lines {#process:establishingcelllines}

For basic [investigational studies](#investigational-studies-mechanism)
into the cell biology of a disorder, there are two broad categories of
cell lines:

-   Patient-derived cell lines such as fibroblasts, lymphoblasts and
    iPSC use donated patient tissue, such as blood, skin, muscle or
    liver.

-   Constructed cell lines introduce a patient's genotype into an
    existing cell line to mimic the condition in that cell line.

For each disorder, it is important to create the cell lines with the
strongest phenotype relative to the high-level phenotype of the
patients. The strongest phenotypes are most useful for validation and
screening.

For instance, if a disorder has strong liver involvement, then
hepatocytes may provide a strong cellular representation of the
disorder, while if it is neurological in nature, then neurons may
provide a strong representation.

As cell lines become established, it is important to conduct
[investigational studies](#investigational-studies-mechanism) that
establish phenotypes for the different cell types.

### Patient-derived cell lines {#patient-derivedcelllines}

The type of cell lines necessary for studying a disorder vary with the
disorder, but fibroblasts and lymphoblastoid lines are relatively
common, if only for their durability.

Stem cell lines (usually induced pluripotent stem cells (iPSC) made from
patients) can also be useful in studying a disorder, because they are
differentiable into other cell types, such as brain cells or liver
cells.

Stem cell lines cost around USD 5,000 to USD 10,000 to create in an
academic laboratory, but can take months to create, so it is advisable
to start the process early. Differentiation into other cell types can
take longer still.

It is also advisable to use as many patients as possible, since some
patients will inevitably provide more robust cell lines than others.

### Constructed cell lines {#constructedcelllines}

Since some genetic conditions make culturing patient-derived cells
challenging, so an alternative approach is to introduce a patient's
pathogenic mutations directly into an existing cell line.

For instance, cancer cell lines are sometimes used for their robust
growth properties, although cancer cell lines can alter the phenotype of
the cells.

An advantage of using existing cell lines is that, in addition to
growing well, they can be created relatively quickly and cheaply for
almost any tissue type.

The chief disadvantage is that their fidelity to the actual condition
and real patients may not be clear.

[]{#creating-biobanks}

## Process: Establishing biobanks and reagent repositories {#process:establishingbiobanksandreagentrepositories}

As a patient community grows, establishing biobanks with cell lines and
repositories of reagents can accelerate research and make it easier to
compare and reproduce results between research labs.

A set of reagents that will likely prove useful are antibodies to any
proteins of interest. (Antibodies can be used in a lab to detect the
presence of a particular protein.)

Patient communities will likely want to partner with an existing medical
research institute such as a university, the NIH or a non-profit such as
[Sanford-Burnham-Prebys](http://www.sbpdiscovery.org/) or
[Coriell](https://www.coriell.org/) for biobanking of cell lines and
tissues.

Because patient tissue is extremely valuable, communities should also
consider creating a procedure for donating the bodies of deceased
patients to aid in investigation of the disorder, should patients or
parents choose to do so.

[]{#investigational-studies-modifier}

## Process: Finding modifier genes and drug targets {#process:findingmodifiergenesanddrugtargets}

In addition to [identifying mechanisms of
harm](#investigational-studies-mechanism), pre-translational scientific
investigations can also aim to identify genes that modify the
[phenotype](#phenotype) of a condition.

Some of these related genes may in turn become drug targets.

**This is an important insight: the gene that caused the disorder may
not be the gene that is targeted to correct the disorder.**

For instance, in a loss of function disorder, there may be another gene
that can compensate for the role of the lost activity.

If an [assay that measures the activity of the deficient gene is
available](#discovering-assays), then it is possible to conduct a
[genetic screen for alternate pathways](#genetic-screen).

If a compensatory gene is discovered, then the next step is to target it
for [activation](#process-inhibiting-or-activating-a-target).

In some cases, disabling or decreasing expression of a second gene may
actually suppress the [phenotype](#phenotype) of the disorder.
Suppressor genes offer additional therapeutic targets for inhibition. A
[genetic screen](#genetic-screen) can identify suppressor genes as well.

For general interactions between genes, the [STRING
database](http://string-db.org/) and
[Genemania](http://www.genemania.org/) provide information on known
relationships.

For determining which genes co-evolve together -- which yields clues to
function -- one can use [ERC
analysis](http://csb.pitt.edu/erc_analysis/).

In addition to genetic screens, another broad-spectrum approach to
identifying targets (and sometimes therapies) is to [conduct
transcriptome-oriented
experiments](#process-finding-therapies-with-transcriptomics) that
reveal genes that have been highly disregulated.

Genes that have been significantly upregulated could be targets for
inhibition, while those that are significantly downregulated could be
targets for activation.

[]{#process-developing-genotype-directed-therapies}

## Process: Developing genotype-directed therapies {#process:developinggenotype-directedtherapies}

Genotypically-guided therapies focus on correcting the genetic defect
itself, rather than the functional impact of the genetic defect, and
include:

-   gene therapies;
-   gene editing;
-   readthrough therapies;
-   antisense oligonucleotide therapies; and
-   RNA therapies.

Gene therapy typically uses a repurposed and modified virus (such as
AAV9) to "infect" the host with a new gene that has been placed in side
of it.

Gene editing delivers gene-editing material and programming, such as the
Cas9 protein suitable RNA guides, to edit the mutant gene directly back
to wild-type.

Both gene therapy and gene editing suffer from significant challenges.

Correcting every single cell in the body is a substantial
pharmacological challenge -- since it requires reaching every cell. So,
typically, some meaningful subset of all cells must be hit -- such as a
specific organ or tissue, and even this remains a major challenge.

In the case of gene editing, the error rate in the edits has to be low
enough that it doesn't cause serious harm in the process.

The costs and timelines for [pursing gene therapy or gene
editing](#gene-therapeutics) is currently much longer than what many
patients may reasonably consider.

If the disorder is caused by a [premature stop
mutation](#premature-stop), then [identifying readthrough therapeutics
may be in scope](#readthrough-therapeutics). Readthrough therapies use
small molecules to skip over the errant stop mutation.

For genetic targets that have been resolved to overactive, underactive,
absent or toxic, there is almost always an [antisense oligonucleotide
that could be crafted](#process-developing-aso) to mitigate or eliminate
the impact by altering the splicing and translation of the target gene.

[]{#gene-therapeutics}

## Process: Pursuing gene-editing and gene therapy {#process:pursuinggene-editingandgenetherapy}

Gene editing and gene therapy is a theoretical silver bullet for all
genetic disorders, and with enough investment in basic scientific
research, it will almost certainly one day become reality.

Conceptually, gene editing involves editing out defects in an organism's
genome by inserting, replacing or deleting elements in an organism's
genetic code.

Practically, there are three major high-level challenges with most
approaches:

1.  Delivering the gene-editing agents to every cell (or every cell of
    interest).

2.  Ensuring that the editing error rate is low enough to avoid
    introducing additional mutations (and likely cancer in the process).

3.  Managing the immune response to delivery vectors.

For delivering gene-editing agents, engineered viruses are the most
popular platform.

New genetic material (such as a functioning gene version of a gene) can
be delivered directly as a separate fragment of DNA called a plasmid.

Alternatively, genetic material can be integrated into the host genome
via techniques like Zinc fingers, TALENs, CRISPR/Cas9 or meganucleases.

[]{#readthrough-therapeutics}

## Process: Identifying readthrough therapeutics {#process:identifyingreadthroughtherapeutics}

If a disorder is caused by a [premature stop mutation](#premature-stop),
then readthrough therapeutics are in scope.

Read-through compounds attempt to override premature stop
[codons](#codon), ultimately converting them to an [amino
acid](#amino-acid) in the process of [protein
synthesis](#protein-synthesis).

([Keeling, *et al*.,
2014](http://www.annualreviews.org/doi/abs/10.1146/annurev-genom-091212-153527))
provide an overview of the readthrough therapeutics space.

When the mutation of interest is a premature stop, then testing
readthrough compounds on cell cultures is a reasonable next step, and
the following compounds may be useful in those tests:

-   [G418](https://en.wikipedia.org/wiki/G418) is a potent readthrough
    compound useful in a laboratory setting as a measure of the
    potential of this approach, since it is a potent readthrough
    inducer, although it is too toxic to be used therapeutically.

-   [Gentamicin](https://en.wikipedia.org/wiki/Gentamicin) (which has
    problematic side effects) is also known to induce readthrough in
    some cases.

-   [Ataluren](https://en.wikipedia.org/wiki/Ataluren), which is
    purported to induce readthrough, is available in Europe.

[]{#process-developing-aso}

## Process: Developing antisense oligonucleotide therapeutics {#process:developingantisenseoligonucleotidetherapeutics}

Antisense oligonucleotides (ASOs) represent a promising path forward for
many rare genetic disorders because they are so versatile.

ASOs can:

-   upregulate gene activity by increasing gene expression with
    splice-enhancement;

-   downregulate gene activity by decreasing gene expression with
    gene-based knockdown;

-   reduce expression of a specific allele with allele-specific
    knockdown; or

-   produce an alternate version of a gene transcript with a problematic
    exon skipped.

If an antisense compound is identified or constructed, the next step is
[compound validation](#validating-compounds) and to focus largely on
toxicity studies if the expectation is to file for single patient
compassionate use.

[]{#exon-skipping-therapeutics}

### Creating exon-skipping antisense oligonucleotides {#creatingexon-skippingantisenseoligonucleotides}

If a damaging mutation occurs in an [exon](#exon) that is non-critical
to the resulting protein, then exon-skipping may be a viable therapeutic
approach.

Databases such as the [Ensembl genome browser](http://www.ensembl.org/)
can provide the exons and introns for a gene.

In addition, Ensembl will also provide alternate transcripts that have
been identified. If an alternate transcript exists that skips the exon
containing the mutation, this is a positive (though not essential)
indication that exon-skipping is a viable therapeutic approach.

To skip over a mutation-bearing exon, an [antisense
oligonucleotide](#antisense-oligonucleotide) is created that can induce
RNA splicing to skip that exon during construction of mRNA.

In theory, an antisense oligonucleotide sequence could be customized for
any disorder in which it is reasonable to skip an exon.

Exon-skipping was a theoretical possibility when I first started writing
this article in 2015, but it became an FDA-approved and even
single-patient modality not long thereafter.

### Upregulating gene expression with antisense oligonucleotides {#upregulatinggeneexpressionwithantisenseoligonucleotides}

If the activity of a gene needs to be enhanced and there is at least one
functional copy of the gene present, then splice-enhancing ASOs that
skip introns, thereby increasing the efficiency of conversion from
pre-mRNA to mRNA are in scope.

### Downregulating gene or allele expression with antisense oligonucleotides {#downregulatinggeneoralleleexpressionwithantisenseoligonucleotides}

If the activity of a gene needs to decreased, then knockdown ASOs --
which may be specific to a single allele or the entire gene -- can be
developed.

If a single mutant allele has introduced toxicity, then an
allele-specific ASO is a reasonable strategy to consider for eliminating
that toxicity.

When designing an allele-specific knockdown ASO, it is worth exploring
whether alternate sites on the mutant allele also differentiate it from
the wild-type allele -- and hence serve as better targets.

It is not alwasy the case that the best region to target is the mutation
itself, but there may be other sequences along the mutant allele that
are more amenable.

It will be necessary to do phased sequencing (such as long-read
sequencing) between the two alleles to know the full sequence of both
alleles confidently.

[]{#process-screening-for-candidate-compounds}

## Process: Chemically screening for candidate compounds {#process:chemicallyscreeningforcandidatecompounds}

Regardless of the underlying cause, much of modern drug development
rests on testing many molecules for an effect on the mechanism of harm
or a target believed to be beneficial for the disorder.

As a result, it is difficult to engage in screening without first being
able to recognize when something has had an effect.

Conducting [investigational studies into the mechanism of
harm](#investigational-studies-mechanism) will help find assays to
reveal such effects.

Once an [assay for measuring a mechanism of harm or the activity of a
target has been discovered](#discovering-assays), the next step is to
[conduct high-throughput
screening](#process-conducting-high-throughput-screening).

If an assay can't be established at a cellular or cell-free level, then
in some cases, a strong phenotype in a model organism can be used as the
basis for a screen.

Given the complexity and cost of model organisms, however, the number of
molecules that can be tested feasibly may be low.

In addition to manual screening, [virtual screening](#virtual-screening)
may be able to make therapeutic predictions without resorting to
laboratory work.

In lieu of testing large numbers of molecules blindly from compound
libraries, running a virtual screen first may reduce the number of drugs
to test. Of course, virtual screens can miss molecules that work in
practice, so while cost and time may go down, the probability of finding
a working candidate molecule drops as well.

With a scalable model, it is possible to [conduct high-throughput
screens](#process-conducting-high-throughput-screening).

If screening yields any hits, the next step is [compound
validation](#validating-compounds) and then optimizing medicinal
chemistry.

[]{#process-conducting-high-throughput-screening}

## Process: Conducting high-throughput drug screening {#process:conductinghigh-throughputdrugscreening}

High-throughput screening attempts to test large numbers of drug
candidate compounds for an effect -- often using robotics to automate
the process.

A "large number" could be all approved drugs (numbering about 1,500) or
it could be millions of drug-like molecules.

For drug repurposing, the [Prestwick Chemical
Library](http://v1.prestwickchemical.com/libraries-screening-lib-pcl.html)
includes 1,520 off-patent but approved drugs.

For more comprehensive repurposing, the larger [Microsource Spectrum
Collection](http://www.msdiscovery.com/spectrum.html) includes 2,560
compounds, some of which are approved, some of which are natural
products and some of which are tool compounds meant to help identify
targets for more in-depth drug discovery.

Both of these libraries are good choices for [drug
repurposing](#drug-repurposing).

High-throughput screening requires the selection of a compound library
and the [discovery of a high-precision assay](#discovering-assays) that
can recognize when a mechanism of harm has been mitigated.

Assays should be engineered to have a high signal-to-noise ratio to rule
out excessive false positives in large screens.

For each compound that gets a hit, the next step is [to validate the
compound](#validating-compounds) and the next step after that is to
optimize the medicinal chemistry of the compound to achieve the right
trade-off betwen efficacy, toxicity and delivery.

[]{#crowd-screening}

## Process: Crowd-sourcing and crowd-screening {#process:crowd-sourcingandcrowd-screening}

In some cases, conducting precision medicine means conducting science.

Science is a process that depends on collaboration and creativity, so
tapping the collective creativity and wisdom of the Internet can
accelerate the process.

For example:

-   *Crowd-sourcing* variant interpretation allows experts on relevant
    genes to provide their insight on pathogenicity, and it opens up the
    possibility of finding a matching case.

-   *Crowd-screening* suggestions through social media for potential
    therapeutics allows experts to contribute rationally predicted
    therapeutics (in contrast to blind high-throughput screening
    approaches).

[Mark2Cure](http://www.mark2cure.org/) is a crowd-screening platform
from the [Su Lab](http://sulab.org/) at Scripps that enables
large-scale, crowd-sourced biocuration of the medical research
literature related to a disease.

Biocuration enables bioinformatics techniques to mine the newly
structured data for relationships between diseases, potential drugs and
genes.

Of course, soliciting advice from social media requires filtering out
advice without a plausible scientific basis, but it can be a powerful
mechanism for generating leads.

[]{#metabolic-diet}

## Process: Designing a metabolic diet {#process:designingametabolicdiet}

In the case of a lost [metabolic pathway](#pathway), in which inputs no
longer convert to outputs, two mechanism of harm should be expected:

1.  accumulation of inputs; and
2.  a deficiency in the outputs.

If there is no alternate pathway to metabolize the input, then (1)
should be examined and if no alternate pathway to synthesize the output
exists, then (2) should be examined.

For example, in the disorder PKU, total loss of function in
phenylalanine hydroxylase leads to an inability to convert the amino
acid phenylalanine into tyrosine.

This suggests two strategies:

-   Limiting consumption of phenylalanine.

-   Increasing consumption of tyrosine.

In fact, strictly limiting consumption of phenylalanine in the diet is
an effective treatment for the disorder, and tyrosine supplementation is
beneficial as well.

As another example, patients with CDG Ib -- a total loss of function in
the gene *MPI* -- lack an enzyme to interconvert mannose-6-phosphate and
fructose-6-phoshpate. Because this enzyme is the sole provider of
mannose-6-phoshpate, the loss of the enzyme results in a deficiency of
mannose-6-phosphate, a critical precursor to a process called
glycosylation.

Adding mannose supplementation to the diet is an effective treatment for
the disorder.

A more common metabolic diet is the restriction of lactose-bearing dairy
products in individuals with lactose intolerance, a result of
insufficient or absent quantities of the enzyme lactase, which breaks
down lactose into galactose and glucose for further digestion.

[]{#finding-mutant-stabilizers}

## Process: Finding stabilizers for mutant proteins {#process:findingstabilizersformutantproteins}

In the event that the mutant protein is predicted to have residual
function, but quality control mechanisms within the cell (such as
endoplasmic-reticulum associated degradation) are degrading the protein,
the goal of stabilization is to find a molecule that interacts with the
mutant protein to prevent degradation.

In general, finding stabilizers may require [virtual screening and
structure-based drug design](#process-virtual-screening).

In the specific case where mutant enzymes may retain activity if they
could properly fold, but poor ability to fold leads to degradation of
the mutant proteins, there is work showing that potent *inhibitors* of
the mutant enzymes at low concentrations may be able to induce proper
folding ([Fan,
2003](http://www.cell.com/trends/pharmacological-sciences/abstract/S0165-6147%2803%2900158-5)),
thereby preventing their destruction and rescuing activity.

[]{#enzyme-replacement-therapy}

## Process: Developing enzyme replacement therapy {#process:developingenzymereplacementtherapy}

In disorders lacking an [enzyme](#enzyme), enzyme replacement therapy,
which replaces the missing enzyme, may be able provide therapeutic
relief.

There are substantial drug delivery challenges in enzyme replacement
therapy, but these vary in difficulty depending on the tissues and
intracellular compartments that need to be targeted.

The first step toward enzyme replacement therapy is being able to
synthesize the enzyme in a biologically active form.

Therapeutic enzyme synthesis generally uses the transfection of Chinese
Hamster Ovary (CHO) cells with DNA containing the gene that encodes the
desired enzyme.

In properly tuned bioreactors, transfected CHO cells can generate large
quantities of the target enzyme with [post-translational
modifications](#post-translational-modification) compatible with
mammals.

Once the enzyme is synthesizable and [validated](#validating-compounds),
[applying medicinal chemistry](#applying-medicinal-chemistry) will
likely be required to ensure that the [enzyme](#enzyme) is delivered to
the correct tissues and/or intracellular compartments.

[]{#genetic-transplantation}

## Process: Evaluating genetically-motivated transplantation {#process:evaluatinggenetically-motivatedtransplantation}

In some cases, transplanting organs, tissue or cells that do not contain
the underlying genetic defect can be therapeutic.

In particular, if a disorder results from a missing [gene
product](#gene-product) and that gene product can be delivered from
another tissue to other cells in the body, then organ and bone-marrow
stem cell transplantation are in scope.

In a bone marrow transplant, the patient's bone marrow is depleted and
then a transfusion of donor stem cells is provided to regrow the bone
marrow.

Moreover, because the donor stem cells don't carry the mutation, as they
differentiate in organs and tissues in the body, they will produce cells
not affected by the disorder.

In theory, gene editing could be used on induced pluripotent stem cell
lines for an autologous bone marrow transplant, although more basic
research into accurate gene editing is required before this could be
considered a realistic possibility.

[]{#stem-cell-therapeutics}

## Process: Exploring stem cell therapeutics {#process:exploringstemcelltherapeutics}

Stem cells have attracted attention for their regenerative therapeutic
potential, and there are certainly disorders and injuries which stand to
benefit from them.

Unfortunately, the scope for stem cells in treating [genetic
disorders](#genetic-disorder) is more limited.

In disorders for which [genetically-motivated
transplantation](#genetic-transplantation) is in scope, it is
conceivable that stem cell lines could be genetically modified to remove
a mutation, and then transfused back into a patient.

Two further obstacles make autologous stem cell therapeutics challenging
for genetic disorders for the near future:

-   transplantation with stem cells increases cancer risk; and

-   error rates in gene-editing further increase cancer risk.

Despite more limited prospects for treatment, stem cell lines are
valuable in investigational studies because they can differentiate into
different cell types, sparing the need to extract those tissues from
patients.

[]{#process-finding-therapies-with-transcriptomics}

## Process: Finding therapies and targets with transcriptomics {#process:findingtherapiesandtargetswithtranscriptomics}

In the context of human disease, transcriptomics (or RNA sequencing) has
the potential to identify genes disregulated as the consequence of the
disease.

Transcriptomics also has the potential to bring a diagnosis when genome
or exome sequencing fails, because RNA sequencing can pick up unusual
splice errors or transcript variants that could be hard to find with
static sequencing techniques alone.

If substantial disregulation is identified, then databases like
[cMap](https://www.broadinstitute.org/cmap/) and [LINCS
cloud](http://www.lincscloud.org/) can be used to compute a
perturbagenic cocktail of compounds designed to bring gene regulation
closer to baseline.

Care must be taken in interpreting results, as some disregulation could
be a compensatory response to the defect. Some apparent "disregulation"
could simply be background variation in the individual.

Transcriptomics requires conducting RNA sequencing on as many patients
and close relatives as possible in order to increase statistical
confidence and separate core disregulation from transcriptional
artifacts.

Restoring baseline expression where disregulation was compensatory could
be anti-therapeutic.

An advantage of a transcriptomics-driven approach to disease
therapeutics is that it holds the potential of addressing a broad class
of downstream mechanisms simultaneously, and it could be utilized even
in the absence of a firm diagnosis, because RNA sequencing can capture a
snapshot of the mechanism of harm as it passes through the
transcriptome.

The disadvantage of a transcriptomics-driven approach is that it does
*not* target the primary mechanism of harm.

While transcriptomics could be used on the level of an individual
patient given sufficient samples, it is certainly more effective with
RNA sequencing data available from the larger population, since this
should allow it to identify core disregulation in a disorder.

RNA sequencing is not generally available in a clinical context, so this
approach require partnering with an academic partner.

[]{#proteomics-therapeutics}

## Process: Finding therapies with proteomics {#process:findingtherapieswithproteomics}

Proteomics measures the protein types and quantities present in an
organism across specific tissues, environments and times.

For human disease, proteomics can identify proteins disregulated as a
consequence of the disease.

[SomaLogic](http://www.somalogic.com/) has a platform for blood-based
proteomics that has the potential to identify biomarkers in human
disease, even down to a personalized level ([Hathout, *et al*.,
2015](http://www.pnas.org/content/112/23/7153)).

As with transcriptomics, disregulated proteins found in proteomics may
also suggest regulatory strategies for therapeutics, with the caveat
that some proteins may be disregulated as a compensatory response.

[]{#process-virtual-screening}

## Process: Screening for drugs based on target structure {#process:screeningfordrugsbasedontargetstructure}

Structure-based drug design and virtual screening are computational
methods for designing and searching for drug candidates (which are
generally inhibitors) based on the structure of the target.

In structure-based drug design, the objective is to design a small
molecule that is roughly opposite in structure and charge to a target
domain on an enzyme.

Before one can conduct structure-based screens, it is necessary to
[analyze the structure of the
target](#process-analyzing-protein-structure).

Virtual screening scans compound libraries for potential ability to bind
with and inhibit target domains on proteins.

Because of the approximative nature of computational methods, predicted
candidates from these methods should proceed to [compound
validation](#validating-compounds).

High-fidelity virtual screening would often require intractable
simulations with molecular dynamics, so docking simulations may be used
in lieu of full physical simulation.

There is software available for conducting these simulations:

-   [PyRx](http://pyrx.sourceforge.net/) can screen a protein against
    possible inhibitors.
-   [ZINC](http://zinc.docking.org/) is a database of structures for
    commercially available compounds.
-   [FAF-Drugs3](http://fafdrugs3.mti.univ-paris-diderot.fr/) is a
    filtering package to predict pharmacokinetics.

For conducting follow-up simulations on hits with full molecular
dynamics, both [NAMD](http://www.ks.uiuc.edu/Research/namd/) and
[GROMACS](http://www.gromacs.org/) can be used.

[]{#model-organism-screening}

## Process: Conducting model organism drug screening {#process:conductingmodelorganismdrugscreening}

Once a [model organism has been created](#model-organism-creation) for a
disorder *and* its phenotype has been robustly characterized, then the
organism may be used as a platform for screening potentially therapeutic
compounds.

For some model organisms, it is possible to employ automation to conduct
phenotyping, which may enable large amounts of compounds to be tested.

[]{#genetic-screen}

## Process: Conducting genetic screens {#process:conductinggeneticscreens}

A compound-based screen on a [precision disease
model](#precision-disease-model) can identify genes impact the
phenotype, but a suppressor screen can identify *genes* that modify the
phenotype, and these genes may be useful as the basis for investigating
therapeutics.

In a suppressor screen, mutagenic agents are introduced into a large
population of model organisms.

If any of the resulting double mutant organisms show *improvement* in
their phenotype, then the mutant can be genetically analyzed to
determine which gene was modified.

-   If knocking down a second gene suppresses the phenotype in a screen,
    then the next step is to [look for inhibitors of the second
    gene](#process-inhibiting-or-activating-a-target).

-   If increasing the activity of a second gene suppresses the phenotype
    in a screen, then a next step is to [explore activating this second
    gene](#process-inhibiting-or-activating-a-target).

[]{#validating-compounds}

## Process: Validating a candidate compound {#process:validatingacandidatecompound}

If a screen produces a hit or a compound is hypothesized to be
therapeutic, the critical next step is to validate the efficacy of the
compound in a model system.

Initial validation involves using the [appropriate
assays](#discovering-assays) discovered while [investigating the
mechanism of harm](#investigational-studies-mechanism) to determine
whether that compound mitigates a particular mechanism.

For example, if a read-through compound is predicted to increase the
expression of the wild-type protein, an [antibody](#antibody) for the
protein should be able to detect its presence.

If validation with cells succeeds or validation with cells is not
possible, the next step is validation against the phenotype of [model
organisms](#model-organism).

If cell-based and organism-based validation succeed, the next step is to
[apply medicinal chemistry](#apply-medicinal-chemistry) to the compound
to convert it to clinical material suitable for clinical trials in
humans.

[]{#apply-medicinal-chemistry}

## Process: Applying medicinal chemistry to drug candidates {#process:applyingmedicinalchemistrytodrugcandidates}

When compounds are first identified either through screening or rational
predictions, it most likely not the case that these compounds will have
regulatory approval, or even that these compounds will be non-toxic and
effective in patients.

As strategies for identifying and developing molecular therapeutics
begin to yield these candidates, for any candidates without regulatory
approval, medicinal chemistry will be required to transform these
compounds into a form suitable for [conducting a clinical
trial](#conducting-clinical-trials).

As a broader discipline, medicinal chemistry aims to manipulate the
efficacy, toxicity and delivery of a compound.

In other words, medicinal chemistry is a multidisciplinary engineering
process that begins with a molecule that demonstrates efficacy on an
assay in cells and ends with a derivative of that molecule that is
*intended* to be safe and effective.

In general, medicinal chemistry challenges have to be re-solved for each
molecule, although some platforms, such as exosomal encapsulation (see a
review in ([Batrakova and Kim,
2015](http://www.sciencedirect.com/science/article/pii/S0168365915300420)),
provide the possibility of aiding delivery for a larger class of
molecules.

[]{#crossing-blood-brain-barrier}

### Crossing the blood-brain barrier {#crossingtheblood-brainbarrier}

While there are many challenges in medicinal chemistry, one often stands
out, especially in diseases impacting the brain: crossing the
blood-brain barrier.

The selective permeability of the endothelial cells in the brain prevent
many molecules from crossing, which makes drug delivery to the brain a
major challenge.

[]{#enzyme-replacement-challenges}

### Enzyme replacement challenges {#enzymereplacementchallenges}

Enzyme replacement therapy (and large molecule therapy in general) also
requires special considerations, both for its increased challenges in
crossing the blood-brain barrier and also for the need to control
targeting to specific tissues or intracellular compartments.

Enzyme replacement may also require targeting a specific organ, tissue
or intracellular compartment.

Within a cell, targeting the lysosome with a synthetic enzyme is perhaps
among the easiest, because the natural process of phagocytosis naturally
tends to direct large molecules to the lysosome.

For delivery to the cytoplasm of the cell, attaching cell-penetrating
peptides (such as the TAT peptide) to an enzyme can improve cell
penetrance.

PEGylation of the enzyme may also be beneficial in reducing the
immunogenicity of the protein (reducing side effects) and in reducing
renal clearance (improving availability and increasing half-life).

[]{#conducting-clinical-trials}

## Process: Conducting clinical trials {#process:conductingclinicaltrials}

Clinical trials attempt to determine the safety and efficacy of a
therapeutic, and they are required by regulatory agencies in most
countries before a compound may be marketed.

Clinical trials typically have four phases:

-   Phase 0: First-in-human. Pharmacodynamics and pharmacokinetics
    study. About a dozen volunteers.

-   Phase 1: Safety testing. Dose range determination. Side effect
    observation. A few dozen volunteers.

-   Phase 2: Effectiveness testing. A few hundred patient volunteers.

-   Phase 3: Large-scale safety and effectiveness testing. A few
    thousand patient volunteers.

Clinical trials are often placebo-controlled and double-blinded, so that
some participants are receiving a therapeutic and others are receiving a
placebo.

[]{#single-patient-trial}

## Process: Conducting a single-patient (*n*=1) clinical trial {#process:conductingasingle-patient_n_1clinicaltrial}

Perhaps one of the greatest epistemological and regulatory challenges
for precision medicine is that there may be so few patients that a
placebo-controlled trial is unlikely to yield the statistical confidence
necessary to validate the approach.

At the moment, there is no regulatory framework in place for
single-patient trials, although [proposals for "n=1"
trials](http://www.nature.com/news/personalized-medicine-time-for-one-person-trials-1.17411)
are circulating in the academic community.

In the U.S., if a patient wishes to take a compound that does not have
FDA approval, the manufacturer must agree to provide it, and the patient
must petition the FDA for permission through [expanded
access](http://www.fda.gov/ForPatients/Other/ExpandedAccess/ucm20041768.htm).

[]{#qa}

## Part II: Questions and answers {#partii:questionsandanswers}

This is part two of the guide.

It began as a glossary, but has evolved into a question and answer
format.

I am striving to explain entries in more patient-friendly language and
in the context of human disease.

In fact, not all of the questions below refer to topics above; some are
there because they may appear in a diagnostic report.

You can read each entry as needed as a reference, but I have tried to
order the questions so that you can also read it top to bottom as a
tutorial on genetics and precision medicine.

It is by no means complete, and I expect to be updating this segment of
the guide regularly.

If you're already trained in a field of science or engineering, then,
once again, I recommend [Quickstart Molecular
Biology](https://www.amazon.com/Quickstart-Molecular-Biology-Introductory-Mathematicians/dp/1621820343?crid=1JGTQXK17TJOT&keywords=quickstart+molecular+biology&qid=1658339748&sprefix=quickstart+molecul%2Caps%2C78&sr=8-1&linkCode=ll1&tag=mmamzn06-20&linkId=f25ba58292bb573e6898fadca3b20a05&language=en_US&ref_=as_li_ss_tl):

[![](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1621820343&Format=_SL250_&ID=AsinImage&MarketPlace=US&ServiceVersion=20070822&WS=1&tag=mmamzn06-20&language=en_US){border="0"}](https://www.amazon.com/Quickstart-Molecular-Biology-Introductory-Mathematicians/dp/1621820343?crid=1JGTQXK17TJOT&keywords=quickstart+molecular+biology&qid=1658339748&sprefix=quickstart+molecul%2Caps%2C78&sr=8-1&linkCode=li3&tag=mmamzn06-20&linkId=304e695567cfcde849c64c26bebbf2e7&language=en_US&ref_=as_li_ss_il){target="_blank"}![](https://ir-na.amazon-adsystem.com/e/ir?t=mmamzn06-20&language=en_US&l=li3&o=1&a=1621820343){width="1"
height="1" border="0"
style="border:none !important; margin:0px !important;"}

It's a rapid introduction to the field, targeted at those that already
have a technical background (broadly speaking).

[]{#qa-start}

[]{#define-precision-medicine}

### What is precision medicine? {#whatisprecisionmedicine}

Defined in a [National Academies Report on Precision
Medicine](https://www.nap.edu/catalog/13284/toward-precision-medicine-building-a-knowledge-network-for-biomedical-research),
precision medicine is the use of data to tailor care to the individual
characteristics of a patient.

More specifically, precision medicine focuses on the use of data to
identify and address the cause(s) of disease in a patient as precisely
as possible.

The data used in precision medicine tends to be molecular (often
genomic) in nature, although all data is in scope, including the
electronic medical record, genomics, transcriptomics, metabolomics,
proteomics and every other "omics".

Precision medicine is also extending beyond traditional biomedical
sources of data to include wearable devices or personal electronics or
social media.

Precision medicine is not a field of medicine as in cardiology or
infectious diseases, but rather an approach applicable to any field of
medicine.

[]{#drug-repurposing}

### What is drug repurposing? {#whatisdrugrepurposing}

Drug repurposing is the identification of a new purpose for an existing
approved therapy.

Drug repurposing can be done for an entire disorder or for a single
patient.

In contrast to drug discovery and development, which seeks to identify
and obtain regulatory approval for a novel therapy, repurposing an
existing drug for a disease or even an individual patient bypasses many
regulatory hurdles and substantially lowers costs.

Physicans have discretion to prescribe approved drugs off-label for
other disorders.

In some cases, an approved drug will work in its available formulation
and at standard dosing.

[]{#phenotype}

### What is a phenotype? {#whatisaphenotype}

In the context of a patient, a phenotype usually refers to a collection
of symptoms.

More generally, phenotype refers to the observable or measurable
characteristics of an organism, whether in cells, model organisms or
human patients.

Everything observable -- from hair color to seizures to blood platelet
levels -- counts as part of the phenotype.

[]{#genome}

### What is a genome? {#whatisagenome}

The human genome is an instruction manual for building and operating a
human being at the molecular level.

This instruction manual exists in every cell of the human body, and it
is encoded in the long string-like molecules of [DNA](#DNA).

[]{#genetic-disorder}

### What is a genetic condition? {#whatisageneticcondition}

A genetic condition results from damaging alterations to the
[genome](#genome) of an organism.

Most genetic conditions are the result of alterations inherited from one
or both parents, and in these, the alterations are present in every
cell.

There is a less common class of genetic conditions in which only some
fraction of a patient's cells experiences a condition -- a situation
known as [somatic mosaicism](#somatic-mosaicism).

Cancer is an example of an genetic condition that begins with
alterations to the [genome](#genome) of a single cell in a previously
healthy patient.

[]{#exome}

### What is an exome? {#whatisanexome}

The exome is the part of the [genome](#genome) that contains
instructions for constructing [proteins](#protein), and it constitutes
about 1% of the entire human genome.

The remainder of the [genome](#genome) outside of the exome is the
[non-coding region](#non-coding-region).

Despite its smaller size, it is estimated that most [genetic
disorders](#genetic-disorder) arise from mutations that alter
[proteins](#protein).

Sequencing the exome instead of the whole genome is an economical way to
look for the root cause of genetic disorders.

[]{#mutation}

### What is a mutation? {#whatisamutation}

A mutation is an [alteration of the genome](#how-mutation).

[]{#sequencing}

### What is sequencing? {#whatissequencing}

Sequencing is a process that uses cells (usually from blood) to read the
genome (or exome) of an individual.

Sequencing permits the identification of mutations.

At present, sequencing the exome is less expensive than sequencing the
entire genome.

[]{#gene}

### What is a gene? {#whatisagene}

A gene is a region in the genome that encodes the instructions for
building a [gene product](#gene-product).

[]{#gene-product}

### What is a gene product? {#whatisageneproduct}

A gene product is a molecule encoded by a gene.

There two kinds of gene products: [proteins](#protein) and [non-coding
RNAs](#non-coding-RNA).

In most genetic disorders studied today, errors in protein-coding genes
are responsible, but there are disorders, such as Prader-Willi Syndrome,
in which [non-coding RNAs](#non-coding-RNA) are implicated.

A protein-coding [gene](#gene) is a region of [DNA](#DNA) that contains
the instructions for building a [protein](#protein) written in the
[standard genetic code](#standard-genetic-code).

[]{#protein}

### What is a protein? {#whatisaprotein}

Protein is a class of molecules that plays a significant role in life.

Proteins are the key actors in cells, and they play many roles,
including:

-   enabling molecular transformations and reactions (cellular
    metabolism);
-   serving as structures within and between cells;
-   mediating communication within and between cells;
-   serving as molecular transporters;
-   conducting cell replication; and
-   building and modifying other proteins.

Structurally, a protein is a sequence of [amino acids](#amino-acid) that
[folds](#protein-folding) into a 3D shape in order to perform its
function.

The instructions for building a protein will be found in a
[gene](#gene), and the instructions will be written in the [standard
genetic code](#standard-genetic-code).

[]{#DNA}

### What is DNA? {#whatisdna}

DNA is a large molecule (a [nucleaic acid](#define-nucleaic-acid)) that
stores the information within the genome.

Viewed as information, a DNA molecule is a long word written in an
alphabet containing the letters `A`, `T`, `C` and `G`.

At a structural level, DNA is composed of two opposing strands, and each
strand is a sequence of [nucleotides](#define-nucleotide), and together,
the two strands form the famous double helical structure.

The two opposing strands in a molecule of DNA are related: A's and T's
pair together between opposing strands and C's and G's pair together, as
in the following simple example of two strands:

    A - T
    G - C
    T - A
    C - G
    T - A

A pair of [nucleotides](#define-nucleotide) linked together within DNA
are known as a [base pair](#base-pair).

[]{#example-gene-dna}

### What's an example of a protein-coding gene in DNA? {#whatsanexampleofaprotein-codinggeneindna}

The following [DNA](#DNA) sequence is a simple [gene](#gene) that
encodes a [protein](#protein) found in the saliva of Gila monsters:

    AACCTGTATATTCAGTGGCTGAAAGATGGCGGCCCGAGCAGCGGCCGCCCGCCGCCGAGC

The process that converts this [DNA](#DNA) sequence into its
corresponding [protein](#protein) is [protein
synthesis](#protein-synthesis).

[]{#define-nucleaic-acid}

### What is a nucleaic acid? {#whatisanucleaicacid}

A nucleaic acid is a chain of [nucleotides](#define-nucleotide) such as
[RNA](#RNA) or [DNA](#DNA).

[]{#define-nucleotide}

### What is a nucleotide? {#whatisanucleotide}

A nucleotide is a molecule that represents one of the letters in the
alphabet for [DNA](#DNA) or [RNA](#RNA).

The four nucleotides in [DNA](#DNA) are adenine (`A`), thymine (`T`),
guanine (`G`) and cytosine (`C`).

The four nucleotides in [RNA](#RNA) are adenine (`A`), uracil (`U`),
guanine (`G`) and cytosine (`C`).

### What is a nucleic acid analogue? {#whatisanucleicacidanalogue}

A nucleaic acid analogue is an artificial nucleaic acid (a DNA- or
RNA-like molecule) that may still have the ability to interact with DNA
or RNA -- or with processes that involve them.

In the case of [oligonucleotide](#define-oligonucleotide) therapeutics,
artificial nucleotides using nucleotide analogues may be used to create
RNA- or DNA-like nucleotides and polymers that can interact with or act
like RNA or DNA.

Some of these alternate nucleic acid chemistries are much longer-lived
in the body, making them more suitable for use as a therapeutic.

[]{#base-pair}

### What is a base pair? {#whatisabasepair}

A base pair is a pairing of two complementary
[nucleotides](#define-nucleotide) in [DNA](#DNA) on opposite strands of
the [DNA](#DNA) helix.

`A` is complementary to `T`, and `C` is complementary to `G`.

[]{#rna}

### What is RNA? {#whatisrna}

RNA is another information-bearing molecule (a \[nucleic acid\]) made of
[nucleotides](#define-nucleotide). It is similar to [DNA](#DNA), except
that it is single-stranded, and in place of thymine there is uracil.

In terms of information content, RNA is a second molecular alphabet
composed of `A`, `U`, `C` and `G`.

When building proteins, [genes](#genes) within [DNA](#DNA) are
[transcribed](#transcription) into [RNA](#RNA), and the RNA is processed
before being [translated](#translation) into a protein.

(`T` becomes `U` during [transcription](#transcription) from [DNA](#DNA)
to RNA.)

In addition to bearing information, some RNA molecules, known as
[non-coding RNAs](#non-coding-RNA), do not translate into proteins, but
still have an active biological role.

[]{#non-coding-RNA} []{#ncRNA}

### What is non-coding RNA (ncRNA)? What is functional RNA? {#whatisnon-codingrnancrnawhatisfunctionalrna}

A non-coding RNA molecule (ncRNA) is an [RNA](#RNA) molecule that does
not end up being translated into a protein.

Non-coding RNA may be called *functional RNA* to emphasize the fact that
even though it does not translate into a [protein](#protein), it may
still have an active biological role, especially in terms of [gene
regulation](#gene-regulation).

[]{#non-coding-region}

### What is the non-coding region of the genome? {#whatisthenon-codingregionofthegenome}

The non-coding region of the [genome](#genome) is the region that does
not encode proteins.

Some regions in the non-coding region contain [non-coding
RNAs](#non-coding-RNA) that do not become proteins, yet play an active
role in the cell.

[]{#define-oligonucleotide}

### What is an oligonucleotide? {#whatisanoligonucleotide}

An oligonucleotide (*oligo* being Greek meaning "a few") is a short
strand of [RNA](#RNA) or [DNA](#DNA) or, more generally, any chain of
nucleic acid analogues.

These short sequences can play active biological roles, especially in
[gene regulation](#gene-regulation) and [splicing](#splicing).

Synthetic oligonucleotides form a potential basis for some therapies.

[]{#variant} []{#allele}

### What is a variant/allele? {#whatisavariantallele}

A *variant* or *allele* is a version of a [gene](#gene).

Though all humans have roughly the same set of genes, each of us has two
alleles for most genes -- one from the chromosome from our father, the
other from the chromosome from our mother.

(The exception is for genes on the Y [chromosome](#chromosome) in
males.)

For most genes, there is a large collection of common variants that make
up the bulk of the alleles in the population.

Mutations in a gene produce new alleles.

[]{#wild-type}

### What is a wild-type allele? {#whatisawild-typeallele}

A wild-type [allele](#variant) for a gene is a commonly occurring
non-pathogenic version found in nature.

In disorders that impact only one of two alleles for a gene, it may be
therapeutic to target the wild-type allele by boosting its activity in
loss of function disorders and reducing its activity in gain of function
disorders.

[]{#penetrance}

### What is the penetrance of an allele with respect to a phenotype? {#whatisthepenetranceofanallelewithrespecttoaphenotype}

The penetrance of an allele with respect to a phenotype refers to the
percentage of the population that will exhibit that phenotype when that
allele is present.

If a disease-causing allele is highly penetrant, then most of the people
with that allele will suffer the disease.

[]{#how-mutation}

### How do mutations change a genome? {#howdomutationschangeagenome}

A mutation is an alteration of the genome (inserting, changing or
deleting letters).

In the context of the Gila monster gene, we can imagine a mutation that
transforms the sequence:

    AACCTGTATATTCAGTGGCTGAAAGATGGCGGCCCGAGCAGCGGCCGCCCGCCGCCGAGC

into the sequence:

    AACGTGTATATTCAGTGGCTGAAAGATGGCGGCCCGAGCAGCGGCCGCCCGCCGCCGAGC

In this case, the fourth letter was changed from C to G.

Geneticists have even developed a notation (called [HGVS
notation](#hgvs-notation)) for describing mutations at the DNA level,
and this one would be called *c*.4C\>G

Under some circumstances, a mutation (or collection of mutations) may
lead to a genetic disorder.

And, when a mutation happens in an individual cell later in life, it may
give rise to cancer.

[]{#de-novo}

### What is a *de novo* mutation? {#whatisa_denovo_mutation}

A *de novo* (a Latin expression implying newness) mutation is one that
it is unique to a child, and not found in either parent.

Through chance, every human being carries a few *de novo* mutations.

While *de novo* mutations are usually harmless on their own, they are
often scrutinized in cases of rare disease.

[]{#inherited-mutation}

### What is an inherited mutation? {#whatisaninheritedmutation}

A mutation is *inherited* if it has been passed from parent to child.

[]{#germline-mutation}

### What is a germline mutation? {#whatisagermlinemutation}

A germline mutation is a *de novo* [mutation](#mutation) that occurs
early in development of an organism.

The cells, tissues and organs that descend from the mutant cell carry
the mutation, but the rest do not.

The result is [somatic mosaicism](#somatic-mosaicism).

[]{#genotype}

### What is a genotype? {#whatisagenotype}

A genotype is the set of [alleles](#variant) for a specific organism.

In the context of genetic condition, *genotype* also refers to the
specific alleles responsible for causing the disease.

During the diagnostic phase of a genetic disorder, *genotype* may also
refer to the collection of mutations under suspicion uncovered by
[sequencing](#sequencing).

[]{#pathogenic}

### What is a pathogenic variant/mutation? {#whatisapathogenicvariantmutation}

A [variant](#variant) is *pathogenic* if it *can* cause disease.

Diagnostic reports label [variants](#variant) according to their
possible relationship to disease.

The commonly reported classifications for a variant are "benign,"
"likely benign," "uncertain significance," "likely pathogenic," or
"pathogenic."

Many variants are classified as "uncertain significance," meaning it is
not presently known whether the variant can cause disease.

It is critical to note the [inheritance
pattern](#pattern-of-inheritance) associated with the prediction of
pathogenicity.

For example, if the inheritance pattern is [recessive](#recessive), then
*both* alleles in that gene must be pathogenic in order to cause
disease.

If only one allele is pathogenic in such case, then the person is a
[carrier](#carrier) for the disorder, but he or she should not be a
patient with the disorder.

(A corner case here would be if the patient has a pathogenic allele for
a recessive disorder paired with a deletion of the allele. In this case,
the resulting total loss of activity in the gene could drive disease.)

Thus, when determining the relevance of all the reported mutations, it
makes sense to ask whether the [genotype](#genotype) (the collection of
all the mutations) itself is pathogenic.

[]{#pattern-of-inheritance}

### What is pattern of inheritance? {#whatispatternofinheritance}

In the context of human disease, the pattern of inheritance for disease
refers to how genes must be inherited from parents in order to exhibit
the disease.

The three common patterns of inheritance for genetic disorders are:

-   [autosomal recessive](#recessive), in which there is a one in four
    chance that a child of two [carriers](#carrier) will have the
    disorder;

-   [autosomal dominant](#dominant), in which there is a one in two
    chance that a child of a [carrier](#carrier) will have the disorder;
    and

-   [X-linked](#x-linked), in which there is a one in two chance that
    the son of a mother carrying the disorder will have the disorder
    while daughters have a one in two chance of being a carrier.

[]{#chromosome}

### What is a chromosome? {#whatisachromosome}

At a structural level, a chromosome is a long string of [DNA](#DNA) plus
packaging material that holds it together and aids in regulating \[gene
expression\].

At a genetics level, a chromosome is a collection of [genes](#genes).

Humans carry 23 pairs of chromosomes (for 46 total).

One of these 23 pairs is the sex chromosome pairing -- two X chromosomes
for women, an X and a Y chromosome in men.

Each pair of the remaining pairs are [autosomes](#autosome).

[]{#autosome}

### What is an autosome? {#whatisanautosome}

Within each pair of [chromosomes](#chromosome), each autosome carries a
set of genes redundant (often called "homologous") with the other.

This redundancy built in to autosome pairs provides protection against
mutations: if one [allele](#variant) of a [gene](#gene) is damaged,
there is a good chance the [allele](#variant) on the other autosome is
still viable, and in many cases, one functional copy of a gene is
sufficient.

When a condition is "autosomal" it means that it involves one of the 22
pairs of autosomal [chromosomes](#chromosome).

[]{#x-linked}

### What is an X-linked condition? {#whatisanx-linkedcondition}

An X-linked condition is one in which a [gene](#gene) on the X
[chromosome](#chromosome) is impacted.

Because men have only one copy of the X [chromosome](#chromosome), these
conditions tend to present only in men, while women are
[carriers](#carrier).

In an X-linked condition, the odds of mother that [carries](#carrier) a
condition will produce an affected son is 1 in 4.

If the mother knows she is carrying a boy, the odds of being affected
increase to 1 in 2.

[]{#zygosity}

### What is the difference between homozygous and heterozygous? {#whatisthedifferencebetweenhomozygousandheterozygous}

An individual is homozygous for a gene if they have two identical
[alleles](#variant) for that [gene](#gene).

An individual is heterozygous for a [gene](#gene) if they have two
different [alleles](#variant) for a [gene](#gene).

[]{#compound-heterozygous}

### What is a compound heterozygous individual? {#whatisacompoundheterozygousindividual}

In human disease, an individual is compound heterozygous for a gene if
they have two different [alleles](#variant) for a [gene](#gene), yet
have a recessive disease caused by that gene.

This is is usually the the result of two different loss of function
alleles.

[]{#haplosufficient}

### What is haplosufficiency? {#whatishaplosufficiency}

With the exception of the Y [chromosome](#chromosome) in men, each gene
has two copies in the genome.

A haplosufficient gene is one for which only functioning
[allele](#variant) is necessary for full function.

A haploinsufficient gene requires both copies of the [gene](#gene) for
full function.

When a loss of function variant is discovered for an
[autosomal](#autosome) gene, it is important to consider whether that
gene is haploinsufficient.

[]{#dominant}

### What is a *dominant* disorder? {#whatisa_dominant_disorder}

If a pathogenic mutation can cause disease by itself, then it is
*dominant*.

If a parent has a dominant pathogenic mutation, that parent should have
the disorder, and one out of every two children on average will have the
same disorder.

[]{#recessive}

### What is a *recessive* disorder? {#whatisa_recessive_disorder}

If a pathogenic mutation requires being paired with another pathogenic
mutation (usually in the same gene) to cause disease, then it is
*recessive*.

If someone has only one copy of a recessive mutation, then they are a
*carrier*.

Many genetic conditions are recessive because humans carry two copies of
most genes (one on each [autosome](#autosome)), and usually only one
working copy of a gene is necessary.

[]{#carrier}

### What is a carrier? {#whatisacarrier}

In the context of human disease, someone is a carrier for a
[recessive](#recessive) disorder if they have a
[pathogenic](#pathogenic) mutation for a [gene](#gene) that can cause
the disorder, but also a functioning copy of that gene as well.

Carriers often have no symptoms, and in some cases have mild symptoms.

If two carriers for a [autosomal](#autosome) recessive condition have a
child, on average, on out of four children will have the condition.

If a carrier (a mother) for an [X-linked](#x-linked) condition has a
child, then there is a one out of two chance that any boy will have the
condition.

[]{#exon} []{#intron}

### What is an exon? What is an intron? {#whatisanexonwhatisanintron}

In most genes, the sequence of DNA for a gene will be composed of both
exons and introns.

Exons are the subsequences of a gene that encode protein structure,
while the remaining regions between exons -- introns -- are ignored
during protein construction.

When proteins are constructed, there is a [splicing](#splicing) phase
that removes introns.

Exome sequencing focuses primarily on exons.

[]{#transcription}

### What is transcription? {#whatistranscription}

Transcription is the first phase of converting a [gene](#gene) encoded
in [DNA](#DNA) into a [protein](#protein).

In transcription, the [DNA](#DNA) for a [gene](#gene) is copied into its
corresponding RNA [transcript](#transcript).

After some additional processing, [RNA](#RNA) is then
[translated](#translation) into an [amino acid](#amino-acid) sequence,
and the [amino acid](#amino-acid) sequence folds into a
[protein](#protein).

Some strategies for treating [genetic disorders](#genetic-disorder) such
as readthrough and [exon-skipping](#exon-skipping-therapeutics) involve
interacting with the [RNA](#RNA) for a gene after transcription.

[]{#example-gene-rna}

### What is an example of a coding RNA sequence after transcription? {#whatisanexampleofacodingrnasequenceaftertranscription}

For example, once transcribed into the protein-coding portion of the
RNA, the code for the protein from the Gila monster looks like:

    AACCUGUAUAUUCAGUGGCUGAAAGAUGGCGGCCCGAGCAGCGGCCGCCCGCCGCCGAGC

[]{#transcript}

### What is a transcript? {#whatisatranscript}

A transcript is the [RNA](#RNA) molecule that has been produced for a
gene.

(A transcript may also be called the *primary transcript* to distinguish
it from RNA that has been processed through mechanisms such as
[splicing](#splicing).)

[]{#messenger-RNA}

### What is messenger RNA (mRNA)? {#whatismessengerrnamrna}

Messenger RNA (mRNA) is the [RNA](#RNA) that remains after
[splicing](#splicing), and is destined for [translation](#translation)
into a [protein](#protein).

[]{#rna-sequencing}

### What is RNA sequencing? {#whatisrnasequencing}

[RNA](#RNA) sequencing takes a snapshot of the active RNA
[transcripts](#transcript) in a cell at a given time.

RNA sequencing yields insights into which [genes are
expressed](#gene-expression) by a particular cell and the quantity of
expression.

[]{#transcriptomics}

### What is transcriptomics? {#whatistranscriptomics}

Transcriptomics uses [RNA](#RNA) sequencing to interrogate the
[transcripts](#transcript) present in specific cells and across time and
environments.

Transcriptomics often seeks to discover [regulatory
relationships](#gene-regulation) between genes.

In the context of human disease, transcriptomics can identify
disregulated genes and suggest [corrective
therapies](#process-finding-therapies-with-transcriptomics).

[]{#amino-acid}

### What is an amino acid? {#whatisanaminoacid}

An amino acid is an individual building block for a [protein](#protein):
proteins are created as chains of amino acids joined together.

Each amino acid has a side chain, with properties such as hydrophobicity
(attracted to or repelled by water) and electrical charge (positive or
negative).

To a large degree, the properties of the side chains determine the
structure and function of the entire protein.

(For example, some proteins require [chaperones](#chaperone) to achieve
their intended structure.)

For instance, mutations in [DNA](#DNA) can change one amino acid to
another in the resulting protein, which may in turn enhance or degrade
the structure and function of the resulting [protein](#protein).

There are 20 standard amino acids ordinarily used for [protein
synthesis](#protein-synthesis):

-   Alanine (Ala, A)
-   Arginine (Arg, R)
-   Asparagine (Asn, N)
-   Aspartic acid (Asp, D)
-   Cysteine (Cys, C)
-   Glutamine (Gln, Q)
-   Glutamic acid (Glu, E)
-   Glycine (Gly, G)
-   Histidine (His, H)
-   Isoleucine (Ile, I)
-   Leucine (Leu, L)
-   Lysine (Lys, K)
-   Methionine (Met, M)
-   Phenylalanine (Phe, F)
-   Proline (Pro, P)
-   Serine (Ser, S)
-   Threonine (Thr, T)
-   Tryptophan (Trp, W)
-   Tyrosine (Tyr, Y)
-   Valine (Val, V)

Each amino acid is represented by one or more
[codons](#standard-genetic-code) in the [standard genetic
code](#standard-genetic-code).

Under the running example of the Gila monster protein, the chain of
amino acids encoded by the gene becomes:

    NLYIQWLKDGGPSSGRPPPS

[]{#protein-synthesis}

### How are proteins created? {#howareproteinscreated}

During the construction of a protein (often called protein synthesis), a
gene is first [transcribed](#transcription) into RNA.

Once transcribed into [RNA](#RNA), the [introns](#intron) are
[spliced](#splicing) out.

The resulting RNA, which contains only the [exons](#exon), is called
[messenger RNA](#messenger-RNA) (mRNA).

The [messenger RNA](#messenger-RNA) is [translated](#translation) into a
sequence of amino acids according to the [standard genetic
code](#standard-genetic-code).

Many proteins are further modified through [post-translational
modifications](#post-translational-modification) after synthesis.

[]{#splicing}

### What is RNA splicing? {#whatisrnasplicing}

When the [DNA](#DNA) for a gene is first transcribed into [RNA](#RNA),
it contains both [exons](#exon) (which contain part of the code for a
protein) and [introns](#intron) (which do not).

[RNA](#RNA) splicing is the phase in which the nucleotides for
[introns](#intron) are removed.

For protein-coding genes, the resulting [RNA](#RNA) is [messenger
RNA](#messenger-RNA).

Mutations in [introns](#intron) that impact splicing can still result in
pathogenic alterations to the resulting protein.

In some cases, splicing will also remove [exons](#exon), resulting in a
[transcript variant](#transcript-variant).

[]{#transcript-variant}

### What is a transcript/splice variant? {#whatisatranscriptsplicevariant}

When a [RNA splicing](#splicing) removes one or more exons, it creates
transcript variants.

Transcript variants lead to different proteins, some of which have
modified functionality.

Attempting to force the synthesis of an transcript variant by
[deliberating skipping an exon](#exon-skipping-therapeutics) is a
therapeutic strategy for some mutations.

Since [mutations](#mutation) are usually reported with respect to a
transcript variant, it is important to make sure that the transcript
variants are identical when comparing mutations, or else to interconvert
the mutations between transcript variants.

[]{#standard-genetic-code} []{#codon}

### What is the standard genetic code? What is a codon? {#whatisthestandardgeneticcodewhatisacodon}

The standard genetic code maps three-letter patterns in DNA to codons.

A codon is an individual instruction in the list of instructions for
building a protein.

A codon encodes one of two types of instructions:

-   insert a specific amino acid next; and

-   stop production of the protein.

For example, the DNA codon `ATG` (which becomes `AUG` in RNA) means
"insert a methionine next," while DNA codon `TGA` (which becomes `UGA`
in RNA) means "stop."

There are 64 possible codons, but only 20 of them represent unique amino
acids. (For example, `AAA` and `AAG` both mean "insert a Lysine.")

Under this interpretation of DNA, we can re-orient the Gila monster gene
into codons and their corresponding instructions, much as if it were a
computer program or a recipe:

    AAC;  // Insert Asparagine
    CTG;  // Insert Leucine
    TAT;  // Insert Tyrosine
    ATT;  // Insert Isoleucine
    CAG;  // Insert Glutamine
    TGG;  // Insert Tryptophan
    CTG;  // Insert Leucine
    AAA;  // Insert Lysine
    GAT;  // Insert Aspartic Acid
    GGC;  // Insert Glycine
    GGC;  // Insert Glycine
    CCG;  // Insert Proline
    AGC;  // Insert Serine
    AGC;  // Insert Serine
    GGC;  // Insert Glycine
    CGC;  // Insert Arginine
    CCG;  // Insert Proline
    CCG;  // Insert Proline
    CCG;  // Insert Proline
    AGC;  // Insert Serine
    TGA;  // Stop

After running this program, we have the following sequence of amino
acids stitched together:

    NLYIQWLKDGGPSSGRPPPS

[]{#translation}

### What is protein translation? {#whatisproteintranslation}

During protein synthesis, protein translation is the construction of an
amino acid sequence from the corresponding RNA under the standard
genetic code.

[]{#proteomics}

### What is proteomics? {#whatisproteomics}

Proteomics interrogates all of the [proteins](#protein) present in
specific cells and across time and environments.

At present, there are a variety of approaches for conducting proteomics.

In the context of human disease, proteomics can identify disregulated
proteins and suggest [corrective therapies](#proteomics-therapeutics).

[]{#mutation-types}

### What are the types of mutations in proteins? {#whatarethetypesofmutationsinproteins}

With an understanding of the [standard genetic
code](#standard-genetic-code), it is possible to categorize mutations
according to their impact on the protein.

The major categories for mutations in protein-coding region of genes
are:

-   [premature stop mutations](#premature-stop);
-   [frameshift mutations](#frameshift);
-   [in-frame mutations](#in-frame);
-   [missense mutations](#missense); and
-   [synonymous mutations](#synonymous).

[]{#hgvs-notation}

### How do you interpret HGVS notation for mutations? {#howdoyouinterprethgvsnotationformutations}

The [HGVS specification](http://www.hgvs.org/mutnomen/) provides a
shorthand notation for describing mutations in a [gene](#gene).

Variants are commonly reported in two different ways at the same time,
in the coding [DNA](#DNA) notation and in the protein-coding notation.

The coding [DNA](#DNA) notation (prefixed with *c*.) indicates at which
[nucleotide](#define-nucleotide) in the *coding* DNA the mutation starts
and what kind of [mutation](#mutation) it was.

The coding DNA is the [DNA](#DNA) that remains when the
[introns](#intron) are [spliced](#splicing) out.

For example:

-   *c*.24G\>C means that the 24rd [nucleotide](#define-nucleotide) was
    changed from G to C.

-   *c*.24Cdel means that the 24th [nucleotide](#define-nucleotide) was
    deleted.

-   \_c.\_67_68insT means that a T was inserted between
    [nucleotides](#define-nucleotide) 67 and 68.

The protein-coding notation (prefixed with *p*.) indicates the effect of
a mutation on the [amino acid](#amino-acid) sequence for a protein.

For example:

-   *p*.R401X means that the 401st [codon](#standard-genetic-code) was
    changed from an arginine [codon](#standard-genetic-code) to a stop
    [codon](#standard-genetic-code). (Possibly also written
    *p*.Arg401Ter or *p*.Arg401\*)

-   *p*.Q631SfsX7 means that the 631st [codon](#standard-genetic-code)
    was changed from a glutamine to a serine due to a
    [frameshift](#frameshift) mutation that resulted in a new stop
    [codon](#standard-genetic-code) 7 [codons](#standard-genetic-code)
    away. (Possibly als written as *p*.Gln631fsTer7 or *p*.Gln641fs\*7)

[]{#premature-stop}

### What is a premature stop / framestop / nonsense mutation? {#whatisaprematurestopframestopnonsensemutation}

A premature stop (also called *nonsense*) [mutation](#mutation)
truncates construction of the protein by turning a codon for an amino
acid into a stop codon.

For example, changing the first `A` to `T` in `AGA` turns it into `TGA`.

`AGA` codes for the amino acid arginine, but `TGA` codes for stop.

Truncation usually destroys the function of the resulting protein. (In
fact, nonsense-mediated decay may even prevent the production of
proteins with such mutations.)

For example, the mutation *p*.R401X (possibly also written *p*.Arg401Ter
or *p*.Arg401\*) indicates that the 401st amino acid (an arginine) has
been replaced by a stop [codon](#standard-genetic-code).

For a premature stop mutation, \[readthrough compounds\]
(#readthrough-therapeutics) should be investigated as potential
therapeutics.

[]{#frameshift}

### What is a frameshift mutation? {#whatisaframeshiftmutation}

A mutation that inserts or deletes a number of nucleotides that is not
an even multiple of three will cause a "frameshift" in which subsequent
[codons](#standard-genetic-code) are misinterpreted.

Frameshifts almost always cause a loss of function mutation in the
resulting protein.

For example, *c*.C1891del (also written as *p*.Q631SfsX7) indicates that
a the 1,891st [nucleotide](#define-nucleotide) in the coding DNA for a
protein (in this case a cytosine) was deleted, which caused the
[codon](#standard-genetic-code) at position 631 (formerly a glutamine)
and all subsequent codons to be garbled, until the introduction of a
stop seven codons down.

[]{#in-frame}

### What is an in-frame mutation? {#whatisanin-framemutation}

An in-frame mutation is an insertion or deletion of
[nucleotides](#define-nucleotide) in a protein-coding region which is an
even multiple of three.

This may add or remove one or several [amino acids](#amino-acid).

In-frame mutations are generally less damaging than premature stop or
frameshift mutations.

[]{#missense}

### What is a missense mutation? {#whatisamissensemutation}

A missense mutations changes a codon from one amino acid to another.

If a missense changes the type of the side chain of the amino acid (e.g.
hydrophobic to polar, positive to negative) it is more likely to damage
the function of the protein than missense mutations that do not.

For example, *p*.W244R indicates a tryptophan has become an arginine at
codon 244 (which changes a hydrophobic side chain to into a positively
charged side chain). In some cases, this could be a loss of function
mutation.

To be clear, even a mutation that does not change the side chain type
(such as alinine to valine) can still be pathogenic, as it can *alter*
the function of the protein, [as in the case of prion
disease](http://brain.oxfordjournals.org/content/122/10/1823).

If the effect of a missense mutation is unclear, [homology
modeling](#homology-modeling) may provide insight into the pathogenicity
based on its impact on structure.

[]{#synonymous}

### What is a synonymous mutation? {#whatisasynonymousmutation}

A synonymous mutation changes the underlying nucleotides for a codon,
but it does not change the amino acid.

For example, a mutation that changes `TTA` into `TTG` probably has no
effect, since both codons insert the amino acid Leucine.

[]{#protein-folding}

### What is protein folding? {#whatisproteinfolding}

Once a protein is [synthesized](#protein-synthesis) as a chain of [amino
acids](#amino-acid), that chain begins folding into a 3D structure
determined by the side chains on its amino acids; properties such as the
acidity (pH) of its environment and temperature and the presence of
[chaperone proteins](#chaperone).

As a principle, folding tends to minimize the number of hydrophobic
("water-fearing") side chains on the exterior of the final form.

The final structure of the protein determines its function.

As an example, the Gila monster protein, after folding into its 3D
shape, looks like:

![Trp Cage
Protein](images/trp-cage-small.png "The Tryptophan Cage protein, from Gila monsters")

Proteins that fail to fold correctly can lead to human disease.

[]{#primary-protein-structure}

### What is primary protein structure? {#whatisprimaryproteinstructure}

The primary structure of a protein is the sequence of [amino
acids](#amino-acid) from which it is made.

[]{#secondary-protein-structure}

### What is secondary protein structure? {#whatissecondaryproteinstructure}

Secondary protein structure refers to commonly occurring local units of
structure in proteins that span several amino acids. A beta sheet is an
example of a commonly occurring secondary unit of structure.

[]{#tertiary-protein-structure}

### What is a tertiary protein structure? {#whatisatertiaryproteinstructure}

Tertiary protein structure refers to the 3D shape of a protein after
[folding](#protein-folding) is complete.

[]{#quaternary-protein-structure}

### What is a quaternary protein structure? {#whatisaquaternaryproteinstructure}

Quaternary protein structure refers to the arrangements of multiple
proteins in a [complex](#protein-complex).

[]{#protein-complex}

### What is a protein complex? {#whatisaproteincomplex}

A protein complex is a multi-protein structure.

[]{#simulated-protein-folding} []{#homology-modeling}

### What is homology modeling / simulated protein folding? {#whatishomologymodelingsimulatedproteinfolding}

Homology modeling attempts to reconstruct the 3D structure of a protein
based on its amino acid sequence and its similarity to the known 3D
structure of a similar sequence of sequences.

For example, if the structure of a wild-type allele is known, then
changing only one amino acid makes it possible to estimate what the new
structure may look like without attempting to solve the entire 3D
structure from scratch.

Protein folding simulation is a technique in computational biology for
predicting the folded structure of a protein.

While *ab initio* [protein folding](#protein-folding) simulations can be
computationally expensive and accuracy is problematic, a computed
folding may offer evidence as to whether [domains of function](#domain)
in a protein are still functional, or whether their [binding
affinity](#binding-affinity) has been altered.

Programs such as [Phyre2](http://www.sbg.bio.ic.ac.uk/phyre2) attempt to
predict the folding of a protein from sequence data, which may yield
insight into the structure of a mutant protein.

[]{#crystallography}

### What is crystallography? {#whatiscrystallography}

Crystallography is a collection of methods for studying and determining
the structure of a crystal.

By freezing proteins into crystals, crystallography (in particular,
x-ray crystallography), can determine their 3D structure.

[]{#antisense-oligonucleotide}

### What is an antisense oligonucleotide? {#whatisanantisenseoligonucleotide}

An antisense [oligonucleotide](#define-oligonucleotide) is a short
sequence of RNA- or DNA-like nucleotides designed to bind to a
particular target sequence or sequence(s).

For example, if the [RNA](#RNA) sequence to be targeted is `AUAG`, then
the antisense oligonucleotide is `UAUC`.

Because antisense oligonucleotides bind to their complements, they can
mute them during protein translation.

In the case of [knockdown](#knockdown) model organisms, these
complementary fragments of [RNA](#RNA) can silence an entire gene.

In the case of [exon-skipping
therapeutics](#exon-skipping-therapeutics), an antisense oligonucleotide
for a particular [exon](#exon) (such as the one containing the harmful
mutation) can cause the [exon](#exon) to be [spliced](#splicing) out
during [protein construction](#protein-synthesis).

[]{#post-translational-modification}

### What is a post-translational modification? {#whatisapost-translationalmodification}

[Proteins](#protein) are often modified after translation by processes
such as glycosylation, [phosphorylation](#define-phosphorylation) or
methylation.

The sites at which proteins are modified is often based on consensus
sequences among [amino acids](#amino-acid) in a protein.

There are a variety of tools for predicting [post-translational
modification
sites](http://www.expasy.org/proteomics/post-translational_modification).

For example, N-linked glycans are usually attached to
[proteins](#protein) at an asparagine which is followed by any [amino
acid](#amino-acid) except proline followed by either a serine or
threonine.

A mutation that alters the consensus sequence -- for instance changing
the asparagine to an aspartate -- would likely prevent N-linked glycans
from being attached, which may in turn alter the function or stability
of the resulting protein.

[]{#protein-types}

### What functions do proteins have? {#whatfunctionsdoproteinshave}

Proteins serve a variety of functions within a cell.

In a genetic disorder that involves a protein, the type of protein
involved may influence therapeutic strategies.

Major types of proteins include:

-   [enzymes](#enzyme);
-   receptors;
-   [chaperones](#chaperone);
-   hormone/signaling proteins;
-   storage proteins;
-   motor proteins;
-   immune proteins;
-   protective proteins;
-   transporter proteins;
-   structural proteins; and
-   regulatory proteins.

Some proteins have more than one type.

[]{#domain}

### What is a domain of function? {#whatisadomainoffunction}

A domain of function is a region within a protein that is responsible
for a specific function.

A given [protein](#protein) may have several domains which work
together, domains that work independently or some combination thereof.

When analyzing mutations, it is useful to examine their potential impact
on the known domains of function within that protein.

[]{#enzyme} []{#metabolic-pathway}

### What is an enzyme? What is a metabolic pathway? {#whatisanenzymewhatisametabolicpathway}

An enzyme is a protein that enables chemical reactions and molecular
transformations.

Thus, an enzyme creates a metabolic pathway from the inputs to the
reaction to the outputs of the reactions.

A metabolic pathway is an enzyme-driven process for conducting chemical
reactions and molecular transformations.

A pathway diagram for the enzyme lactase illustrates the pathway:

                  ----> galactose
                /
    lactose ---
                \
                  ----> glucose

Some humans with mutations in the gene for lactase -- *LCT* -- cannot
produce lactase, and as a result, they cannot digest lactose, a
condition known as lactose intolerance.

(In fact, as humans age, they produce less lactase, resulting in
increasing lactose intolerance as this pathway shuts down.)

Collectively, enzymes and the pathways they define determine the
metabolism of an organism.

[]{#substrate}

### What is a substrate? {#whatisasubstrate}

A substrate is a compound on which an enzyme acts.

For example, for the enzyme lactase, its substrate is lactose.

[]{#transporter-protein}

### What is a transporter protein? {#whatisatransporterprotein}

A membrane transporter protein is like an automatic door on the surface
of the cell (or an intracellular compartment) that only opens for
specific molecules.

Membrane transporter proteins are selectively permeable membrane-bound
proteins that regulate the movements of molecules inside and outside of
a cell and between intracellular compartments.

Ion channels are an example of a transporter protein.

[]{#ion-channel}

### What is an ion channel? {#whatisanionchannel}

Ion channels are formed by membrane-bound [transporter
proteins](#transporter-protein) that regulate the flow of ions into and
out of a cell or intracellular compartment.

A defect in a ion channel protein can lead to a
[channelopathy](#channelopathy).

[]{#channelopathy}

### What is a channelopathy? {#whatisachannelopathy}

Channelopathies are disorders caused by defects in ion channel proteins
-- specific class of transporter protein -- which regulate the flow of
ions across a membrane.

[]{#receptor}

### What is a receptor? {#whatisareceptor}

Receptors are (generally) membrane-bound proteins that transmit signals
across a membrane boundary, often from outside a cell to inside a cell.

When an agonist docks with its target receptor, it causes the release of
a [secondary messenger](#secondary-messenger) compound on the opposite
side of the membrane.

Receptors can have a baseline activity level -- known as constitutive
activity -- even in the absence of their agonist.

With receptors, antagonists play the role of inhibitors, blocking
agonists from reaching the receptor and preventing the transmission of a
signal.

Unlike enzymes, receptors may also be susceptible to an inverse agonist,
which lower their constitutive activity. (Enzymes have no background
activity in the absence of a substrate.)

[]{#define-kinase}

### What is a kinase? {#whatisakinase}

A kinase is a protein that transfers phosphate groups onto other
molecules, most commonly other proteins.

Kinases may also transfer phosphate groups onto lipids (fats) or onto
carbohydrates.

The process of transferring phosphate groups onto molecules is called
[phosphorylation](#define-phosphorylation).

When phosphorylating, a kinase typically targets a specific amino acid
residue on the protein.

[]{#define-phosphorylation}

### What is phosphorylation? {#whatisphosphorylation}

Phosphorylation is a common [post-translational
modification](#post-translational-modification) for proteins.

Phosphorylation is the process of transferring phosphate groups onto
molecules like proteins, lipids and carbohydrates.

[Kinases](#define-kinase) are the class of proteins repsonsible for this
transfer.

The addition of a phosphate group may activate or inactive the protein.

Dephosphorylation is the process of removing a phosphate group, and a
major group of proteins responsible for this reverse process are
phosphotases.

Phosphorylation and dephosphorylation constitute a major dynamic
regulatory mechanism within biology.

[]{#constitutive-activity}

### What is constitutive activity? {#whatisconstitutiveactivity}

Constitutive activity is the baseline activity of a receptor in the
absence of an agonist.

[]{#secondary-messenger}

### What is a secondary messenger? {#whatisasecondarymessenger}

A secondary messenger is the compound released by a
[receptor](#receptor) when stimulated by an [agonist](#agonist) on the
opposing side of a membrane.

A secondary messenger may trigger a cascade of reactions to the external
stimulus.

[]{#agonist}

### What is an agonist? {#whatisanagonist}

An agonist is an agent that stimulates a [receptor](#receptor) to
release its [secondary messenger](#secondary-messenger).

[]{#antagonist}

### What is an antagonist? {#whatisanantagonist}

An antagonist is an agent that prevents an [agonist](#agonist) from
stimulating a [receptor](#receptor).

[]{#inverse-agonist}

### What is an inverse agonist? {#whatisaninverseagonist}

An inverse agonist lowers the [constitutive
activity](#constitutive-activity) of a [receptor](#receptor).

[]{##chaperone}

### What is a chaperone? {#whatisachaperone}

A chaperone protein aids in the folding of other [proteins](#protein),
or helps to maintain protein folding in the presence of stress (such as
a higher temperature).

[]{#cytogenetic-notation}

### What is cytogenetic notation? {#whatiscytogeneticnotation}

Cytogenetic notation is the notation used to describe regions within
[chromosomes](#chromosome).

The general format of the notation is:

    <chromosome number> 'p' or 'q' <band number> . <sub-band number>

For example, `3p24.2` indicates chromosome 3, `p` indicates the short
arm of the chromosome, `24` is the 24th colored band, and `.2` indicates
the second sub-band within the 24th band.

Characteristic bands show up on [chromosomes](#chromosome) when they're
stained with trypsin, and these bands are identify regions.

In a condition with chromosomal abnormalities, it is important to to
determine from the cytogenic notation which regions of the chromosome
have been deleted or duplicated.

The [UCSC genome browser](http://genome.ucsc.edu/) can list all of the
impacted genes in a region.

With the advent of [sequencing](#sequencing), chromosomal abnormalities
are now often reported in very specific ranges of base pairs.

[]{#somatic-mosaicism}

### What is somatic mosaicism? {#whatissomaticmosaicism}

Somatic mosaicism is the technical term for what happens when mutations
happen early on during development -- in the germline.

For example, if a mutation happens in a cell when a developing human
being is roughly ten cells, than that [mutation](#mutation) may be
present in about 10% of the resulting cells.

Somatic mosaicism can lead to an individual suffering from a disorder
incompletely, and it can also complicate diagnostic sequencing: if the
tissue used for [sequencing](#sequencing) does not contain the
[pathogenic](#pathogenic) mutation, then sequencing will not find it.

[]{#mechanism-of-harm}

### What is a mechanism of harm? {#whatisamechanismofharm}

A mechanism of harm is the process by which a diseases causes harm.

The primary mechanism of harm is the root cause of the disorder, which
in the cause of genetic disorders, is a mutation or group of mutations.

A downstream mechanism of harm is a later link in the chain of causes.

For example, in cystic fibrosis, according to ([Ratjen,
2009](http://www.rcjournal.com/contents/05.09/05.09.0595.pdf)) the
initial loss of function in the CFTR gene leads to:

-   defective chloride and thiocyanate ion transport across cell
    membranes;

-   which leads to loss of surface liquid in the airway;

-   which leads to destabilization of cilia and loss of mucociliary
    transport;

-   which leads to retention of phlegm;

-   which leads to infection;

-   which leads to inflammation;

-   which in turn aggravates the retention of phlegm.

It may be possible to devise therapeutic strategies that intervene at
any link in the chain between mechanisms of harm.

[]{#precision-disease-model}

### What is a precision disease model? {#whatisaprecisiondiseasemodel}

A precision disease model is a biological avatar that encodes key
aspects of a patient's disease.

A precision disease model can be a cellular model or a [model
organism](#model-organism).

A cellular model can be constructed directly from the patient's own
cells, or it can be created from another cell line, usually by
genetically editing the cell line to match the patient's genotype.

[]{#model-organism}

### What is a model organism? {#whatisamodelorganism}

A model organism is an organism that has been genetically modified or
bred to exhibit a specific [phenotype](#phenotype) or the analog of a
human disorder.

Common model organisms include:

-   *E. coli* bacteria;
-   yeast (often *Saccharomyces cerevisiae*);
-   worms (often *Caenorhabditis elegans*);
-   fruit flies (often *Drosophila melanogaster*);
-   zebrafish (*Danio rario*);
-   mice; and
-   rats;

and there are [dozens of other model
organisms](https://en.wikipedia.org/wiki/List_of_model_organisms) also
used in research.

In the context of genetic disorders, model organisms may have human
mutations introduced (a knock-in), or an entire gene removed (a
knockout).

[Creating model organisms](#process-creating-model-organisms) is useful
in many stages of disease research, from discovery and diagnosis to the
development of therapeutics.

[]{#knockout}

### What is a knockout organism? {#whatisaknockoutorganism}

A knockout organism is one in which a gene has been removed.

Knockout organisms are useful for studying the role of a particular
gene.

Knockout organisms are also useful for studying recessive disorders in
which the primary mechanism is total loss of function in a gene.

[]{#knockdown}

### What is a knockdown organism? {#whatisaknockdownorganism}

By introducing interfering RNA for a specific gene into to cells, it is
possible to dial down (and even eliminate) the expression of a target
gene.

When the interfering RNA is introduced exogenously, the interfering RNA
is eventually depleted and gene activity is restored.

It is also possible to construct permanent knockdowns, in which gene
expression is dialed down through genetic modification.

Because the amount of interfering RNA can be varied, it is posible to
study the effect of differing levels of expression of a gene.

[]{#knockin}

### What is a knock-in organism? {#whatisaknock-inorganism}

A knock-in organism is one in which a specific gene has been introduced.

In organisms that contain the equivalent of a human gene, the human
version can be inserted to test its functional equivalence and
conservation.

In addition, a disease-causing version of a gene from a human patient
can be knocked in to create a more faithful model organism in which to
study a disorder.

Some therapeutic strategies can only be tested on knock-in models. For
example, [activating a mutant
allele](#process-inhibiting-or-activating-a-target) only works if there
is a mutant allele to upregulate.

[]{#fibroblast}

### What is a fibroblast? {#whatisafibroblast}

In the context of human disease, a fibroblast cell line is a cell line
usually created from the skin of patients (and sometimes family
members).

[]{#stem-cell}

### What is a stem cell? What is an iPS cell? {#whatisastemcellwhatisanipscell}

A stem cell is an immature cell that can be differentiated into many
different cell types, e.g., skin, cardiac tissue, neurons.

Embyronic stem cells are the most differentiable.

Induced pluripotent stem cells (iPS cells) are mature adult cells that
have been reprogrammed to behave like early stem cells.

[]{#ipsc-advantages}

### What are the advantages of iPS cell lines? {#whataretheadvantagesofipscelllines}

For [genetic disorders](#genetic-disorder), iPS cells make it possible
to obtain tissue types which may otherwise be difficult or impossible to
extract directly from patients.

[]{#biomarker}

### What is a biomarker? {#whatisabiomarker}

A biomarker is an observable indicator of a disease state, often used is
clinical trials to measure the effectiveness of a therapy.

An example of a biomarker is the presence of oligosaccharides in urine;
this is a biomarker for many lysosomal storage diseases.

As another example, low protein in the cerebrospinal fluid (CSF) is a
biomarker for [NGLY1 deficiency](http://www.ngly1.org/).

[]{#assay}

### What is an assay? {#whatisanassay}

In biochemistry, an assay is a technique for measuring a property of
interest in a sample.

An assay is defined by both a process and a collection of material
necessary to execute the process.

Assays are often run by hand, but in some cases, they may be automated
for high-throughput screening.

From the perspective of practicing precision medicine, it is critical to
note that developing an assay may require an act of scientific
discovery, which in turn hinges on the creative process underpinning
scientific progress.

For example, an assay that targets the primary mechanism of harm in an
enzyme deficiency disorder will (somehow) measure the activity of the
enzyme.

Running the assay on patient cells should show no activity for the
enzyme, while running the assay on control cells should show activity
for the enzyme.

In this example, the assays is useful for validating compounds predicted
to restore the activity of the missing enzyme.

For instance, if patient cells are treated with the compound and then
run through the assay, and it shows activity, then the compound may be a
target for drug development.

[]{#molecular-therapy}

### What is a molecular therapy? {#whatisamoleculartherapy}

A molecular therapy is one that targets the molecular basis for a
disorder.

In a [genetic disorder](#genetic-disorder), a molecular therapy can
attempt to correct a mutation itself at a genetic level (as in
gene-editing or readthrough therapeutics), or it can attempt to
compensate at the protein level (as in mutant protein stabilization), or
it can intervene at a downstream [mechanism of harm](#mechanism-of-harm)
with a molecular basis.

[]{#gene-expression}

### What is gene expression? {#whatisgeneexpression}

Gene expression refers to the presence and quantity of the [gene
product](#gene-product) associated with a [gene](#gene), and to the act
of creating the [gene product](#gene-product).

Increasing gene expression for a protein-coding gene implies increasing
the [protein](#protein) encoded by that gene.

In some contexts, increasing gene expression refers to increasing the
RNA transcription for the gene (and assuming a corresponding increase in
the protein).

[]{#gene-regulation}

### What is gene regulation? {#whatisgeneregulation}

Gene regulation refers to the processes and entities that manage the
expression of genes.

Even though every cell (except for sperm and eggs) contains every gene
for an individual, not every cell expresses all of the gene products
associated with every gene, and even with a cell, the proteins being
expressed depend on the environment and state of the cell.

[]{#gene-regulatory-network}

### What is a gene regulatory network? {#whatisageneregulatorynetwork}

Genes exert regulatory effects on each other: the expression of one gene
may increase or decrease the expression of another gene.

RNA sequencing, the basis for [transcriptomics](#transcriptomics),
examines a snapshot of the RNA content in a cell, which can infer
regulatory relationships.

A gene regulatory network expresses the regulatory dependence
relationships between genes.

[]{#antibody}

### What is an antibody? {#whatisanantibody}

Within the immune system, an antibody is a kind of protein that is
adapted to recognize many different (presumably infectious) agents.

Antibodies have a Y-like structure, and the tips contain a region that
can be varied significantly to recognize a wide variety of molecules.

Once an antibody recognizes its target, it signals it for destruction
(or may actively disable the target on its own).

Some therapeutics are also based on developing custom antibodies to
recognize harmful agents.

In laboratory science, special antibodies are often developed to detect
the presence and quantity of particular agents.

[]{#binding-affinity}

### What is binding affinity? {#whatisbindingaffinity}

With respect to a given structure such as [DNA](#DNA) or [a domain on a
protein](#domain-of-function), the binding affinity of another molecule
is the degree to which this secondary molecule is attracted.

Drug design often depends on optimizing binding affinity.

[]{#identifying-an-expert}

### How do I find the right scientific expert? {#howdoifindtherightscientificexpert}

One of the most challenging aspects of precision medicine from the
patient side is the identification of qualified and appropriate
scientific expertise.

The Weber Lab at Harvard has created search engines for expertise:

-   [Harvard Catalyst Expert
    Search](https://connects.catalyst.harvard.edu/profiles/search/people)

-   [Direct2Expert](http://direct2experts.org/)

In standard medicine, patients expect to be able to work with a single
physician, but in precision medicine, each stage may require a different
physician or scientist.

Evaluating the quality and fit of a potential scientific partner may
also be challenging for non-academics.

Questions to answer when considering the fit of a scientist include:

-   Does the scientist have publications that relate to the genes,
    models or mechanisms of interest?

-   Does the scientist have research funding already aligned with genes,
    models or mechanisms of interest?

If funding a scientist, it is important to request a plan that explains
and justifies both the basic and translational scope of research
efforts.
:::
