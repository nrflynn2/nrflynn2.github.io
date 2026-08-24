---
layout: "post"
title: "Novel vs repurposed targets: quantifying novelty and extending drug-repurposing methods"
date: "2026-05-29 09:00:00-0700"
description: "Drug target novelty is measurable, and the trade-off with drug repurposing is the commercial story most pipelines never quantify. A practitioner's map."
tags:
  - "machine learning"
  - "drug discovery"
  - "target discovery"
  - "drug repurposing"
categories:
  - "target discovery"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/blog/target-discovery/APPH_FLYNN_UN19.png"
og_image: "https://noahrflynn.com/assets/img/blog/target-discovery/APPH_FLYNN_UN19.png"
series: "Drug Target Discovery"
series_order: 5
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is a novel drug target?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A novel drug target is a gene or protein with no approved-drug association by mechanism of action. In Agarwal's ~1,000-target analysis, roughly 712 of 959 targets were novel by that criterion, and more than half had no competitor programs. That is why novelty often translates into commercial solitude. The NIH Illuminating the Druggable Genome initiative offers a more useful gradient through four Target Development Levels: Tclin, Tchem, Tbio, and Tdark. The binary novel/proven split collapses the Tchem/Tbio/Tdark gradient, which is why the TDL framework is more useful for target-selection decisions."
        }
      },
      {
        "@type": "Question",
        "name": "How is drug repurposing different from drug discovery?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Drug discovery starts with a disease and searches for new targets and molecules. Drug repurposing starts with an approved or well-characterized compound and searches for new disease indications. From a target-novelty perspective, repurposing operates on already-proven targets because the compound already has an approved-drug association. The novelty sits in the indication. Roughly one-third of recent drug approvals are repurposing-adjacent, and the Phase I likelihood of approval for non-originator products is roughly twice that for novel therapies (14.7% vs 6.8% in the 2011–2020 BIO report), driven mostly by reduced attrition at the Phase III transition (70.3% vs 52.9%). The trade-off is weaker intellectual-property protection, including three-year US data exclusivity for a repurposing claim versus five-year exclusivity for a new chemical entity, plus vulnerability to generic-manufacturer skinny labelling."
        }
      },
      {
        "@type": "Question",
        "name": "What is skinny labelling?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Skinny labelling is the US regulatory practice in which a generic manufacturer launches an off-patent molecule with a label that omits one or more indications still covered by method-of-use patents. The generic competes on off-patent indications and tries to avoid infringement on the patented repurposing-specific use. For repurposing sponsors, that weakens the commercial position of a new-indication program because a generic entrant can capture the old-indication market, and the sponsor still has to defend the method-of-use patent separately. The legal and commercial landscape continues to evolve through cases such as GlaxoSmithKline v. Teva and related litigation."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Pharos database?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pharos is the public-facing portal for the NIH Illuminating the Druggable Genome (IDG) initiative, launched in 2014 and maintained by the IDG Knowledge Management Center. It is the standard reference for Target Development Level (TDL) classifications, Tclin, Tchem, Tbio, and Tdark, and it aggregates target information including tissue expression across healthy human tissues, protein structure when available, associated drugs and diseases, pathway memberships, and literature signals. For novelty scoring, the TDL assignment anchors the term novel to something more precise than an ad hoc threshold. Tclin targets are proven; Tchem are novel but tractable; Tbio are novel with biology but hard to drug; Tdark are the ignorome. Pharos is freely available and publicly maintained."
        }
      },
      {
        "@type": "Question",
        "name": "What is the IDG initiative?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Illuminating the Druggable Genome (IDG) initiative is an NIH Common Fund program launched in 2014 to address the research bias in which roughly 75% of protein research focuses on the 10% of proteins known before the human genome was sequenced. IDG provides computational tools, target-development-level classifications, and targeted funding to increase scientific attention on understudied proteins, especially Tbio and Tdark targets. Its practical outputs for target-discovery practitioners include the Pharos portal, the TDL framework, and the TIN-X platform that quantifies (target × disease) pairs along novelty and importance axes. The underlying observation is that understudy can reinforce itself through the grant-funding feedback loop, which is why computational methods that substitute cheaply for experimental characterization shift the cost curve more for under-studied targets than for well-studied ones."
        }
      }
    ]
  }
---
A target-discovery lead gets two one-pagers. One covers a kinase, an enzyme class with many approved inhibitors already behind it. It already has three approved drugs, a decade of medicinal-chemistry papers, and six competing Phase 1 programs. The other covers a transcription factor - a protein class that is often harder to drug. It has no approved drug, no crystal structure, one mouse knockout paper, and no tool compound (no experimental molecule for probing the target directly). Which program gets funded? In most organizations, the kinase wins. The evidence base is deeper, the validation path is shorter, and the novelty story can be reconstructed later. This post asks how to *quantify* novelty, what the repurposing alternative actually costs, and where ML helps with either.

## Why drug target novelty matters in 2026

Target novelty matters because it sits alongside biomarker strategy as one of the few front-of-funnel choices that can materially change a program's odds. Target selection itself is the subject of [front-of-funnel decisions]({{ '/blog/2026/drug-target-discovery-phase-ii-failures/' | absolute_url }}). Biomarker stratification, covered in [likelihood of approval by therapeutic area]({{ '/blog/2026/likelihood-of-approval-therapeutic-area/' | absolute_url }}), roughly doubles approval odds. The 2011–2020 BIO / Informa Pharma Intelligence / QLS Advisors *Clinical Development Success Rates* data put **Phase I likelihood of approval for off-patent therapies at 14.7% versus 6.8% for novel therapies**. Off-patent here means programs built on drugs whose core patents have expired. Most of that gap appears in Phase III, where non-originator products - follow-on or reused therapies rather than brand-new ones - transitioned at 70.3% and novel products at 52.9%. Vaccines ran 9.7%, biologics 9.1%, new molecular entities (entirely new drugs) 5.7%, and biosimilars (the follow-on versions of biologic drugs) 32.3%.

> **Concept Translation:** The novel-vs-off-patent split is the drug-discovery version of an exploration-vs-exploitation trade-off. Off-patent / repurposing programs exploit known biology and known compounds at lower per-program cost and higher per-program success rate, but with crowded competition and limited upside. Novel-target programs explore - paying more for validation, accepting higher attrition, and reaching for the larger payoff that comes from being first to a target. Most portfolios mix both, and the mix is one of the more visible commercial decisions a research organization makes.

A second reason is structural. Over seventy-five percent of protein research still focuses on the ten percent of proteins known before the human genome was mapped. The skew reflects ease of work more than biological importance. Antibodies exist. Assays exist. Knockout mice exist. Crystal structures exist. Grant reviewers recognize the name. For the other ninety percent of proteins - the **ignorome**, the large pool of understudied proteins - little of that infrastructure is waiting for you. Recent ML gains in structure prediction, protein language models, and literature-scale NLP matter most here because they substitute computed evidence for missing infrastructure.

A third reason is NTRK. In 2018 the FDA approved larotrectinib (Vitrakvi, Bayer/Loxo Oncology) for any cancer driven by an NTRK gene fusion, a rearrangement that creates an abnormal TRK-family driver protein. It was the first tumor-agnostic targeted therapy - approval was tied to the molecular lesion rather than the tissue where the tumor started. Entrectinib followed in 2019 with broader spectrum activity; repotrectinib followed in 2023 with improved potency and activity against resistance mutations. The sequence is the commercial problem in miniature: a novel target, a first-in-class drug, and several approved drugs in the same class within five years. After the first-in-class drug lands, the target is no longer novel in the commercially useful sense. The window to own it is short.

## Two kinds of drug target novelty

<!-- FIGURE 1 - The Target Development Level (TDL) pyramid -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN19.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN19.png' | absolute_url }}" alt="Target Development Level pyramid: Tdark (ignorome), Tbio, Tchem, Tclin - the vertical gradient of target novelty and tractability." loading="lazy">
</picture>

A useful starting point is Agarwal's working definition, because it still shows up in platform documentation and industry decks. A **novel target** is a gene or protein with no approved-drug association. A **proven target** has at least one. In Agarwal's analysis of roughly a thousand drug targets, 247 were proven and 712 novel; more than half of the novel targets had no competitor programs, whereas nearly ninety percent of proven targets had at least one. Competition on novel targets increased as programs advanced through clinical trials, likely because early positive signal drew followers. At portfolio level, novelty correlates with solitude, and solitude carries commercial value.

The definition is useful, but it collapses very different situations. A protein with hundreds of papers, a crystal structure, knockout-mouse phenotypes, three failed clinical programs, and no approval is "novel" by Agarwal's definition. So is a protein with no papers, no structure, no knockout, no tool compound, and no drug-discovery history. Both are technically first-in-class opportunities. They do not require the same investment.

A more practical framework is the **Target Development Level (TDL)** classification from the NIH **Illuminating the Druggable Genome (IDG)** initiative, launched in 2014. The IDG Knowledge Management Center defined four categories.

- **Tclin.** Targets linked to at least one approved drug by mechanism of action - the drug's therapeutic effect is understood to run through that target. (Agarwal's "proven.")
- **Tchem.** Proteins known to bind small molecules with high potency - compounds can hit them strongly enough to be useful probes or starting points - but without approved-drug links. Small-molecule tool compounds exist; approval does not. Still "novel" in Agarwal's sense, but far from the ignorome.
- **Tbio.** Proteins with a confirmed Mendelian disease phenotype (where inherited variants in the gene cause a recognizable human disorder) or other biological evidence, but no demonstrated tractable chemistry - no convincing small-molecule starting point. "Novel" and biologically interesting; tools may be limited to genetic manipulation.
- **Tdark.** Proteins meeting none of the above. Minimal biological characterization, no tool compounds, often no crystal structure. The ignorome.

> **Concept Translation:** TDL is closer to a label-quality gradient than a binary class. Tclin proteins have the equivalent of fully labeled, audited training data: drugs, structures, assays, papers, mouse knockouts. Tdark proteins have almost nothing labeled at all. ML methods trained on protein-level features inherit this skew - performance is highest where the data is densest, lowest in the long tail. The novelty-vs-confidence trade-off below is partly the question of whether your team can *create* the missing labels for a Tbio or Tdark program before the budget runs out.

Moving from Tdark to Tclin usually means a decade and several hundred million dollars of infrastructure investment per target. In practice, the "novelty vs confidence" decision is usually a Tchem-versus-Tbio decision. Few organizations fund Tdark programs without some other reason to believe, and Tclin is already proven.

One IDG finding matters here. Tdark proteins receive less NIH funding than other categories, and the pattern reinforces itself: less funding yields fewer papers, which lowers priority in the next grant cycle. That is the computational-tractability story. If the ignorome is under-studied because it is under-resourced, then any method that substitutes cheaply for experimental characterization - predicted structures, NLP-aggregated literature, network-inferred functional context - shifts the cost curve more for Tbio and Tdark than for Tclin.

<!-- SEO §4 moderate: The trade-off nobody gets to dodge → The novelty trade-off nobody gets to dodge -->
## The trade-off nobody gets to dodge

<!-- FIGURE 2 - The novelty/confidence trade-off -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN20.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN20.png' | absolute_url }}" alt="Novelty–confidence trade-off: Tclin is crowded with low cost, Tdark is empty with high cost, Tchem is the operational sweet spot." loading="lazy">
</picture>

For any candidate target, novelty and confidence usually move in opposite directions. High-confidence targets are well studied, well characterized, and often already drugged. Validation costs are lower because many of the needed experiments have already been done somewhere. Competition is also higher: more organizations have programs, patents are crowded, and the commercial ceiling is divided. High-novelty targets reverse that profile. They demand more in-house validation and carry more biological risk, but they offer more commercial upside if the biology holds. In the Tchem-versus-Tbio decision, the key question is direct - how much of the target-validation burden does your team still have to carry itself?

Three patterns matter more in practice than they do on slides.

- **The validation cost of a Tbio target is frequently underestimated.** Teams look at the novel-target peak-sales story and forget that the tool-compound, pharmacokinetic/pharmacodynamic (PK/PD), and off-target profile work that comes free with a Tchem/Tclin target has to be rebuilt from scratch.

- **The competitive cost of a Tclin target is frequently underestimated.** Teams look at the proven-target LOA numbers and forget that the LOA is averaged across a crowd. The odds that *your* program, third-to-market, captures enough peak sales to justify R&D are not the class odds. That is why the BCR-ABL kinase-inhibitor space progressed from imatinib in 2001 through dasatinib, nilotinib, bosutinib, ponatinib, and asciminib, each positioned as an improvement on its predecessors and each competing for a smaller per-drug revenue share. Imatinib is a textbook first-in-class success story. It is also now generic, off-patent since 2015–2016, and no longer first-line in many cases.

- **"Novel" and "understudied" are not the same axis.** A protein can be proven in one disease (Tclin) and effectively novel in another. A kinase with approved inhibitors for oncology may have strong preclinical evidence in neurodegeneration and no programs targeting it there. The novelty framework needs to be applied at the (target × disease) pair level, not the target level alone. This is where the text-mining methods in the next section matter.

## Quantifying target novelty

Novelty is a continuum, so the practical question is how to measure it. The standard approach uses NLP over text-based evidence - publications, grants, clinical-trial registrations - to produce single-number scores that track a target's attention level in the scientific community.

The basic workflow is direct. Build a named-entity-recognition (NER) system that can identify gene, protein, disease, and drug names in biomedical text. Apply it to a corpus, typically PubMed, NIH RePORTER grant records, ClinicalTrials.gov trial registrations, and patent filings. For a candidate (target × disease) pair, count:

- **Publication volume.** How many papers mention this target in the context of this disease? Trend over time - is the area growing, flat, declining?
- **Funding signals.** How many grants are active on this target? Is NIH funding for this target growing relative to the field? Large, growing, well-funded areas are the opposite of ignorome.
- **Clinical-trial involvement.** How many trials reference this target directly or as a mechanism of action? In which phases? In which indications?
- **Drug-interaction evidence.** How many investigational or approved compounds are annotated as hitting this target? Any of them in the disease of interest?

> **Concept Translation:** Novelty scoring is information retrieval over the scientific corpus, with the target as the query and "attention paid to it" as the relevance signal. Most practical implementations are a layered NER + relation-extraction pipeline followed by aggregation. From an LLM perspective, this is exactly the territory modern biomedical language models - BioBERT, PubMedBERT, BioGPT, and successors - are pretrained for. The scores that come out are corpus-attention summaries, not biological judgments. They tell you how much the field is paying attention to a target, which is informative but not equivalent to "is this target real?"

Two database patterns come up repeatedly for this kind of work. The **TIN-X** platform from the IDG consortium quantifies (target × disorder) pairs along two axes: a **novelty index** (a publication-scarcity score) and an **importance index** (which measures how strongly the literature links that target to a specific disorder). The scatter of targets in novelty-importance space gives you the portfolio view. Well-studied important targets are crowded, well-studied unimportant targets are dead ends, under-studied important targets are the opportunity, and under-studied unimportant targets are probably in the ignorome for good reason.

> **Concept Translation:** TIN-X reduces every (target × disease) pair to a 2D point. The plot is a portfolio embedding - you can see at a glance which corner the candidate sits in, and where the unworked opportunities cluster. The same kind of low-dimensional projection that ML practitioners use to inspect representation spaces (UMAP, t-SNE on learned embeddings) maps onto a real product question here: where on the plot do programs that pay off live, and which corner does this candidate occupy?

The **NER-plus-RE** components underlying this work - named-entity recognition plus relation extraction - are useful but still imperfect. Biomedical named-entity recognition reaches about 90% F-score in benchmarks for well-structured entity types (gene, disease, chemical), where F-score is the standard balance of precision and recall. Relation extraction for claims such as "drug X binds target Y with Kd Z" sits closer to 50% F-score. The asymmetry matters for novelty scoring. Counting publications and extracting entities is tractable; extracting structured claims about target-disease mechanisms is where errors still accumulate.

LLM-based methods have moved the RE frontier since 2023, with transformer-based relation-extraction systems - typically fine-tuned BERT-family or domain-pretrained biomedical LLMs - now deployed in several commercial and open-source target-discovery pipelines. 

Quantified novelty is decision support. A target that scores "low publication volume, high disease-association evidence in genetics" is genuinely interesting (the structured frameworks for [evidence frameworks for target-disease linkage]({{ '/blog/2026/target-disease-association-evidence/' | absolute_url }}) are the subject of the companion post). A human reviewer still has to read the papers to confirm that the NLP has not confused gene-symbol ambiguities, missed a key negative result, or counted reviews as primary papers. The scores compress the literature. They do not conclude.

## Drug repurposing as the opposite axis

Novel-target discovery asks "can we find new biology to drug?" Drug repurposing asks "can we find new diseases for chemistry we've already validated?" The problems are asymmetric. Repurposing starts with an approved or well-characterized compound and searches across diseases; novel-target discovery starts with a disease and searches across targets. The intersection is direct: by the Agarwal definition, the *target* of a repurposed drug is already proven because the protein already has an approved-drug association. The novelty sits in the indication.

Repurposing has been sold as cheaper and faster for a decade. The claim is directionally right, but it leaves out structural costs. Roughly one-third of recent drug approvals have been repurposing-adjacent, and the Phase I LOA advantage over novel is meaningful, with the largest separation at the Phase III transition (70.3% for non-originator products vs 52.9% for novel). Those advantages do not erase the following costs.

- Bringing a repurposed compound to market still runs to hundreds of millions or low billions of dollars. Preclinical-research savings help, but they do not carry the later-phase load. Repurposed compounds still go through the same regulatory path as novel ones.
- Out-licensing an existing compound for a new indication carries "in-kind" costs - remanufacturing active product and placebo, compiling new study reports, and establishing pharmacovigilance (ongoing safety monitoring) for a new indication. Academic repurposing advocates often underestimate those costs.
- IP and regulatory exclusivity are weaker for new indications than for new molecules. The **US 505(b)(2) pathway** - a regulatory route that lets sponsors rely partly on prior evidence for an already approved drug - typically secures three to five years of market exclusivity, versus five years of new-chemical-entity exclusivity on the 505(b)(1) pathway used for novel molecules. For indication-only repurposing claims (where the same molecule is already approved for a different use and is now claimed for a new disease), exclusivity is usually at the lower end of that range. **Skinny labelling** - the practice of a generic manufacturer launching without the new indication on the label and thereby avoiding patents that cover only that indication - further weakens the sponsor's position. The legal and commercial landscape around skinny labelling continues to evolve.
- Patents for repurposing-specific indications are harder to obtain and often expire in inconvenient windows. The common pattern is that the most valuable repurposing discoveries happen *after* the original patent expires, which is exactly when commercial protection is weakest.
- Pharmaceutical organizations often decline repurposing opportunities that don't align with core therapeutic areas, and almost always decline opportunities in compounds they've previously discontinued. These are organizational constraints, not scientific ones, and they stay constant regardless of how good the computational repurposing signal is.

> **Concept Translation:** 505(b)(2) is recognizable as fine-tuning rather than training from scratch. The full 505(b)(1) NDA path is the equivalent of training a new model end-to-end on a fresh problem - every safety dataset, every dose-finding study, every preclinical model has to be rebuilt. 505(b)(2) lets the sponsor reuse the prior approval as a frozen backbone and add a smaller "scientific bridge" study, typically a pharmacokinetic comparison, to fit the new claim. The cost reduction is roughly the gap between training a 70B model from scratch and fine-tuning one for a new task: large, but not as large as the headline numbers suggest, because the downstream regulatory infrastructure still has to be built.

Seen in concrete terms, "cheaper and faster" buys a specific regulatory shortcut. The 505(b)(2) pathway, established by the Hatch-Waxman Amendments of 1984, allows the FDA to rely on existing safety and efficacy data - including published literature and prior FDA findings on a Reference Listed Drug (the previously approved product that anchors the comparison) - so long as a scientific bridge such as a pharmacokinetic study connects the new use to the established record. Development through approval via 505(b)(2) typically runs three to eight years and roughly $8 million to $200 million. A full 505(b)(1) NDA - a new drug application for a fully new product - typically runs ten to fifteen years and $1 billion to $2.2 billion. That is a 70–90% reduction in out-of-pocket capital expenditure, with three to five years of market exclusivity at the end. 505(b)(2) approvals routinely exceed forty per year and peaked at sixty-eight in 2020, often outnumbering new molecular entities approved via 505(b)(1). One caveat remains: FDA *review* time for a 505(b)(2) submission can exceed that of an NME because evaluating the scientific bridge between old and new data creates its own regulatory burden. The development calendar often shrinks. The regulatory calendar does not always follow.

These frictions explain why the biggest repurposing success stories tend to be atypical. Massive unmet need creates market-making urgency (AZT in early HIV, remdesivir in COVID-19); a side effect eclipses the original indication (Viagra); or a mechanistic insight opens a distinct indication for an off-patent drug (thalidomide in erythema nodosum leprosum, then multiple myeloma). The ordinary case - a statistically significant signal in a computational repurposing screen without unusual market dynamics - often fails the business-case analysis even when the science is sound.

## Methods for computational drug repurposing

If the goal is to predict new disease-drug pairings systematically, current pipelines usually fall into three methodological families.

**Structure- and similarity-based methods.** Molecular docking against alternative targets, pharmacophore matching (which compares the 3D binding features a molecule presents rather than its exact structure), and fingerprint-based similarity to drugs with known activity in a target disease. The classical ML framing here is nearest-neighbor retrieval in chemical or target space - an approved drug whose structure or induced transcriptomic profile resembles that of a known therapeutic for disease *X* is a repurposing candidate for *X*.

**Genetic-association and omics-based methods.** Compounds whose target list overlaps with disease-associated loci (from GWAS, rare-variant analysis, or differential-expression studies) are candidates for repurposing into that disease. Connectivity-map methods compare the gene-expression changes caused by a drug with the changes seen in disease and look for reversals - the canonical ML instantiation of this and the single most cited ML method in drug repurposing.

> **Concept Translation:** The Connectivity Map / L1000 framing is signature matching in transcriptomic space. Every drug perturbation produces a characteristic gene-expression vector - a "signature" - and every disease state produces another. A drug whose signature is *anti-correlated* with the disease signature is a candidate for treating that disease, on the heuristic that reversing the disease's transcriptional state may reverse the disease itself. Mechanically, this is nearest-neighbor in a high-dimensional vector space with a sign flip, exactly the kind of retrieval problem that contrastive learning is built for.

**Network-based methods.** Biomedical knowledge graphs encoding drug-target, target-pathway, target-disease, and pathway-disease relationships allow repurposing to be formulated as a link-prediction or proximity problem. The model either predicts useful missing links in the graph or asks which drugs sit closest to the disease module in network space. Drugs "close" to a disease in that sense - whether close is measured by random walks, network diffusion, or learned embeddings - are candidates.

All three families lean on unsupervised and semi-supervised ML because labeled examples are scarce. You have lots of unlabeled structural data, lots of unlabeled transcriptomic profiles, and a few thousand confirmed drug-disease pairs. The standard move is to learn representations in which similar things cluster, then use sparse labels to rank. This is the frame *Build AI Drug Discovery Pipelines* Chapter 7 takes up in detail, with drug repurposing as the running example.

## Databases that wire drugs and targets together

Three databases recur in the drug-target querying that any novelty or repurposing workflow needs.

**DrugBank.** Searchable by drug or target, returning interactions, chemical properties, mechanism of action, related diseases, clinical-trial status, and brand names. Basic search is free; advanced query and bulk download require a license, with free academic licenses available. DrugBank's strength is the curation quality on approved drugs and late-stage candidates.

**Pharos** (the public portal for IDG data, funded by the NIH Common Fund). Searchable by target, drug, or disease, with target pages that include the TDL classification, tissue expression across healthy human tissues, protein structure when available, associated drugs, and pathway memberships. Pharos is the canonical source for the Tclin/Tchem/Tbio/Tdark categorization and is freely available. For any novelty-scoring workflow that wants to anchor "novel" to something other than ad-hoc thresholds, the TDL assignment from Pharos is the standard reference.

**DGIdb** (Drug-Gene Interaction Database). Organizes the druggable genome into two classes: genes with known drug interactions, and genes that are potentially druggable. The second class is particularly useful for prioritizing gene lists from omics studies by which ones have a plausible path to small-molecule tractability. Publicly available, free to download.

For a practitioner-built novelty scoring pipeline, the useful pattern is to join across all three: DGIdb for the druggable-genome filter, Pharos for the TDL assignment, and DrugBank for the approved/investigational drug inventory. Layer PubMed, NIH RePORTER, and ClinicalTrials.gov on top for the text-signal component. These are mature components, and most real pipelines depend on them.

## A worked example in network-based drug repurposing for SARS-CoV-2

<!-- FIGURE 3 - The SARS-CoV-2 network-repurposing worked example -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN21.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN21.png' | absolute_url }}" alt="Network-based SARS-CoV-2 repurposing: 6,340 drugs ranked, 62% hit rate on top candidates, 76 of 77 worked via indirect host pathways." loading="lazy">
</picture>

An early-pandemic SARS-CoV-2 study gives a concrete view of computational repurposing at scale. Researchers combined three data sources - the human protein-protein interaction network (the "interactome"), experimentally characterized SARS-CoV-2 viral target interactions, and drug-target interaction data - and used network-diffusion and network-proximity algorithms (which score how near a drug's targets sit to disease-relevant proteins in the network) to rank 6,340 approved and investigational drugs by expected efficacy against SARS-CoV-2.

The ranking was then tested experimentally in human cells. The top-ranked drugs showed a 62% success rate in reducing viral infection. Of the six drugs that were effective, four could be directly repurposed for COVID-19 treatment. The more striking result was that **seventy-six of the seventy-seven drugs that reduced viral infection did not bind to proteins targeted by SARS-CoV-2** (primary paper: Morselli Gysi et al., *PNAS* 118(19):e2025581118, 2021). The efficacy came from indirect, network-based mechanisms - perturbations to host pathways that happen to be close in network space to viral-target pathways, rather than direct antiviral activity in the classical sense.

> **Concept Translation:** Network proximity is graph-based propagation rather than 1:1 binding. A drug "near" a disease in network space is one whose protein targets share many shortest paths with the disease's known protein targets. The propagation is computed as a random walk, a Laplacian smoothing, or a learned graph-embedding distance - different algorithms, same intuition. The mechanism of action *can be entirely indirect*: the drug perturbs a host protein that is in the right neighborhood of the viral-target proteins, and the perturbation ripples through the network. A classical docking screen would never find these candidates because they don't bind the obvious targets.

Two points matter.

First, the hit rate is high relative to a naïve virtual screen (a broad in silico ranking of compounds with little biological context). The network-proximity frame encodes a prior - drugs already approved for other indications have cleared a basic tractability bar. Restricting the search space to those compounds and ranking by network relevance to the target biology concentrates candidates on the right side of that bar. That is why repurposing can work computationally even when it fails commercially.

Second, the network result distinguishes repurposing as target identification from repurposing as drug matching. A classical docking-based screen looks for drugs that bind viral proteins. A network-diffusion screen finds drugs that perturb host pathways whose topology matters for viral infection - a different mechanism, and one that a target-centric analysis would easily miss. For an ML practitioner entering drug discovery, the lesson is direct: the representation choice - chemical similarity, network proximity, or transcriptomic signature - encodes a hypothesis about mechanism. Repurposing screens are strongest when they triangulate across representations.

## The NTRK case when novelty works

<!-- FIGURE 4 - The NTRK novelty half-life timeline -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN22.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN22.png' | absolute_url }}" alt="NTRK novelty half-life: larotrectinib 2018, entrectinib 2019, repotrectinib 2023 - three approved drugs, one class, five years." loading="lazy">
</picture>

Imatinib succeeded as the first BCR-ABL inhibitor because CML (chronic myeloid leukemia) was a rapidly fatal disease with few good alternatives; the rational kinase-inhibitor paradigm it validated then took two decades to spread across other kinases. The more recent parallel is NTRK.

The target-discovery rationale for NTRK was unusually clean. In a subset of cancers across multiple tissues, a gene fusion produces a TRK-family protein that is constitutively active and functions as a driver. Patients identifiable by a single molecular criterion - NTRK fusion detectable by IHC (immunohistochemistry) or NGS (next-generation sequencing) - share a common therapeutic vulnerability across many tumor histologies. Larotrectinib's 2018 approval marked the first tumor-agnostic targeted therapy. Entrectinib followed in 2019 with a broader spectrum (ROS1 fusions as well as NTRK); repotrectinib followed in 2023 with improved potency and resistance-mutation coverage (activity against variants that emerge after treatment with earlier drugs). Within five years of first-in-class approval, the class had three approved drugs.

The NTRK arc is a case study in novelty half-life. Larotrectinib's team owned a genuinely novel target-disease linkage for a narrow window. Once the tumor-agnostic framing proved out regulatorily, the competitive landscape tightened quickly. Entrectinib had been in clinical development before larotrectinib's approval, and repotrectinib was engineered specifically to address resistance mutations that emerge on the earlier agents. By 2026, NTRK-fusion oncology is no longer a first-in-class opportunity for new entrants; the novelty lives in resistance mechanisms, new fusion partners, and non-oncology TRK indications that remain lightly explored.

Cross-cancer analysis is the computational work that keeps tumor-agnostic programs coherent. It assembles expression and genomic data across TCGA (The Cancer Genome Atlas) and similar pan-cancer compendia to identify which molecular lesions recur across tissues and which do not. NTRK would not be the NTRK story without a decade of pan-cancer sequencing work laying that groundwork. The generalizable point for target-novelty reasoning is that the lesion-centric view, organized around the molecular abnormality itself, often outruns the tissue-centric view in finding novel-but-tractable therapeutic categories. Pan-cancer analysis is the computational engine for finding the next NTRK.

## What's next in drug target novelty

**The Tdark problem remains open.** Every infrastructure advantage that makes Tclin targets easy to work on - crystal structures, tool compounds, knockout models, antibodies - was built over decades at enormous cost. Protein-language-model embeddings, AlphaFold-class structure prediction, and NLP over sparse literature are the field's cheaper substitutes. The operational question for the next few years is whether those substitutes are *good enough* to de-risk Tdark programs until they compete with Tchem programs on expected value.

**Repurposing is stronger as a computational problem than as a commercial one.** Every methodological advance in computational repurposing produces more candidates than the industry funds. The bottleneck is structural - patents, exclusivity, skinny labelling, and organizational fit. A less explored research direction is program design that works *with* that commercial reality. Rare-disease orphan-drug programs, neglected-tropical-disease partnerships, and academic-industry hybrid models are common proposals; none has yet produced the volume of repurposing approvals that the computational hit rates would suggest.

**LLM-based literature intelligence is changing novelty scoring faster than the surrounding tooling.** NER and relation extraction on biomedical text are substantially more accurate now than they were when the IDG TDL system was first operationalized. The open question in 2026 is whether that translates into *better target nominations* or only *larger target-evidence databases*. The risk is familiar - higher-recall text extraction can produce confident-looking summaries of uncertain or contradictory evidence. Explicitly flagging what the ML does not know will matter more than pushing raw scores higher.

**Novelty scoring shares the validation problem of the rest of target-discovery ML.** The ground truth for "was this a good novel-target nomination?" arrives as Phase III readout a decade later. Retrospective benchmarks are biased toward targets that entered pipelines, and failed targets get less documentation than successful ones. Prospective benchmarks are limited by timescale. Until target-discovery ML has something like the PDBbind / CASP benchmark - a widely accepted held-out benchmark set or community challenge for the task that actually matters - the discipline will remain calibrated as much by industry credibility as by methodology papers. That is a property of the field, not of any specific method.

The common commitment underneath these methods is compression. Every credible target-novelty score is a summary of what the literature collectively knows, and every credible repurposing candidate is a summary of what chemistry has already paid to validate. The ML's job is to make those summaries trustworthy enough for a program committee to act on them. That is a narrower claim than the usual "AI-discovered novel target" narrative. It is also closer to what target-discovery ML actually does well.

---

## Further reading

- Agarwal, P. (circa 2013–2016). *Novel vs proven drug targets: portfolio-level analysis of ~1,000 targets.* [doi:10.1038/nrd4089](https://doi.org/10.1038/nrd4089) The foundational portfolio-level analysis that defines "novel" as a gene/protein with no approved-drug association and quantifies the novelty-vs-competition relationship across ~959 analyzed targets. Source for the 247 proven / 712 novel split, the >50% competitor-free rate among novel targets, and the >90% competitor-present rate among proven targets.

- NIH Illuminating the Druggable Genome (IDG) initiative. *Pharos: the IDG Knowledge Management Center portal.* [URL: https://pharos.nih.gov/]. The canonical public portal for Target Development Level (TDL) classifications (Tclin, Tchem, Tbio, Tdark), target-level aggregation of biological and pharmacological data, and the IDG's understudy-bias framing. For the canonical academic references, see Nguyen et al., *Nucleic Acids Research* database issue (multiple years - search "Pharos IDG Nucleic Acids Research database issue" for the most recent), and the 2014 IDG launch paper (search "Illuminating the Druggable Genome 2014 launch Nature Reviews Drug Discovery OR Nature Chemical Biology").

- Morselli Gysi, D., do Valle, Í., Zitnik, M., Ameli, A., Gan, X., Varol, O., Ghiassian, S. D., Patten, J. J., Davey, R. A., Loscalzo, J., Barabási, A.-L. (2021). *Network medicine framework for identifying drug-repurposing opportunities for COVID-19.* *Proceedings of the National Academy of Sciences* 118(19):e2025581118. DOI: 10.1073/pnas.2025581118. The primary source for the SARS-CoV-2 network-medicine worked example: ranked 6,340 approved and investigational drugs by network-diffusion / network-proximity scores, experimentally validated 918 in VeroE6 cells, and produced the 62% top-rank hit rate and the 76-of-77 indirect-mechanism finding. The methods section also documents the three-pipeline framework (AI, network diffusion, network proximity) the draft summarizes.

- Pushpakom, S., Iorio, F., Eyers, P. A., Escott, K. J., Hopper, S., Wells, A., Doig, A., Guilliams, T., Latimer, J., McNamee, C., Norris, A., Sanseau, P., Cavalla, D., Pirmohamed, M. (2019). *Drug repurposing: progress, challenges and recommendations.* *Nature Reviews Drug Discovery* 18:41–58. [URL: https://doi.org/10.1038/nrd.2018.168]. The most-cited general-audience review of drug-repurposing methodology. Source for the three-family framing of computational repurposing methods (structure/similarity, genetic/omics, network) that the draft's Methods section extends, and for the commercial-versus-computational tension the post's "Drug repurposing as the opposite axis" section takes up. **Important pairing for the "one-third of recent approvals are repurposing-adjacent" claim** - the specific fraction depends heavily on counting methodology; Pushpakom gives the operational definition and supporting counts for that framing.

---
