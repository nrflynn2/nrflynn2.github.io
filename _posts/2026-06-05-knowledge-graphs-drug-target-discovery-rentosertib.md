---
layout: "post"
title: "Knowledge graphs, network medicine, and the first end-to-end AI-discovered drug: a target-discovery case study"
date: "2026-06-05 09:00:00-0700"
description: "Rentosertib is the first end-to-end AI-discovered drug to show a Phase 2 efficacy signal. This post examines the knowledge graph that identified TNIK and the program that followed."
tags:
  - "machine learning"
  - "drug discovery"
  - "target discovery"
  - "knowledge graphs"
categories:
  - "target discovery"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/blog/target-discovery/APPH_FLYNN_UN23.png"
og_image: "https://noahrflynn.com/assets/img/blog/target-discovery/APPH_FLYNN_UN23.png"
series: "Drug Target Discovery"
series_order: 6
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is a biomedical knowledge graph?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A biomedical knowledge graph is a large heterogeneous graph in which nodes represent biological and clinical entities such as genes, proteins, diseases, drugs, pathways, tissues, and phenotypes, and edges represent relationships among them, such as activation, inhibition, binding, expression, or disease-gene association. Well-assembled biomedical KGs integrate dozens of public resources (DrugBank, OMIM, STRING, Reactome, ChEMBL, GWAS Catalog) with text-mined edges from the biomedical literature. The Clinical Knowledge Graph published by Santos and colleagues reported roughly 20 million nodes across 36 types and over 200 million relationships across 47 types. For ML, the key property of these graphs is incompleteness. Knowledge-graph-based target discovery tries to predict the missing edges, especially missing disease-gene edges."
        }
      },
      {
        "@type": "Question",
        "name": "How is AI used to discover drugs?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "AI contributes to drug discovery at several stages. At the front of the funnel, knowledge graphs and multi-omics pipelines identify novel disease-associated targets by predicting missing gene-disease edges in a biomedical network. Downstream, generative chemistry models design candidate molecules against those targets, and structure-prediction systems such as AlphaFold 3 and its open-source successors (Boltz-2, Chai-1, Protenix) support structure-based design even for targets without experimentally solved structures. As of early 2026, industry trackers report more than 173 AI-discovered drug programs in clinical trials, with 15 to 20 expected to enter pivotal Phase 3 trials this year. Rentosertib, an Insilico-discovered TNIK inhibitor for idiopathic pulmonary fibrosis, is the first end-to-end AI-discovered drug to show a Phase 2 efficacy signal, with both target and molecule AI-derived. Insilico's published timeline for the program reports approximately 12 to 18 months from project initiation to preclinical candidate nomination and under 30 months to first-in-human dosing, against a traditional industry benchmark of 4.5 to 6 years for the equivalent span."
        }
      },
      {
        "@type": "Question",
        "name": "What is network medicine?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Network medicine is the application of network science to human disease biology, including graph-theoretic analysis of node degree, centrality, community structure, and motifs. The premise is that biological targets do not behave as isolated points. They sit inside interaction networks, so modulating one protein propagates effects to neighbors, pathways, and downstream effectors. Network medicine methods identify hub proteins, bridging nodes with high betweenness centrality that connect distinct subnetworks, and disease modules, which are subgraphs enriched for disease-associated genes. A 2021 network-medicine framework ranked 6,340 drugs for potential COVID-19 repurposing using network-proximity methods and produced a 62 percent experimental hit rate when the top candidates were tested."
        }
      },
      {
        "@type": "Question",
        "name": "What was the first AI-designed drug?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The answer depends on the definition of AI-designed. If the term means a drug whose target was identified by AI and whose molecule was designed by generative AI end-to-end, rentosertib is the most widely cited example. Phase IIa results were published in Nature Medicine in June 2025 (PMID 40461817) from a 71-patient idiopathic pulmonary fibrosis trial, showing a +98.4 mL change in forced vital capacity at week 12 for the 60 mg arm versus a −20.3 mL decline in the placebo arm. The program also moved quickly: approximately 12 to 18 months from project initiation to preclinical candidate, and under 30 months to first dosing in humans, against a traditional industry benchmark of 4.5 to 6 years. Rentosertib also became the first AI-designed drug to receive a USAN (United States Adopted Name). As of April 2026, a pivotal Phase 3 trial has not started and regulatory discussions are ongoing. Other AI-assisted drugs have reached Phase 3 earlier, including zasocitinib (Schrödinger/Nimbus/Takeda) for psoriasis, but in those cases AI optimized a molecule against a known target rather than discovering the full program end to end."
        }
      },
      {
        "@type": "Question",
        "name": "What is rentosertib?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Rentosertib, formerly ISM001-055 / INS018_055, is a first-in-class oral small-molecule inhibitor of TNIK (TRAF2- and NCK-interacting kinase) developed by Insilico Medicine for idiopathic pulmonary fibrosis. Both the target and the molecule were AI-derived end-to-end. TNIK emerged from a multi-omics, text-mining, and knowledge-graph pipeline as a central regulator of fibrosis and inflammation, and the molecule came from generative chemistry. The discovery program reached preclinical-candidate nomination in approximately 12 to 18 months and first dosing in humans in under 30 months, against a traditional industry benchmark of 4.5 to 6 years. A Phase IIa trial (GENESIS-IPF, NCT05938920) of 71 patients across 21 sites in China published results in Nature Medicine in June 2025 (PMID 40461817), showing a +98.4 mL change in forced vital capacity for the 60 mg daily arm versus a −20.3 mL decline on placebo over 12 weeks. The trial met its primary safety endpoint. Efficacy numbers were secondary and hypothesis-generating, not statistically powered to establish efficacy. As of April 2026, a pivotal Phase 3 trial has not initiated."
        }
      }
    ]
  }
---
In June 2025, *Nature Medicine* published Phase IIa results from a 71-patient trial of a first-in-class oral kinase inhibitor for idiopathic pulmonary fibrosis. The target was TNIK (TRAF2- and NCK-interacting kinase), which was not an established IPF target when the program began. It emerged from a computational pipeline that combined multi-omics analysis (joint analysis of several molecular data types) with biomedical text mining and graph reasoning. The molecule came from a generative chemistry model. In that sense, both the target and the molecule were AI-derived end-to-end. The trial showed a +98.4 mL change in forced vital capacity (a standard lung-function measure) at week 12 for the 60 mg arm, against a −20.3 mL decline on placebo (Xu, Ren, Wang et al. 2025, *Nature Medicine*, PMID 40461817). This post examines the knowledge graph that surfaced TNIK and the program that followed.

## Why this matters in 2026

Most discussion of ML in drug discovery in 2026 still centers on chemistry. Generative models design novel small molecules. AlphaFold 3 and its open-weights successors - Boltz-2, Chai-1, Protenix - have made routine biomolecular complex prediction practical for most proteins, including in the presence of ligands, nucleic acids, and post-translational modifications. Virtual screening (computationally ranking large compound libraries for likely binders) runs at ten-thousand-compound scale in days.

This post focuses on the earlier step: deciding what a molecule should hit. When that decision is wrong, Phase II - the first stage where efficacy gets a real test in patients - fails regardless of how good the chemistry turns out to be. (The [front-of-funnel decision]({{ '/blog/2026/drug-target-discovery-phase-ii-failures/' | relative_url }}) walks through that economic argument in detail.)

Three developments since early 2024 have changed the shape of this space. Industry trackers now count more than 173 AI-discovered drug programs in clinical trials, with 15–20 expected to enter pivotal Phase III trials this year - the larger confirmatory studies usually meant to support approval. The field is no longer mostly preclinical. Recursion's May 2025 discontinuation of REC-994, its lead pre-merger AI-discovered candidate for cerebral cavernous malformation, provided the first prominent counterexample after long-term Phase II data failed to confirm earlier efficacy trends. That matters because AI-designed compounds can fail in the clinic for the same reasons traditional ones do. A third shift is structural: AlphaFold-3-class systems now sit in an open-source field rather than a single closed one, which changes the cost calculus for building target-discovery platforms on top of predicted structures.

This post is the capstone of the series. The point is integration - how evidence-framework thinking ([evidence frameworks]({{ '/blog/2026/target-disease-association-evidence/' | relative_url }})), novelty scoring ([novel vs repurposed targets]({{ '/blog/2026/drug-target-novelty-repurposing/' | relative_url }})), and the network-medicine view fit together inside a single end-to-end program, with [synthetic lethality]({{ '/blog/2026/synthetic-lethality-drug-discovery-ml/' | relative_url }}) extending the framework to combination targets.

## From biological networks to knowledge graphs

<!-- FIGURE 1 - Biomedical knowledge graph schematic -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN23.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN23.png' | relative_url }}" alt="Biomedical knowledge graph schematic with gene, protein, disease, drug, pathway, tissue, and phenotype nodes connected by typed edges; one teal-highlighted gene→pathway→disease path is labeled as a predicted candidate target–disease edge." loading="lazy">
</picture>

Network biology predates today's knowledge-graph language. In much of computational biology, *systems biology* refers to the same basic idea. In drug discovery, this way of thinking often goes under the name *network medicine* - using networks to reason about how diseases cluster in pathways and how interventions propagate through them. The premise is direct. Protein targets do not act as isolated points. They sit inside interaction networks, and any attempt to modulate one protein propagates through its edges. A target-discovery view that ignores that propagation will misread biological effect.

The zoo of biological networks breaks into roughly five types. *Protein–protein interaction networks* use proteins as nodes and physical interactions as edges; proteins with many neighbors tend to be essential for cell survival. *Gene regulatory networks* capture transcription-factor-to-target-gene relationships. *Gene co-expression networks* connect genes whose expression covaries across conditions, on the assumption that they are co-regulated. *Metabolic networks* use metabolites as nodes and biochemical reactions as edges. *Signaling networks* represent information flow from receptors through kinase cascades to effectors. Beyond these sit drug–disease association networks, sequence-similarity networks, non-coding-RNA–protein networks, and a long tail of specialty graphs.

Three structural features matter most for target discovery. First, degree distributions follow a power law - these networks are *scale-free*, with a small number of highly connected **hubs** and a long tail of sparsely connected nodes. Such networks tolerate random node removal relatively well and fail badly when hubs are removed, which is why hub proteins can be attractive therapeutic targets or dangerous *poison* targets. Second, nodes with high **betweenness centrality**, often called **bridging nodes**, connect otherwise distinct subnetworks. Hitting a bridging node is usually less lethal than hitting a hub, which is one reason these nodes attract interest as safer targets. Third, biological networks are rich in **motifs** - small overrepresented subgraph patterns that often correspond to specific biological processes.

> **Concept Translation:** Scale-free degree distributions and hub fragility are familiar from network science generally - the World Wide Web, citation networks, and protein interaction networks all share the same statistical signature. A useful intuition: random failures are absorbed because most nodes are sparsely connected, but targeted hub removal cascades because a small number of nodes carries most of the connectivity. That property does double duty in drug discovery: it tells you which proteins are valuable to hit (hubs near the disease) and which are lethal to hit (hubs essential everywhere). Bridging nodes - high betweenness centrality, low degree - sit between modules and tend to disrupt specific pathways without crashing the whole network. The same robustness math from social-network analysis transfers directly.

Knowledge graphs generalize this picture. A biomedical knowledge graph is a large heterogeneous graph in which both nodes and edges have types. Node types include genes, proteins, diseases, drugs, chemicals, pathways, tissues, cell types, phenotypes, and ontology terms. Edge types include activation, inhibition, binding, expression, disease-gene association, drug-target interaction, co-occurrence, and many others. A well-assembled biomedical KG draws from dozens of public resources - DrugBank for drug–target pairs, OMIM for Mendelian disease–gene links, STRING for protein–protein interaction data, Reactome for pathways, ChEMBL for compound–target bioactivity, the GWAS Catalog for genetic associations - then combines them with text-mined edges from the biomedical literature.

The scale is large and still growing. The Clinical Knowledge Graph published by Santos and colleagues in 2022 (Santos et al., *Nat Biotechnol* 40:692–702, DOI 10.1038/s41587-021-01145-6) reports close to 20 million nodes across 36 types and around 220 million relationships across 47 types, drawn from 26 biomedical databases and roughly 7 million abstracts. Hetionet, the open-source Himmelstein knowledge graph built around drug repositioning (Himmelstein et al., *eLife* 6:e26726, 2017), is smaller (47,031 nodes / 11 types, 2.25 million relationships / 24 types) but widely used in academic methods work. PrimeKG, released in 2023 and aimed at precision medicine (Chandak, Huang & Zitnik, *Sci Data* 10:67, 2023), integrates 20 high-quality resources to describe 17,080 diseases with around 4 million relationships. Commercial equivalents, including the ones used in the worked examples below, are typically larger, updated more often, and less transparent in how they are assembled.

The most important property of these graphs, for ML purposes, is incompleteness. We do not know most of the relationships we would need among every gene, drug, and disease. The edges we do have are enriched for what humans have already studied, so well-studied proteins collect more edges and less-studied ones fewer; that is the "ignorome" problem covered in detail in [novel vs repurposed targets]({{ '/blog/2026/drug-target-novelty-repurposing/' | relative_url }}). In one sentence: knowledge-graph-based target discovery tries to predict the missing edges.

## Text mining and where most new edges come from

<!-- FIGURE 2 - The text-mining pipeline for knowledge-graph construction -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN24.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN24.png' | relative_url }}" alt="Three-stage text-mining pipeline (information retrieval, named entity recognition at ~90% F1, relation extraction at ~50% accuracy) feeding edges into a knowledge graph; the highlighted teal arrow in the relation-extraction stage represents the extracted gene–disease relation." loading="lazy">
</picture>

No one can hand-curate a knowledge graph at PubMed scale. Several thousand new biomedical papers are indexed per day, and the useful subset - papers with new target–disease claims, new pathway assignments, new drug–target binding assays - is already larger than any curation team can track. Text mining is therefore how most new relationships enter the graph.

The text-mining pipeline that feeds knowledge graphs has three stages: information retrieval, named entity recognition, and relation extraction.

**Information retrieval** is the comparatively easy stage. Identify which documents in a corpus are relevant to a query. Industry has done that at scale for decades.

**Named entity recognition (NER)** locates predefined entity types in text - genes, proteins, diseases, chemicals, cell lines, mutations, and biological processes. For biomedical NER, the state of the art sits around 90% F1-score in aggregate, though performance varies meaningfully by entity type. Gene and cell-line names are relatively easier because they tend to be less ambiguous. Chemicals and disease names are harder because the same concept often appears under many surface forms, and informal writing is rarely tidy. For most practical purposes, that level of performance is usable. The remaining errors cluster in predictable places, and downstream graph-construction steps can often absorb them through redundancy.

**Relation extraction (RE)** is the hard part. Given two entities, determine whether a relationship exists and, if so, what kind. In biomedical text, that means triples like *gene–activates–biological-process*, *chemical–ameliorates–disease*, or *disease–affects–gene*. Approaches range from simple co-occurrence (where two entities appearing in the same abstract are treated as a hypothesis) to rule-based patterns and machine-learned classifiers. Aggregate RE performance sits around 50% accuracy. That figure makes text-mined edges hard to treat as stand-alone evidence. In practice, they are treated as weaker evidence than curated edges, and graph-scoring algorithms weight them accordingly.

Four problems keep biomedical RE difficult. Drug and disease names are heterogeneous and context-dependent - "Type 2 diabetes," "T2D," and "non-insulin-dependent diabetes mellitus" all name the same condition, but mapping surface form to canonical entity is still nontrivial. Labeled training data is scarce. Document styles vary sharply: journal articles, clinical trial registrations, and patents read like different languages even when they discuss the same target. And models still struggle to distinguish a paper's new finding from background knowledge the paper is merely citing.

Text mining also reaches beyond PubMed. Patents capture industrial priorities before papers do. Grant applications show what researchers believe can attract funding. Clinical trial registries such as ClinicalTrials.gov show what compounds are being tested against what diseases. Electronic health records, where accessible, describe observed drug effects in real patient populations. Pulling these into one graph is mostly an engineering task rather than a scientific one, but it is the sort of engineering task that takes teams years to do well.

## Graph machine learning for link prediction in target identification

<!-- FIGURE 4 - Link prediction as target identification -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN25.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN25.png' | relative_url }}" alt="Two-panel diagram showing link prediction as target identification: a known knowledge graph on the left and the same graph with a predicted disease–gene edge highlighted in teal on the right; pipeline annotation beneath shows graph representation learning feeding an MLP classifier producing edge probability." loading="lazy">
</picture>

Once you have a large, heterogeneous, incomplete knowledge graph, the ML problem that best matches "find new drug targets" is **link prediction**. Given the edges you have, predict the ones you are missing. For target identification, the mapping is direct: a missing edge between a *disease* node and a *gene* node is a hypothesis that the gene matters to the disease.

The standard approach is **graph representation learning**. Learn a vector embedding for each node - and often each edge type - so that structurally similar nodes sit near one another in embedding space. Three families dominate. *Matrix-factorization-based* methods decompose the adjacency matrix, or a weighted variant, into low-rank factors; this includes DeepWalk's matrix view and related spectral approaches. *Random-walk-based* methods such as DeepWalk, node2vec, and metapath2vec generate sequences of nodes by walking the graph and then train a word2vec-style model on those sequences. The resulting embeddings capture local neighborhood structure and higher-order connectivity. *Deep-learning-based* methods use graph neural networks - graph convolutional networks (GCNs), graph attention networks (GATs), relational GCNs (R-GCNs), and heterogeneous graph transformers (HGTs) - to learn embeddings through message passing. In message passing, each node updates its representation by aggregating information from its neighbors. The heterogeneous variants are built for the multi-node-type setting biomedical KGs require.

Once nodes are embedded, link prediction becomes a scoring problem. A multi-layer perceptron, operating on concatenated or dot-producted embeddings of two candidate nodes, outputs the probability that an edge exists. Training uses known edges as positives and sampled non-edges as negatives. The same machinery handles related tasks:

- **Drug–target interaction prediction.** Will this compound bind this protein?
- **Drug–drug interaction prediction.** Do these two drugs interact adversely?
- **Adverse-event prediction.** What post-market adverse events should we expect from a novel target?
- **Drug repurposing.** What approved drugs might treat this disease via some existing but unrecognized edge?

> **Concept Translation:** All four downstream tasks reduce to the same architecture - predict an edge of a specific type between two nodes - differing mainly in which node and edge types participate. From an ML engineering perspective, this is one of the rare cases where a single backbone (a heterogeneous graph encoder + a scoring head) genuinely covers a wide range of business problems with different tasks just being different decoder heads. That is why target discovery, drug repurposing, and adverse-event prediction sit so close together in the literature; they are sibling problems on the same graph.

What makes biomedical knowledge graphs harder than canonical social-network or citation-network benchmarks is heterogeneity. A general-purpose GCN treats all nodes and edges as the same kind of object. Biomedical graphs contain dozens of each, and edge semantics matter. A *binds* edge between a drug and a protein is not the same as an *inhibits* edge, and neither means the same thing as a text-mined *co-occurs* edge. Heterogeneous graph neural networks and relational GNNs address this by learning separate transformations for each edge type, though the added parameters create their own problem when training data is sparse.

> **Concept Translation:** Heterogeneous GNNs run into a familiar parameter-sparsity problem - every additional edge type multiplies the learnable transformations, but the labeled examples per edge type don't grow proportionally. Some edge types have millions of examples (drug–target, gene–pathway), and others have only a few hundred. The standard mitigations are familiar from low-resource ML: parameter sharing across related edge types, regularization, meta-learning across edge types, and inductive priors that bias the model toward biologically reasonable propagation patterns.

<!-- SEO §4 moderate: LLMs and the 2024+ shift → LLMs and the 2024+ shift in knowledge-graph construction -->
## LLMs and the 2024+ shift

In the course material underlying this series, LLMs appeared as a short forward-looking section: biomedical NER, relation extraction, and chat-based graph exploration. That was roughly the 2024 picture. By 2026, the picture is broader, but the uses are similar.

In practice, LLMs do three things in the knowledge-graph-for-target-discovery workflow.

**Biomedical NER, better than earlier systems.** Fine-tuned BERT-family models (BioBERT, PubMedBERT, BioGPT) pushed NER benchmarks several points past pre-LLM approaches, and current instruction-tuned models push them further still. In practice, that means a scientist can point an off-the-shelf model at a corpus and get usable entity annotations without building a specialized pipeline. The remaining errors cluster around rare entity types and domain-specific abbreviations that are underrepresented in pretraining.

**Relation extraction, still hard.** Zero-shot RE with large models performs better than zero-shot RE with smaller ones, but it still underperforms specialized supervised pipelines in entity-dense biomedical settings. The more useful shift is in *few-shot* RE. With a small set of examples for a relation of interest, large models can produce reasonable extractions across the rest of a corpus. The bottleneck moves from building a 10,000-example labeled dataset to curating 20 good examples.

> **Concept Translation:** Few-shot RE is the part of the LLM era that has changed biomedical KG construction the most. Annotating 10,000 examples of *gene–activates–pathway* triples used to require a domain-expert team and months of work. With a modern instruction-tuned model and 20 well-chosen examples, the same task can be set up in an afternoon. The annotation cost has not gone to zero - it has shifted from "label tens of thousands of examples" to "curate prompts and a small evaluation set." The bottleneck is now in evaluation rather than labeling, which is a familiar shift from other LLM application domains.

**Natural-language interfaces to knowledge graphs.** On the practitioner side, modern target-discovery platforms increasingly expose a chat interface over a structured knowledge graph instead of a SPARQL endpoint or Neo4j Cypher box (both are formal graph-query interfaces). The goal is to let a scientist ask *"what targets are upregulated in IPF patient tissue and also have a bridging-node role in known pulmonary fibrosis pathways?"* without first translating the request into a formal query language. Behind the scenes, the LLM generates structured queries, executes them against the graph, and summarizes the results. This is where the strengths and weaknesses of LLMs meet most directly. Strong systems ground each claim in a specific node or edge and show provenance. Weak ones generate plausible relationships that the graph does not support.

The largest open question for LLM-augmented KG workflows is evaluation. Even a low fabrication rate is hard to manage when the errors look fluent. A formal query interface either succeeds or fails. A chat interface can fail quietly. Platforms that take this seriously include source citations with every claim surfaced to the user.

## Worked example: the rentosertib target-discovery arc

<!-- FIGURE 3 - The rentosertib timeline (reuse / extension of P0 asset) -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN26.webp' | relative_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN26.png' | relative_url }}" alt="Rentosertib timeline from 2020 through April 2026: TNIK identification (2020–21), generative chemistry inhibitor series (2021–22), preclinical validation (2022), Phase 1 trials (2023), Nature Biotechnology discovery-to-Phase-1 paper (Mar 2024), Nature Medicine Phase IIa results showing +98.4 mL FVC vs −20.3 mL placebo (Jun 2025, highlighted in teal), and Phase 3 regulatory discussions ongoing (Apr 2026, open marker)." loading="lazy">
</picture>

Rentosertib, formerly known by the internal codes ISM001-055 and INS018_055, is the clearest public example in 2026 of an end-to-end AI-driven target-and-molecule program. It deserves a close read for two reasons. The public documentation is unusually thorough - two *Nature*-family papers in fifteen months and a Harvard Business School teaching case. And the program runs through every part of the methodology discussed above.

The program-level fact that stands out is speed. Project initiation to preclinical candidate nomination took about 12 to 18 months; project initiation to first dosing in humans took under 30 months. The traditional industry benchmark for the same span is 4.5 to 6 years. The open question is whether that compression holds across other programs or whether it depended on favorable conditions specific to TNIK and IPF, including strong network-medicine support for the target and relatively well-characterized fibrotic biology. Insilico has framed the result as a counterexample to **Eroom's Law** - Moore's Law spelled backwards, the observation that pharmaceutical R&D productivity has fallen despite rising technological capability. That is the strongest version of the speed claim.

### Target identification - multi-omics to TNIK

The program began with idiopathic pulmonary fibrosis, a progressive and fatal lung disease with limited treatment options. The target-identification pipeline combined several streams: multi-omics analysis of lung tissue from IPF patients versus healthy controls to find differentially expressed genes; pathway activation inference to identify dysregulated fibrosis pathways; text mining across the IPF literature to collect known disease–gene associations; and knowledge-graph reasoning over protein–protein interactions and pathway data to propagate signal from known IPF targets to their network neighbors. (The structured evidence frameworks for weighing target-disease linkage across multi-omics streams are the subject of the [evidence frameworks post]({{ '/blog/2026/target-disease-association-evidence/' | relative_url }}).) TNIK, TRAF2- and NCK-interacting kinase, emerged as a novel candidate IPF regulator. The key point is novelty. TNIK was not an established IPF target at the start of the program. It emerged from computational analysis rather than from the pursuit of an already published target hypothesis. That distinguishes it from the many AI-supported programs in which ML optimizes a molecule against a preselected target. In the target-discovery literature, TNIK is described as a central regulator of fibrosis and inflammation because multi-omics signal and proximity in the graph to genes already implicated in IPF pathways converged on it, not because the literature had already settled on it.

> **Concept Translation:** "Knowledge-graph reasoning to propagate signal from known targets to their neighbors" is graph diffusion in operational terms. Start with seed nodes that are known IPF-associated genes, then run a random walk or label-propagation algorithm across the graph and rank nodes by how much weight they accumulate. Nodes that aren't in the seed set but accumulate high weight - TNIK, in this case - are the candidates. This is the same algorithm family used for personalized PageRank or graph-based semi-supervised learning, applied to the target-prioritization problem.

### Target validation - parallel preclinical and chemistry

Validation ran in parallel with early chemistry, as it does in many modern programs. Wet-lab validation is expensive, and strict sequencing lengthens the cycle. Preclinical models confirmed that TNIK inhibition reduced fibrotic phenotypes in multiple systems. Generative chemistry tools produced a series of TNIK inhibitors; a small subset was synthesized and tested; and the compound that became rentosertib emerged from that iteration. The full discovery-to-Phase-1 history appeared in *Nature Biotechnology* in March 2024 (Ren et al., doi:10.1038/s41587-024-02143-0). That compressed validation-chemistry loop is what produced the 12-to-18-month preclinical-candidate-nomination timeline noted above. The Harvard Business School case study treats the parallelism, more than any single computational breakthrough, as the most reproducible lesson.

### Phase I - safety and pharmacokinetics

Two Phase 1 trials, one in New Zealand and one in China, together with a Phase 0 microdose trial, established safety, tolerability, and a favorable pharmacokinetic profile in healthy volunteers by 2023. A microdose trial gives a very small, subtherapeutic dose to gather early human data, and pharmacokinetics refers to how the body absorbs, distributes, metabolizes, and clears the drug. This was standard Phase I work. What stands out is how quickly the program reached human dosing, not any unusual feature of Phase I design or conduct.

### Phase IIa - the GENESIS-IPF trial

The Phase IIa trial (NCT05938920) was a multicenter, double-blind, placebo-controlled, randomized study of 71 IPF patients across 21 sites in China, with 12 weeks of dosing (Xu, Ren, Wang et al. 2025, *Nature Medicine*, PMID 40461817). The primary endpoint was safety, and rentosertib met it. The secondary endpoint was change in forced vital capacity from baseline at week 12. The 60 mg daily arm showed a +98.4 mL change in FVC, compared with a −20.3 mL decline in the placebo arm. The trial was not statistically powered to establish efficacy - it was a proof-of-concept study designed to look for an early signal rather than to settle the question definitively. Even so, the direction of effect is what *Nature Medicine* described as the first clinical proof of concept for an end-to-end AI-discovered drug when the results were published in June 2025 (Xu, Ren, Wang et al., doi:10.1038/s41591-025-03743-2; PubMed PMID 40461817).

Rentosertib was also the first AI-designed drug to receive a USAN (United States Adopted Name). That detail is small, but it suggests the regulatory apparatus is starting to treat these programs as part of ordinary drug development rather than as an exception.

### Interpretation - what 71 patients does and doesn't prove

The trial enrolled 71 patients for 12 weeks, so it is not a registrational result - it is not the kind of trial package used to support approval. It is hypothesis-generating. As of April 2026, no pivotal trial is running; Insilico is in regulatory discussions about a Phase IIb pivotal study, and a separate US Phase IIa (NCT05975983) is enrolling, with eight of a planned 60 patients reported to have completed the 12-week treatment as of mid-2025 and a primary completion date of February 2026. If a pivotal study reads out negative, rentosertib will join the long list of Phase IIa direction-of-effect signals - cases where the treated arm moved in the expected direction but the result did not hold up in larger testing - that did not replicate.

For target-discovery methodology, the more instructive part lies upstream of Phase IIa. TNIK had to be identified before any chemistry could begin, and that happened through a workflow that combined multi-omics, literature mining, and knowledge-graph reasoning. The Phase IIa result matters because it suggests the target call was directionally right. The harder question is generalization across diseases, and that will take a decade of readouts to answer. Recursion's May 2025 discontinuation of REC-994 is a useful reminder that AI-discovered targets can fail for the same reasons traditionally discovered targets fail; the failure mode is familiar (the LOA economics that explain why single-program failures matter less than cumulative field readouts are the subject of the [therapeutic-area economics post]({{ '/blog/2026/likelihood-of-approval-therapeutic-area/' | relative_url }})).

## What's next, and where to watch

Four developments are worth tracking over the next 12–24 months.

**Rentosertib Phase III.** The pivotal trial has not started as of April 2026; Insilico's public statements indicate that regulatory discussions are ongoing, and late-2025 reporting pointed to Q4 2025 as the target for late-stage trial initiation. A successful Phase III would be the next major readout because it would remove the easiest objection to the story - one 71-patient Phase IIa study is too thin a basis for broad claims. It still would not settle the methodological question on its own. A failed Phase III would also leave the broader question open.

**Generalization across modalities.** Rentosertib is a small-molecule kinase inhibitor. The same methodology has not yet been publicly demonstrated at comparable depth for antibody targets, nucleic-acid therapeutics, or targeted-protein-degradation modalities such as PROTACs and molecular glues, let alone cell therapies. Published target-discovery platforms can, in principle, output candidates regardless of downstream modality. The empirical record of "we predicted this target, built a non-small-molecule against it, and it worked" is still much thinner. The [druggability post]({{ '/blog/2026/druggability-assessment-alphafold-3/' | relative_url }}) covers why that matters.

**Open-source vs proprietary knowledge graphs.** The field is split. Open resources such as Open Targets, Hetionet, PrimeKG, and Clinical Knowledge Graph are large, documented, and freely available, but they update slowly. Proprietary platforms inside target-discovery companies are larger, updated continuously, and tied to proprietary ML models, but they are hard to validate from the outside. Whether a fully open target-discovery stack can match a well-resourced proprietary one remains unresolved. The answer matters. A yes would democratize the workflow; a no would concentrate capability inside a small number of well-funded platforms.

**Regulatory path.** The FDA published its draft guidance on AI in drug development in January 2025, with final guidance expected in Q2 2026. The draft sets out a risk-based credibility framework for sponsors who use AI in regulatory submissions. For knowledge-graph-based target identification, which sits several steps upstream of any direct regulatory decision, the practical implications are still unsettled. The most immediate effect is likely to be pressure for **provenance** - a clear trail from each claim back to its supporting source data and model version. Every claimed edge in a submission KG will need a traceable source, and every ML-predicted target will need documented training data and model versioning. Tooling for that level of provenance is not yet standardized.

> **Concept Translation:** The provenance question for regulatory-grade knowledge graphs is closer to model cards, dataset cards, and ML lineage tooling than to anything traditional in computational biology. Each predicted target needs a traceable answer to "where did the supporting edges come from, when were they extracted, what model or curator extracted them, and what version of the graph produced this prediction?" The ML community has been working through similar questions for several years (think bias audits, dataset documentation, version-pinned model artifacts). Drug-discovery teams are about to inherit the same problem at higher stakes.

For most of the last decade, target discovery was the part of drug development least altered by ML. That is no longer true. The rentosertib Phase IIa result does not resolve whether knowledge-graph-based target identification can supplant traditional, hypothesis-driven discovery; that will require many more programs and much more time. What it does establish is that ML has reached the front of the funnel. The live questions now concern reliability, boundary conditions, and failure modes.

Those are better questions than the field was asking two years ago.


---

## Further reading

- Xu, Z., Ren, F., Wang, P. et al. (2025). *A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized Phase 2a trial.* *Nature Medicine.* DOI 10.1038/s41591-025-03743-2; PubMed PMID 40461817. The Phase IIa results paper for the rentosertib program - the primary source for the +98.4 mL FVC change, the 71-patient GENESIS-IPF trial design, the 22-site China execution, and the biomarker-correlation analyses the post summarizes in the "Worked example" section. Readers who want to verify the specific trial endpoints, dose arms, or safety findings should go here. **Important note on currency:** the published paper is the Phase IIa result only; Phase 3 status changes on a quarterly cadence, and readers should cross-reference ClinicalTrials.gov for the current pivotal-trial status at the time they read this post.

- Ren, F., Aliper, A., Chen, J. et al. (2024). *A small-molecule TNIK inhibitor targets fibrosis in preclinical and clinical models.* *Nature Biotechnology.* DOI 10.1038/s41587-024-02143-0. The discovery-to-Phase-1 history paper - the methodological companion to the Phase IIa paper above, covering target identification (the multi-omics and knowledge-graph workflow that surfaced TNIK), generative chemistry (the molecule-design arc), preclinical validation, and Phase 1 safety/PK. **This is the primary source for the "Target identification" and "Target validation" subsections of the rentosertib worked example.** Readers who want to understand the methodology in more detail than the blog post provides should go here first; it is the denser technical reference of the two rentosertib papers.

- Open Targets Platform documentation (2026). *Open Targets Platform: data sources and scoring.* [URL: https://platform.opentargets.org/docs]. The canonical open-source reference public biomedical knowledge graph - free, well-documented, continuously updated. The documentation covers the evidence categories, data sources (ChEMBL, UniProt, GWAS Catalog, OMIM, Reactome, and roughly 20 others), and target-disease scoring methodology that a practitioner would need to adapt for building a similar system or integrating Open Targets into their own pipeline. **This replaces what would otherwise be a proprietary-platform reference** and is the cleanest methodology-to-implementation handoff in the Further Reading block. Aligns with the sponsor-neutrality audit: an open, free, well-documented platform is a better reader resource than a commercial vendor's whitepaper. (For the operational scoring rationale and the human-genetics weighting in particular, see also the *Annual Review of Biomedical Data Science* methodology paper from the Open Targets team - discoverable via the platform documentation.)

- Himmelstein, D. S., Lizee, A., Hessler, C., Brueggeman, L., Chen, S. L., Hadley, D., Green, A., Khankhanian, P., Baranzini, S. E. (2017). *Systematic integration of biomedical knowledge prioritizes drugs for repurposing.* *eLife* 6:e26726. DOI 10.7554/eLife.26726. The canonical academic reference for a working biomedical knowledge graph (Hetionet) combined with a link-prediction-based drug repurposing workflow. Hetionet is open-access, an order of magnitude smaller than commercial KGs but rigorously documented, and the paper walks through the graph-representation-learning-to-link-prediction pipeline the "Graph machine learning" section describes. **Recommended as the single best academic introduction** to the methodology for a reader who wants to see a working biomedical KG plus link-prediction treatment in one primary source.
