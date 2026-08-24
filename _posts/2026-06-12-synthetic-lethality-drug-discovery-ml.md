---
layout: "post"
title: "Synthetic lethality and combination targets: ML methods for finding drug pairs that work together"
date: "2026-06-12 09:00:00-0700"
description: "Synthetic lethality turns a drug-target problem into a target-pair problem. Which ML methods find the pairs? CRISPR screens, DAISY, SynLethDB, and GNN link prediction."
tags:
  - "machine learning"
  - "drug discovery"
  - "target discovery"
  - "oncology"
categories:
  - "target discovery"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/blog/target-discovery/APPH_FLYNN_UN27.png"
og_image: "https://noahrflynn.com/assets/img/blog/target-discovery/APPH_FLYNN_UN27.png"
series: "Drug Target Discovery"
series_order: 7
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is synthetic lethality?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Synthetic lethality is a relationship between two genes in which loss of either gene alone is survivable, but loss of both together kills the cell. In cancer, one of those losses is often already present as a tumor mutation, and the other is induced pharmacologically by a drug. The classical example is PARP inhibition in BRCA-mutant tumors, which exploits the synthetic-lethal relationship between PARP1 and BRCA1/2 to kill tumor cells and spare healthy tissue. Synthetic lethality is the foundation of biomarker-stratified, mutation-targeted oncology drug development. The 2022–2023 FDA narrowing of advanced-ovarian-cancer indications for olaparib, niraparib, and rucaparib, in response to mature overall-survival data, sharpened the discipline: synthetic-lethal logic holds within the genetic background it predicts, and broader use must be supported by mature OS data, not surrogate endpoints alone."
        }
      },
      {
        "@type": "Question",
        "name": "How do CRISPR screens find synthetic-lethal pairs?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Pooled CRISPR screens deliver a library of 60,000 or more guide RNAs into a cancer cell line, often one carrying a defined mutation such as BRCA1-null. The cell population is split between treated and control arms, and after a fixed number of doublings the guide-RNA pool is sequenced. Guides whose targets are essential under the test condition become depleted in the treated arm, identifying synthetic-lethal partners. The standard analytical pipeline, MAGeCK, normalizes guide counts, models them with a negative binomial distribution, and aggregates per-guide signal to per-gene scores. Variants such as CRISPRi (transcriptional repression rather than DNA cutting), combination screens (two guides per vector), and Perturb-seq (single-cell readout of perturbations) extend the basic design. CRISPR screens are the experimental gold standard but expensive and reproducibility-limited across labs, so computational SL prediction is used to prioritize candidates before screening."
        }
      },
      {
        "@type": "Question",
        "name": "What is MAGeCK?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "MAGeCK (Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout) is the standard statistical pipeline for analyzing pooled CRISPR screens. It normalizes guide-RNA read counts across samples, models counts with a negative binomial distribution, tests each guide for differential abundance between treatment and control arms, and aggregates guide-level signals to gene-level scores using a rank-based test. The output is a per-gene score with p-value and false-discovery rate, plus pathway-level enrichment. For ML, MAGeCK is the step where raw CRISPR-screen data becomes a labeled dataset suitable for downstream classifiers. The depleted-gene list becomes the positive class for supervised synthetic-lethal prediction models."
        }
      },
      {
        "@type": "Question",
        "name": "How do you predict drug synergy?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Drug synergy prediction models take pairs of molecules and a cell-line context, then predict whether the pair's combined effect exceeds the sum of its single-agent effects. Features typically include chemical-structure descriptors, known target profiles, and cell-line molecular context such as mutation, expression, copy number, and subtype membership. Model families range from traditional methods like SVMs and random forests with QSAR-style features to deep neural networks on molecular fingerprints and omics, and graph neural networks on drug-target-cell interaction graphs. The problem is imbalanced: in a published 2,025-pair screen against 125 cancer cell lines, only about 5.2% of pairs showed synergy. That requires class-imbalance-aware training and careful evaluation on metrics like AUPRC and top-K precision. Context matters more than chemistry. The same pair is often synergistic in one cell line and antagonistic in another, so models conditioned on cell-line molecular context outperform pan-tissue models on clinically useful benchmarks."
        }
      },
      {
        "@type": "Question",
        "name": "What is SynLethDB?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "SynLethDB is a curated synthetic-lethality knowledge graph that aggregates experimental and computational evidence for candidate synthetic-lethal gene pairs across multiple species. It stores pairs as edges in a graph structure, with nodes representing genes and edges annotated by the supporting evidence type, including CRISPR screens, RNAi screens, computational prediction, and literature-derived evidence. For a practitioner planning a new screen or running an in-silico SL prediction, SynLethDB is the first resource to check for prior supporting evidence. Methodologically, it sits at the intersection of synthetic-lethality prediction and biomedical knowledge graphs. The same graph-representation-learning and link-prediction methods used on target-disease knowledge graphs also apply to SynLethDB."
        }
      },
      {
        "@type": "Question",
        "name": "Why did PARP inhibitors work?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "PARP inhibitors work in BRCA-mutant cancers because of synthetic lethality between PARP1 and BRCA1/2. In a BRCA-wildtype cell, homologous-recombination repair handles DNA double-strand breaks whether or not PARP1 is active, so inhibiting PARP1 is tolerable because the backup pathway works. In a BRCA-mutant cancer cell, homologous recombination is crippled and the cell depends on PARP1-mediated repair to prevent replication-fork collapse. Block PARP1 and the BRCA-mutant cell accumulates lethal double-strand breaks it cannot repair, and healthy BRCA-wildtype cells tolerate the same drug. This mechanism gave the first PARP inhibitors, olaparib in December 2014 and then rucaparib, niraparib, and talazoparib through 2018, tumor-selective efficacy tied to a companion diagnostic identifying BRCA-mutant patients. It was the first clinical validation of a synthetic-lethal drug class. The class remains approved, but the FDA narrowed or withdrew six advanced-ovarian-cancer indications across olaparib, niraparib, and rucaparib in 2022–2023 after mature overall-survival data showed detriment in non-BRCA-mutant populations. Surviving recurrent-EOC maintenance indications were restricted to confirmed deleterious BRCA mutations. The next-wave DNA-damage-response inhibitors, including Polθ and USP1, are aimed at residual resistance in the same setting, and WRN inhibitors extend synthetic-lethal logic to MSI-H/dMMR tumors."
        }
      },
      {
        "@type": "Question",
        "name": "What are WRN inhibitors and why do they work in MSI-H cancers?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "WRN (Werner syndrome RecQ helicase) is a DNA helicase essential for genome maintenance during replication. In tumors with microsatellite instability and defective mismatch repair (MSI-H/dMMR), which are common in colorectal, gastric, and endometrial cancers, loss of mismatch repair leaves cells dependent on WRN to resolve the replication stress and secondary-structure problems generated by microsatellite-unstable DNA. Inhibiting WRN in this background induces catastrophic genomic instability and tumor-cell death, and healthy mismatch-repair-proficient tissue tolerates the same inhibition because mismatch repair handles the underlying problem. WRN was identified as a top synthetic-lethal target in MSI-H/dMMR cancers through large-scale functional-genomics screens (Project Score and others) in the late 2010s. As of 2026, three small-molecule WRN inhibitors are in clinical development: Novartis's HRO761 (Phase 1/1b NCT05838768, MSI-H/dMMR solid tumors, ESMO 2025 update), Nimbus's NDI-219216 (Phase 1/2 dose escalation completed ahead of schedule with no DLTs and no MTD reached), and Nimbus's follow-on NTX-452 (FIH studies began 1H 2025)."
        }
      }
    ]
  }
---
Consider a cancer cell with a broken *BRCA1* gene. Losing BRCA1 alone does not kill the cell because a backup DNA-repair pathway still functions. Inhibit PARP1 in a healthy cell, and it survives for the same reason: BRCA1 remains intact. Put those two conditions together in a BRCA-mutant tumor treated with a PARP inhibitor, and the cell dies. Neither hit is lethal alone. The combination is. That is synthetic lethality. In oncology, it has been one of the most productive target-discovery ideas of the past two decades. For machine learning, it creates a problem with clear labels and a tractable search space.

> **Concept Translation:** Synthetic lethality is a context-conditional prediction problem. The label "lethal" is not a property of either gene alone - it's a property of the pair, conditioned on a genetic background. The ML framing is closer to a logical AND on two perturbations than to a continuous dose-response curve. The search space, the label structure, and the evaluation protocols look different from the rest of target discovery: you're not asking "is this gene a good target?" but "is this gene a good target *given* that gene B is already broken?"

## Why synthetic lethality matters for drug discovery in 2026

Synthetic lethality has moved from biological observation to clinical strategy. The first-generation PARP inhibitors form a real class: olaparib, rucaparib, niraparib, and talazoparib were approved between 2014 and 2018, generated real revenue, and exposed two problems the field has spent the early 2020s trying to solve.

The first is **acquired resistance**. Tumors revert BRCA mutations. Some restore homologous recombination, the cell's high-fidelity pathway for repairing double-strand DNA breaks. Others adapt replication-fork protection, the machinery that keeps DNA replication from collapsing under stress. Progression-free-survival gains attenuate over time. This is the resistance story most discussions of PARP inhibitors focus on.

The second is **biomarker discipline**. Mature randomized data through 2022 and 2023 made the point more sharply. In advanced epithelial ovarian cancer, four randomized controlled trials with long enough follow-up to read out overall survival (OS, time until death from any cause) showed that earlier progression-free-survival (PFS, time until the cancer grows or the patient dies) gains in less tightly selected populations did not translate to OS. In several non-BRCA-mutant arms, patients on PARP inhibitors died sooner than controls. Between late 2022 and late 2023, the FDA withdrew or narrowed six advanced epithelial ovarian cancer indications across olaparib, niraparib, and rucaparib; the surviving maintenance indications in recurrent ovarian cancer (use after an initial response to keep the disease under control) were restricted to patients with confirmed deleterious BRCA mutations, with manufacturers issuing "Dear Healthcare Provider" letters to clinicians (ASCO and SGO summaries of the FDA revisions, 2022–2023). The class works in the subgroup the synthetic-lethal argument identifies. Broaden the indication on the strength of a surrogate endpoint - an earlier readout used in place of survival - and mature OS data can reverse the story. That lesson now sits near the center of any serious synthetic-lethal drug program.

A second wave of DNA-damage-response inhibitors is aimed squarely at those residual problems. Two programs return to the same BRCA-deficient setting from different angles. Artios Pharma's **ART6043**, a DNA polymerase θ (Polθ) inhibitor, received FDA Fast Track designation on February 23, 2026 for germline BRCA-mutant HER2-negative breast cancer (patients who inherit a BRCA mutation and whose tumors do not overexpress HER2), and is launching a global randomized Phase 2 in combination with olaparib (Artios Pharma press release, Feb 23, 2026; ongoing Phase 1/2a NCT05898399). KSQ Therapeutics' USP1 inhibitor **KSQ-4279** (also reported as RO7623066 / RG6614 under a Roche partnership announced July 2023) completed first-in-human Phase 1 testing with anemia as the principal dose-limiting signal (Yap et al., 2024 ASCO Annual Meeting, abstract 3005; NCT05240898). A competing USP1 program, TNG348, was terminated in May 2024 for liver toxicity, with Grade 3/4 liver-function abnormalities observed in patients who remained on study longer than eight weeks (Tango Therapeutics press release, May 23, 2024; Phase 1/2 NCT06065059). That is a reminder that correct biology does not guarantee a drug-like molecule.

A third program reaches a different genetic context. **WRN** (Werner syndrome RecQ helicase) is synthetic-lethal in tumors with microsatellite instability and defective mismatch repair (MSI-H/dMMR) - tumors that fail to correct copying mistakes in repetitive DNA and therefore accumulate unstable short repeats. That population includes a substantial fraction of colorectal, gastric, and endometrial cancers. WRN inhibitors entered the clinic over 2024–2025, and three programs have made the most progress: **NDI-219216** (Nimbus Therapeutics), a non-covalent oral WRN inhibitor that completed Phase 1/2 dose-escalation roughly nine months ahead of schedule with no dose-limiting toxicities and no maximum tolerated dose reached; **HRO761** (Novartis), a first-in-class oral non-covalent WRN inhibitor with an ongoing Phase 1/1b trial (NCT05838768) in MSI-H/dMMR solid tumors that presented favorable safety and encouraging antitumor activity at ESMO 2025; and **NTX-452** (Nimbus), a follow-on candidate with preclinical complete-response data that began first-in-human studies in the first half of 2025 (Nimbus and Novartis disclosures; ESMO 2025 abstracts). WRN is the clearest post-BRCA-PARP program the field has produced so far: a different genetic vulnerability, a different biomarker, the same synthetic-lethal logic.

There is also a methods story underneath the clinical one. Synthetic-lethality target identification has become one of the most data-rich sub-problems in target discovery. CRISPR screens generate gigabytes of guide-RNA count data per campaign. Drug-combination screens evaluate thousands of pairs against hundreds of cell lines. The raw material for supervised classification, unsupervised community detection, and link prediction is already there. This post is about what that methods stack actually looks like.

## What synthetic lethality means

<!-- FIGURE 1 - The synthetic-lethality concept (2×2 conceptual figure, Portage editorial style) -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN27.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN27.png' | absolute_url }}" alt="Four-panel figure of synthetic lethality: healthy cells survive single-gene loss, but tumor cells that have already lost one partner gene die when the second is inhibited." loading="lazy">
</picture>

The textbook definition is a pair of genes whose simultaneous inactivation kills the cell, but loss of either gene alone does not. In the usual diagram, gene A and gene B perform redundant or parallel functions. Lose A and B compensates. Lose B and A compensates. Lose both, and compensation fails.

In cancer, one of those two losses is often already present. The tumor has disabled gene B through somatic mutation, copy-number loss, or epigenetic silencing. A drug that inhibits gene A now hits a vulnerability found in the cancer cell but not in the patient's healthy tissue. That selective window is why synthetic lethality matters as a target-discovery strategy rather than only as a combination-therapy strategy. It offers a way to drug targets that would otherwise be too toxic systemically, because the liability appears only in the mutant background. The PARP-inhibitor regulatory recalibration of 2022–2023 is the reminder that this logic holds only inside the genetic background it predicts. Drift outside that background, and benefit can turn to harm.

Drug synergy is a different problem: it asks whether two drugs together produce more effect than the sum of their individual effects. Synthetic lethality asks whether losing one intact gene is lethal when another is already broken. The former is a pharmacological question; the latter is a genetic one. They meet in the clinic. A PARP inhibitor in a BRCA-mutant tumor exploits a genetic synthetic-lethal relationship and shows single-agent efficacy. The methods used to find synergy and synthetic lethality differ, so I treat them separately below.

### Why cancer is the natural hunting ground for synthetic lethality

Most clinically validated synthetic-lethal pairs sit in DNA damage repair: PARP1 with BRCA1/2, Polθ with BRCA1/2, USP1 with BRCA1/2, WEE1 with TP53-mutant backgrounds, ATR with ATM-deficient backgrounds, and WRN with MSI-H/dMMR backgrounds. This concentration is not accidental. Cancer cells accumulate mutations at far higher rates than normal tissue because they have already broken, at least in part, one or more of the pathways that repair damage. That breakage fuels the oncogenic mutational trajectory *and* creates dependencies on whatever parallel repair machinery remains intact. Hit the remaining machinery, and the tumor's own mutability kills it.

Outside DNA repair, the synthetic-lethal network is less well charted. That gap is both a problem and an opportunity for ML.

## The target–target problem

Most of this series asks "is this the right target?" That is a target–disease question. Synthetic lethality is different: the answer to "is target A worth developing?" depends on whether some other target B is already broken in the patient's tumor. It is a target–target problem, and it reshapes what target discovery means.

Practically, this has three consequences.

**The candidate pool is combinatorial.** For ~20,000 protein-coding genes, there are ~200 million unordered pairs. Genome-scale screening of pairs remains expensive, especially compared with single-gene essentiality screens, which are now routine. That cost is why computational prioritization exists.

**The biomarker is central, and the bar is rising.** A PARP inhibitor in a BRCA-wildtype tumor does very little, and the FDA's 2022–2023 narrowing of the ovarian-cancer indications across olaparib, niraparib, and rucaparib formalized the principle: when mature OS data did not support broader use, the indication snapped back to confirmed deleterious BRCA mutations. Any SL-derived target program carries a built-in patient-selection story. That is an advantage, because [biomarker-stratified programs have higher likelihood of approval]({{ '/blog/2026/likelihood-of-approval-therapeutic-area/' | absolute_url }}). It is also demanding - you have to develop and validate the assay alongside the molecule, and resist the regulatory or commercial pull to broaden the program before the OS data is in.

**Novelty changes meaning.** In the single-target paradigm, "novel" means the gene has never been drugged. In the SL paradigm, "novel" can also mean *the pair* has never been drugged. A well-studied gene becomes a first-in-class target the moment someone validates it as synthetic-lethal with a disease-relevant mutation. That changes what counts as a first-in-class program and how you would score it — the kind of question the [novel-vs-repurposed framework]({{ '/blog/2026/drug-target-novelty-repurposing/' | absolute_url }}) takes up.

> **Concept Translation:** Combinatorial scaling is the recurring problem. ~200 million unordered gene pairs is roughly the same order of magnitude as a fully-specified pairwise-feature-interaction matrix in a tabular ML problem with 20K features - and most ML practitioners don't enumerate every pairwise interaction either. They use linear models with explicit pair selection, tree-based models that pick informative pairs implicitly, or low-rank embeddings that score pair similarity without storing every pair. SL prediction does the same thing: prune the search space with structural priors (network proximity, pathway membership, mutual exclusivity), then test the survivors experimentally.

<!-- SEO §4 moderate: Identifying SL pairs, method 1: CRISPR screens → Identifying synthetic-lethal pairs, method 1: CRISPR screens -->
## Identifying SL pairs with method 1 through CRISPR screens

<!-- FIGURE 2 - The CRISPR screen and MAGeCK pipeline (4-stage horizontal flow, Portage editorial style) -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN28.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN28.png' | absolute_url }}" alt="Four-stage CRISPR screen pipeline: a guide-RNA library is transfected, the cell population is split between control and treated arms, guides are sequenced and counted, and MAGeCK ranks the depleted hits." loading="lazy">
</picture>

The experimental workhorse is the pooled CRISPR screen.

### The classical screen

Design a library of guide RNAs covering the genes of interest, typically genome-wide, with ~60,000 guides and 3–4 guides per gene. Deliver the library into a cancer cell line, often one carrying a specific mutation such as BRCA1-null (the cell lacks functional BRCA1). Split the population: treat one half with the drug or condition under test, and leave the other as vehicle control (the same solvent without the active drug). Let the cells grow for a fixed number of doublings, then harvest. Copy the guide-RNA sequences out of genomic DNA with PCR (a method for copying specific DNA sequences), then sequence the pool and count the guides.

The readout is direct. A guide RNA targeting a gene whose loss sensitizes the cell to the drug becomes under-represented in the treated arm versus control because the cells carrying that guide died. A guide targeting a gene whose loss has no effect tracks the control. For synthetic-lethal discovery against a PARP inhibitor in BRCA1-null cells, the depleted guides point to genes that become essential when both BRCA1 and the PARP inhibitor are compromising the DNA-repair landscape.

> **Concept Translation:** A pooled CRISPR screen is a massively parallel ablation study with barcoded readout. Each guide RNA is a barcode that identifies which gene was knocked out in which cell. The cell population goes through a treatment perturbation and the surviving pool is sequenced. The ratio of guide counts between arms is the per-gene ablation effect - the same quantity an ML practitioner running ablation experiments is computing, but at 60,000 ablations in parallel rather than one at a time.

### MAGeCK and the statistical layer

Raw guide counts are noisy. Each gene has multiple guides with variable cutting efficiency. Library preparation and sequencing introduce batch effects, and cells under drug treatment drift. The standard analytical pipeline is **MAGeCK** (Model-based Analysis of Genome-wide CRISPR/Cas9 Knockout; Li et al., *Genome Biology* 15:554, 2014). It performs median-ratio normalization across samples, models guide-RNA read counts with a negative binomial distribution, tests each guide for differential abundance, and then aggregates guides to genes with a rank-based step that pools signal across guides targeting the same gene. The output is a per-gene score with a p-value and false-discovery rate, plus pathway-level enrichment.

For ML, MAGeCK is where CRISPR screens stop being raw counts and become a labeled dataset. The depleted-gene list becomes the positive class for any downstream classifier. The full screen, shared across labs, becomes training data for models that try to predict synthetic-lethal pairs without running a new screen every time.

### CRISPRi, combination screens, and Perturb-seq

Classical CRISPR mutates the target gene. That triggers a DNA damage response, which is fine for most targets but confounding for a synthetic-lethality screen that is itself about DNA damage. **CRISPRi** uses a nuclease-dead Cas9 (dCas9) fused to the KRAB transcriptional repressor - a protein domain that shuts transcription down. The guide RNA brings the complex to the gene's promoter, KRAB suppresses transcription, and the DNA is never cut. You get loss of function without the confounding DDR signal, and the effect is reversible, which lets you check whether a phenotype is guide-specific.

> **Concept Translation:** CRISPR-Cas9 vs CRISPRi maps neatly onto hard vs soft ablation. CRISPR-Cas9 cuts the gene out (closer to removing a feature from the dataset entirely). CRISPRi turns transcription down without altering the DNA (closer to applying a learnable mask that scales the feature contribution toward zero). For a study where the cutting itself triggers downstream artifacts - DNA damage in this case, which confounds DNA-repair experiments - the soft-ablation version isolates the loss-of-function effect from the cutting-induced effect.

**Combination CRISPR screens** place two guides in a single vector and deliver them together. This is the direct experimental approach to finding synthetic-lethal pairs: knock out both genes and measure dropout. The combinatorial scaling is the obvious limit. Even a 1,000 × 1,000 pairwise screen is a million guide combinations, not something you run casually.

**Perturb-seq** combines a pooled CRISPR screen with single-cell RNA sequencing. Each cell receives a guide RNA; when you run the single-cell readout, you recover both the transcriptome and the identity of the knocked-out gene from the same cell. Instead of a single dropout phenotype, you get a transcriptional signature for every perturbation. That signal is far richer for ML. It lets you cluster perturbations by downstream effect, build models of pathway dependencies, and identify genes whose loss produces transcriptional states similar to known synthetic-lethal partners.

> **Concept Translation:** Perturb-seq is what happens when you replace a scalar phenotype (alive / dead, fitness score) with a high-dimensional embedding (the transcriptional state of the cell after perturbation). Two perturbations that produce similar transcriptional states are likely hitting related biology, and the distance between perturbation embeddings becomes a useful feature for ML. The same intuition that drives representation-learning approaches in other domains - learn an informative embedding, then do downstream tasks in that space - applies here, with the added advantage that the perturbation labels come for free from the guide-RNA barcode.

<!-- SEO §4 moderate: Identifying SL pairs, method 2: computational prediction → Identifying synthetic-lethal pairs, method 2: computational prediction -->
## Identifying SL pairs with method 2 through computational prediction

<!-- FIGURE 3 - Synthetic lethality prediction as graph link prediction (2-panel diagram with a model-flow band, Portage editorial style) -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN29.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN29.png' | absolute_url }}" alt="Two-panel diagram of synthetic-lethality prediction: an observed gene–gene network on the left, the same network on the right with a model-predicted synthetic-lethal edge highlighted, and a graph-representation-learning → classifier → edge-probability flow band below." loading="lazy">
</picture>

CRISPR screens are definitive but expensive, and they have reproducibility issues across labs, libraries, and cell lines. A parallel literature tries to predict synthetic-lethal pairs from existing data.

### Mutual exclusivity in tumor genomics

The hypothesis is direct. If two genes are synthetic-lethal, a tumor carrying mutations in both would not survive. Across a large cohort of sequenced tumors, synthetic-lethal pairs should therefore show mutually exclusive mutation patterns. Any given tumor has a hit in gene A *or* gene B, but rarely both. The method reduces to a statistical test for co-occurrence versus the baseline expected from mutation frequencies alone. This is cheap, runs on existing cohort data such as The Cancer Genome Atlas (TCGA), and produces candidates. It also produces many false positives, because mutual exclusivity can arise for reasons unrelated to lethality - for example, two mutations producing the same downstream phenotype.

> **Concept Translation:** Mutual exclusivity is a population-level signal that substitutes for an experiment you can't run. You can't ablate two genes in one human tumor and check whether it dies; instead you check whether two ablations *ever appear together in the existing tumor population*, on the logic that if the combination were lethal, evolution would have removed it. The signal is a survivorship-based negative test - observed-but-empty cells in a co-occurrence contingency table. Like all observational substitutes for experiments, it generates hypotheses cheaply and has a high false-positive rate that calls for downstream experimental validation.

### Multi-omics layering

Mutation data alone is sparse. Adding epigenetic silencing (promoter methylation, chromatin state) and transcriptomic downregulation as proxies for functional loss makes the signal denser. A gene that is not mutated but is transcriptionally silenced is, for the cell, nearly as lost as a mutated one. Combining these layers under the rule "gene is functionally absent if mutated *or* silenced *or* strongly downregulated" expands the positive pool and gives a more reliable substrate for testing mutual-exclusivity-style hypotheses.

### DAISY and related in-silico methods

**DAISY** (Data mining synthetic lethality identification pipeline; Jerby-Arnon et al., *Cell* 158:1199–1209, 2014) is a representative in-silico synthetic-lethality pipeline that integrates cancer-sample copy-number variation (gene amplifications and deletions), transcriptomics, and short-hairpin-RNA-interference dropout data - an older screen type that suppresses genes rather than cutting them. It constructs a cancer synthetic-lethal network where edges are candidate SL pairs supported by consistent evidence across data types. The network can then be mined for gene-gene and, because some genes are drug targets, gene-drug SL interactions. DAISY was the foundational in-silico SL method; multiple successor approaches have extended it with updated data modalities and ML backbones.

### Yeast conservation

Core cellular machinery, including DNA repair, cell cycle control, and protein homeostasis, is deeply conserved across eukaryotes. Large-scale yeast double-knockout screens have been built out into broad genetic interaction maps, and conserved synthetic-lethal pairs in those maps are prior hypotheses for human pairs. The inference chain is "pair is lethal in yeast → pathway is conserved → pair may be lethal in mammalian cancer with the right mutational context," and it works often enough to be useful as a prioritization filter.

### SynLethDB

When you want to check whether any previous experimental or computational evidence supports a candidate pair, **SynLethDB** (Guo, Liu & Zheng, *Nucleic Acids Res.* 44:D1011–D1017, 2016; SynLethDB 2.0 in 2022) is the main aggregated resource - a synthetic-lethality knowledge graph curating supporting publications, experiments, and predictions across species. It is a reasonable starting point before running a new screen. It is also a live use case for the knowledge-graph methodology unpacked in [the capstone on knowledge-graph-based target discovery]({{ '/blog/2026/knowledge-graphs-drug-target-discovery-rentosertib/' | absolute_url }}).

<!-- SEO §4 moderate: Where ML actually enters → Where ML actually enters synthetic-lethal prediction -->
### Where ML actually enters

It helps to separate machine learning from statistical modeling and curation.

The *classical* SL prediction problem is binary classification. Given a gene pair, predict synthetic-lethal or not. Features are drawn from protein-protein interaction networks, gene co-expression, pathway membership, sequence or structure similarity, evolutionary conservation, shared regulators, and, when available, multi-omic co-occurrence patterns across tumor cohorts. Models range from support vector machines and random forests to gradient-boosted trees on tabular features and graph neural networks operating on learned representations of each pair.

Formulated as a graph problem, SL prediction is a link-prediction task on a heterogeneous biological network. Nodes are genes, edges are any of the thousands of known gene-gene relationships, and the model learns to predict a new edge type ("synthetic lethal with") from the surrounding topology. This is the natural formulation for graph machine learning. It also sits close to the way knowledge-graph link prediction is used for target-disease scoring more generally — the subject of the [knowledge-graph capstone]({{ '/blog/2026/knowledge-graphs-drug-target-discovery-rentosertib/' | absolute_url }}).

The network framing also gives a useful intuition about where SL partners are likely to sit. Biological networks are scale-free - they have hubs with many connections and bridges with high betweenness (nodes that lie on many shortest paths between modules). Hubs tend to be essential. Inhibit them and the cell dies regardless of genetic background, so they make poor SL candidates. Bridges and mid-degree nodes that connect parallel modules are more interesting. Losing one is survivable if the parallel module is intact, and the synthetic-lethal relationship with the parallel module appears as a structural feature of the graph. In practice, graph neural networks trained on such networks learn much of this topology implicitly. You do not need to hand-engineer bridge-like features if you have enough labeled pairs.

## The other problem of drug synergy prediction

SL prediction is about *which two genes*. Drug synergy prediction is about *which two molecules*. The two problems overlap. A drug that hits one SL-partner gene will often synergize with a drug that hits the other. Most drug-combination screens operate one level up, at the level of molecules with broad target profiles, so the ML problem changes accordingly.

A 2022 large-scale combination screen by Jaaks and colleagues (*Nature* 603:166–173, 2022) evaluated 2,025 pairs of clinical-stage compounds against 125 breast, colon, and pancreatic cancer cell lines (51 breast, 45 colon, 29 pancreatic) with deep molecular characterization. The key number for model builders: across 108,259 combination–cell-line pairs, **only about 5.2% showed synergy**, with the rate highest in pancreatic lines and lowest in breast. **Only 27% of the synergistic pairs were synergistic at both high and low drug concentrations.** Synergy is a narrow window, not a property of the pair in isolation (Jaaks et al. 2022 *Nature*).

A few implications for anyone building ML on drug-combo data.

**It's an imbalanced classification problem.** With about 5% positives, a model predicting "no synergy" for everything is already 95% accurate. Training and evaluation therefore need to handle class imbalance explicitly through sample weighting and metrics such as AUROC, AUPRC, and top-K precision.

**Context matters more than chemistry.** The same pair is synergistic in one cell line and antagonistic in another. Any model that predicts synergy from molecular descriptors alone and ignores cell-line molecular context will overfit to the average and miss the biology. Models trained across many tissues are useful for screening prioritization, but the real clinical value lies in per-tissue, or better yet per-subtype, models that condition on molecular context.

**Subtyping matters.** Breast-cancer analyses typically stratify by the **PAM50** intrinsic subtypes, an expression-based labeling scheme - luminal A, luminal B, HER2-enriched, basal-like, and normal-like. Colorectal work uses **CRIS** subtypes, a comparable expression-based subtype scheme. A pair may show synergy only in a single subtype - basal-like breast, microsatellite-stable or KRAS-mutant colon - and the Jaaks et al. screen documents several such subtype-specific combinations. A model that ignores subtype membership misses this; a model that encodes it as a feature or conditioning variable can capture it.

**The pathway-level signal is real.** Across the three cancer types in that screen, the **EGFR signaling pathway** was the one where synergistic pairs clustered most consistently, with most other pathways showing synergy in only one or two of the three. ML can surface that kind of signal directly by grouping pairs by shared pathway membership and testing for pathway-level enrichment in the synergistic set. That, in turn, points to where mechanistic explanations for synergy will be easiest to write.

Methodologically, the models used on this kind of data span the familiar ML spectrum. Support vector machines and random forests with chemical-structure descriptors and QSAR-style features (hand-engineered numerical summaries of molecular structure). Deep neural networks that take molecular fingerprints, target profiles, and cell-line omics and learn joint representations. Graph neural networks that represent drugs and cell lines as nodes in a drug-target-cell interaction graph and learn synergy as an edge-weight prediction. No single family wins consistently across benchmarks. Performance depends heavily on the dataset and the evaluation protocol, which is itself a marker of a young ML application area.

## The worked example: BRCA, PARP, and the next wave

<!-- FIGURE 4 - Two-decade synthetic-lethality timeline, 2005 to 2026 (Portage editorial style) -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN30.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN30.png' | absolute_url }}" alt="Synthetic-lethality timeline 2005–2026: PARP–BRCA discovery and the first PARP approvals, the 2022–2023 ovarian-cancer label narrowing in response to overall-survival data, and the 2024–2026 next-wave Polθ, USP1, and WRN programs." loading="lazy">
</picture>

The BRCA-PARP story is still the best worked example because it makes the full pipeline visible: biological hypothesis, biomarker definition, drug development, resistance, and label revision.

BRCA1 and BRCA2 are tumor-suppressor genes whose products are essential for homologous-recombination repair, the high-fidelity pathway that fixes DNA double-strand breaks. Loss-of-function mutations in either are common in hereditary breast and ovarian cancer and appear sporadically in other tumor types. In BRCA-mutant cells, homologous recombination is compromised, so the cell relies on error-prone backup pathways to get through S phase, the DNA-replication phase of the cell cycle. PARP1 detects single-strand breaks and recruits the repair machinery that resolves them before replication turns them into lethal double-strand breaks.

In a BRCA-wildtype cell, PARP1 inhibition is tolerable because homologous recombination can still handle the double-strand breaks that leak through. In a BRCA-mutant cell, the same inhibition produces more double-strand breaks than the crippled repair machinery can process, and the cell dies. The first clinical validation arrived in December 2014, when olaparib received FDA approval for BRCA-mutant ovarian cancer; rucaparib followed in December 2016, niraparib in March 2017, and talazoparib in October 2018 (the latter for germline-BRCA-mutant HER2-negative metastatic breast cancer). PARP inhibitors are now a multi-drug class for BRCA-mutant and homologous-recombination-deficient (HR-deficient) breast, ovarian, prostate, and pancreatic cancers.

Clinical use exposed two problems. **Resistance** was expected: tumors revert BRCA mutations, restore homologous recombination, or adapt replication-fork protection. **Biomarker drift** was the harder lesson. As the first wave of PARP inhibitors moved into broader ovarian-cancer indications - including post-platinum-chemotherapy maintenance (the drug given after an initial response to keep the disease controlled), in unselected or HRD-positive populations rather than strict BRCA-mutant ones - early progression-free-survival gains read out but mature overall-survival data did not follow. Here HRD-positive means tumors with a broader homologous-recombination-deficiency signature that extends beyond BRCA mutation status alone. Across four randomized controlled trials in advanced ovarian cancer, longer follow-up showed an OS detriment in non-BRCA-mutant arms compared with controls. Between late 2022 and late 2023, the FDA narrowed or withdrew six advanced epithelial ovarian cancer indications across olaparib, niraparib, and rucaparib, with manufacturers issuing "Dear Healthcare Provider" letters and the surviving recurrent ovarian-cancer maintenance indications restricted to confirmed deleterious BRCA mutations (ASCO and SGO summaries of the FDA revisions, 2022–2023). The synthetic-lethal argument held. The indication broadening did not.

That history sets the bar for the next wave. The field is now pursuing targets that either layer on top of PARP in BRCA-mutant settings to address resistance, or extend synthetic-lethal logic to a different mutational background altogether.

**Polθ (POLQ)** is a DNA polymerase that drives theta-mediated end joining (TMEJ), a parallel error-prone repair pathway that BRCA-deficient tumors rely on in place of homologous recombination. Polθ was identified as synthetic-lethal with BRCA1/2 in 2015–2016 work. Small-molecule Polθ inhibitors entered the clinic in the early 2020s. Artios Pharma's **ART6043** received FDA Fast Track designation on February 23, 2026 in combination with olaparib for germline BRCA-mutant (gBRCAm) HER2-negative breast cancer in patients without prior PARP-inhibitor treatment, and Artios is launching a global randomized Phase 2 in that population (Artios press release, Feb 23, 2026; ongoing Phase 1/2a NCT05898399). Dana-Farber's repurposed novobiocin program targets Polθ through a different binding mode and sits in early clinical testing.

**USP1** is a deubiquitinase that regulates translesion synthesis and Fanconi-anemia pathway signaling - two DNA-damage-tolerance systems that help cells keep copying damaged DNA and coordinate repair when replication stalls. USP1-BRCA1/2 synthetic lethality was established through a combination of genome-scale CRISPR screens and targeted validation. It is a concrete example of the methods in this post generating a clinical program. **KSQ-4279** (also reported as RO7623066 / RG6614 under a Roche partnership announced July 2023) emerged as a first-in-class USP1 inhibitor and completed first-in-human Phase 1 testing (Yap et al., 2024 ASCO Annual Meeting, abstract 3005; NCT05240898) with anemia (≈36% as a single agent, climbing to ≈87% in combination with olaparib) as the principal dose-limiting signal. A competing USP1 program, TNG348 (Tango Therapeutics), was terminated in May 2024 for liver toxicity, with Grade 3/4 liver-function abnormalities observed in patients who remained on study longer than eight weeks (Tango Therapeutics press release, May 23, 2024). The biology may be right and the molecule can still fail.

**WRN** is the clearest example of synthetic-lethality logic extending to a non-BRCA background. WRN is a RecQ-family helicase essential for genome maintenance during DNA replication. In tumors with microsatellite instability and defective mismatch repair (MSI-H/dMMR), a substantial fraction of colorectal, gastric, and endometrial cancers, loss of mismatch repair leaves cells dependent on WRN-mediated resolution of the replication stress generated by MSI. Functional-genomics screens (Project Score and Open Targets among others) identified WRN as a top SL target in MSI-H/dMMR backgrounds in the late 2010s, and three programs are now in or entering the clinic. **NDI-219216** (Nimbus Therapeutics), a non-covalent oral WRN inhibitor, completed Phase 1/2 dose escalation roughly nine months ahead of schedule with no dose-limiting toxicities and no maximum tolerated dose reached (dose escalation never hit a safety ceiling during the study), and demonstrated WRN target engagement of >24 hours (evidence that the drug was hitting WRN for more than a day). **HRO761** (Novartis) is a first-in-class oral non-covalent WRN inhibitor in a Phase 1/1b trial (NCT05838768) for MSI-H/dMMR solid tumors; ESMO 2025 interim results showed a favorable safety profile (manageable, low-grade gastrointestinal events) and encouraging signs of durable antitumor activity. **NTX-452** (Nimbus) is a follow-on candidate showing tumor regression and complete responses at low oral doses in preclinical models refractory to immunotherapy and standard chemotherapy, and began first-in-human studies in the first half of 2025 (Nimbus and Novartis disclosures; ESMO 2025 abstracts).

The pattern is consistent. Polθ, USP1, and WRN were each identified computationally or through screening, validated experimentally, and translated into clinical programs anchored on a specific genetic biomarker. The biomarker is part of the program from day one - germline-BRCA-mutant for Polθ, BRCA1/2-deficient for USP1, MSI-H/dMMR for WRN. That is the structural lesson the PARP regulatory recalibration drove home. It is what the end-to-end SL pipeline looks like when it works.

<!-- SEO §4 moderate: Robotics, AI, and the feed-forward combo screen → Robotics, AI, and the feed-forward combo screen for synthetic lethality -->
## Robotics, AI, and the feed-forward combo screen

Beyond finding SL pairs, ML also enters the screening process itself. Large-scale drug-combination screening is experimentally intensive. `2,025 pairs × 125 cell lines × multiple concentrations × biological replicates` is a large number of wells. The industry trajectory has moved toward full laboratory automation and, beyond that, toward a feed-forward loop - a robotic platform runs part of a screen, feeds the results into an ML model that scores the expected value of every remaining experiment, replans the next batch to maximize information gain, and iterates.

The ML methods here are active learning and Bayesian optimization, familiar from other high-throughput-screening contexts. The setup is direct. A surrogate model of synergy, an acquisition function that trades off predicted hits against uncertain regions of the combination space, and an experimental loop that updates the surrogate as results arrive. The combinatorial explosion that makes exhaustive screening infeasible is exactly what makes active learning valuable. You do not need to evaluate every pair if the model can prioritize well.

> **Concept Translation:** This is the same active-learning loop that ML practitioners build for any expensive labeling problem - annotation, simulation, hyperparameter search. The acquisition function is whatever balances exploitation (test pairs the surrogate already predicts as hits) against exploration (test pairs in regions where the surrogate is uncertain). Upper confidence bound, expected improvement, Thompson sampling - the standard library of acquisition functions transfers to combo screens with no modification. The experimental loop just costs more per query than a typical labeling task and produces noisier observations, which puts more weight on uncertainty-aware models.

The longer-term vision of patient-sample-derived combination screens run in hospital settings to inform individual treatment decisions remains aspirational in published work as of 2026, but it is the logical continuation of the current trajectory.

## Where the field is heading, and where caution is warranted

**Scalability of validation.** Computational SL predictions substantially outpace experimental validation, and the failure rate from computational hit to experimentally confirmed SL pair is high. The methods literature tends to report validation on a handful of top-ranked candidates; the actual precision of a model deployed at scale is usually worse than the paper numbers suggest. This mirrors the broader target-discovery validation problem that the [evidence-frameworks post]({{ '/blog/2026/target-disease-association-evidence/' | absolute_url }}) examines.

**Druggability of SL partners.** Identifying a synthetic-lethal partner solves only half the problem. Many SL partners are scaffolding proteins, transcription factors, or complex assemblies with no obvious small-molecule binding pocket. Whether a given SL target is tractable depends on [modality choice]({{ '/blog/2026/druggability-assessment-alphafold-3/' | absolute_url }}). A target that is intractable for small molecules may still be accessible to PROTACs, molecular glues, or antibody-drug conjugates. Polθ, USP1, and WRN turned out to be straightforward small-molecule targets; the next wave of SL candidates may not.

**Toxicity is not predicted by SL screens.** A synthetic-lethal pair in cancer cells says nothing about whether inhibiting target A will be tolerable in healthy tissue. The USP1 and Polθ programs both ran into clinical tolerability surprises: TNG348 was terminated in May 2024 for liver toxicity (Grade 3/4 LFT abnormalities at >8 weeks), and KSQ-4279 showed anemia signals and dose-limiting blood toxicity across the USP1 class. The PARP class illustrates the same issue one level up. Tolerability is a function of mechanism, but also of the *population* receiving the drug. The 2022–2023 OS-detriment story shows what happens when a drug that is tolerable and effective in one genetic background is pushed into a broader one without mature OS data to support it. Predicting tolerability from mechanism remains an open problem, and the SL framework provides only indirect traction on it.

**Single-cell-conditioned SL maps.** The bulk of the SL literature operates on cell-line-level data. Perturb-seq and related single-cell CRISPR-screening methods open the door to within-tumor SL maps that condition on cell state. Is a pair lethal in proliferating cells but not in quiescent, non-dividing ones? In one tumor microenvironment niche (a local cellular neighborhood) but not another? This is an area where ML models and experimental methods are evolving together, and where the 2026-onward literature is worth watching.

Two decades after its first clinical validation, synthetic lethality now looks like a mature target-discovery strategy rather than a research curiosity. The ML methods are not exotic. Most of the predictive work is binary classification, link prediction, and active learning, applied carefully to a domain with unusually clear labels, accumulating experimental data, and a clinical readout that closes the loop.

---

## Further reading

- Bryant, H. E., Schultz, N., Thomas, H. D. et al. (2005). *Specific killing of BRCA2-deficient tumours with inhibitors of poly(ADP-ribose) polymerase.* *Nature* 434, 913–917. [doi:10.1038/nature03443](https://doi.org/10.1038/nature03443). One of the two foundational papers (with Farmer et al. 2005 below) establishing the PARP-BRCA synthetic-lethal relationship in cell-line studies; the direct primary reference for the "first clinical validation arrived in December 2014" framing in the post's worked-example section. Readers who want to see the original evidence that anchored the entire next twenty years of synthetic-lethality drug development should start here.

- Farmer, H., McCabe, N., Lord, C. J. et al. (2005). *Targeting the DNA repair defect in BRCA mutant cells as a therapeutic strategy.* *Nature* 434, 917–921. [doi:10.1038/nature03445](https://doi.org/10.1038/nature03445). The companion paper to Bryant et al. 2005, published back-to-back in the same *Nature* issue, establishing the same PARP-BRCA relationship from an independent group. The two papers together are the canonical citation for the PARP-BRCA synthetic-lethality story - citing only one would be selectively citing the historical record.

- Li, W., Xu, H., Xiao, T. et al. (2014). *MAGeCK enables robust identification of essential genes from genome-scale CRISPR/Cas9 knockout screens.* *Genome Biology* 15, 554. DOI: 10.1186/s13059-014-0554-4. PMID: 25476604. The original MAGeCK methods paper; the authoritative reference for the statistical analysis pipeline described in the CRISPR-screens section. Readers who want to implement any of the draft's CRISPR-screen analysis will end up here first. **Tooling-currency note:** MAGeCK has had multiple major releases since this 2014 paper; the core negative-binomial-plus-rank-aggregation methodology is unchanged, but the software ecosystem (MAGeCK-VISPR for visualization, MAGeCK-iNC for interactive comparisons, MAGeCK-MLE for maximum-likelihood estimation in complex designs) has expanded. Readers building a current-day pipeline should cite the 2014 paper for the methodology and the most recent major release's documentation for the software.

- Guo, J., Liu, H., Zheng, J. (2016). *SynLethDB: synthetic lethality database toward discovery of selective and sensitive anticancer drug targets.* *Nucleic Acids Research* 44(D1), D1011–D1017. DOI: 10.1093/nar/gkv1108. The original SynLethDB methods paper; the primary-reference resource for anyone checking whether a candidate SL pair has prior evidence. **Database-currency note:** the database has been continuously updated since the original 2016 publication; SynLethDB 2.0 (Wang et al., *Database* 2022, baac030) added a knowledge-graph front end, CRISPR-derived SLs, and computational-prediction evidence types. Readers who use the database in practice should cite both the methods paper and the current release documentation.

- *Society of Gynecologic Oncology - Revisions to FDA Approvals for PARP Inhibitors in the Management of Ovarian Cancer.* [Society of Gynecologic Oncology summary](https://www.sgo.org/resources/revisions-to-fda-approvals-for-parp-inhibitors/). The clinical-society summary of the 2022–2023 FDA narrowing of advanced-EOC indications across olaparib, niraparib, and rucaparib in response to mature overall-survival data. The primary-source-of-record is the FDA labeling change history for each individual product, but the SGO summary is the most accessible single document covering all six indications and the OS-vs-PFS discordance that drove the recalibration - useful background for the post's "biomarker drift" framing in the worked-example section. *See also:* the JCO review by Tew et al. (2024), *Overall Survival and the Evolving Benefit-Risk Assessment for Poly(ADP-ribose) Polymerase Inhibitors in Advanced Ovarian Cancer*, [doi:10.1200/JCO-24-02834](https://doi.org/10.1200/JCO-24-02834), for the deeper review of the trial-level data.

- Chan, E. M., Shibue, T., McFarland, J. M. et al. (2019). *WRN helicase is a synthetic lethal target in microsatellite unstable cancers.* *Nature* 568, 551–556. [doi:10.1038/s41586-019-1102-x](https://doi.org/10.1038/s41586-019-1102-x). The foundational paper establishing WRN as a synthetic-lethal target in MSI-H/dMMR cancers - the third major branch of the worked-example section. Companion functional-genomics screens (Behan et al. 2019, *Nature*; Lieb et al. 2019, *eLife*; Kategaya et al. 2019, *iScience*) corroborated the finding from independent angles and are the historical anchor for the WRN clinical programs (HRO761, NDI-219216, NTX-452) discussed in the post's next-wave section. Readers interested in the broader functional-genomics screening framework that generated WRN as a hit should start here.

- Jerby-Arnon, L., Pfetzer, N., Waldman, Y. Y. et al. (2014). *Predicting cancer-specific vulnerability via data-driven detection of synthetic lethality.* *Cell* 158, 1199–1209. DOI: 10.1016/j.cell.2014.07.027. PMID: 25171417. The original DAISY paper, foundational for in-silico SL prediction. The pipeline integrates copy-number variation, transcriptomics, and shRNA dropout data to construct a cancer synthetic-lethal network, and remains the methodological reference point for in-silico SL approaches. Most subsequent in-silico SL methods are extensions of DAISY's three-evidence-type framework.

- Jaaks, P., Coker, E. A., Vis, D. J. et al. (2022). *Effective drug combinations in breast, colon and pancreatic cancer cells.* *Nature* 603, 166–173. DOI: 10.1038/s41586-022-04437-2. The 2,025-combination, 125-cell-line, 108,259-pair screen that anchors the post's drug-synergy section: the 5.2% synergy rate, the cross-tissue synergy ranking (highest in pancreas, lowest in breast), the basal-like and microsatellite-stable subtype findings, and the TOP1+CHEK1 inhibitor lead combination (irinotecan + rabusertib in mouse xenograft). Readers building synergy-prediction models should treat this dataset as a benchmark.
