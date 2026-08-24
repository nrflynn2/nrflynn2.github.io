---
layout: "post"
title: "Tissue specificity as a safety filter: GTEx, Human Protein Atlas, and scRNA-seq for target prioritization"
date: "2026-06-03 09:00:00-0700"
description: "Tissue specificity predicts on-target, off-tissue side effects before a drug is ever dosed. A practitioner's guide to GTEx, Protein Atlas, and scRNA-seq."
tags:
  - "machine learning"
  - "drug discovery"
  - "target discovery"
  - "safety"
categories:
  - "target discovery"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/blog/target-discovery/APPH_FLYNN_UN13.png"
og_image: "https://noahrflynn.com/assets/img/blog/target-discovery/APPH_FLYNN_UN13.png"
series: "Drug Target Discovery"
series_order: 3
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is a tissue-specific gene?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A tissue-specific gene is expressed preferentially in one tissue or a small group of related tissues, rather than across the body. Using the Human Protein Atlas classification, only about 5 percent of human protein-coding genes are detected in a single tissue, and another ~17 percent are restricted to a small compartment such as the several structures of the brain. Roughly 15 percent are classified as tissue-enriched overall, while about 40 percent are not tissue-specific at all. Tissue-specific genes tend to carry stronger biological relationships to their resident organs than housekeeping genes and are overrepresented among drug targets."
        }
      },
      {
        "@type": "Question",
        "name": "What is GTEx used for in drug discovery?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "GTEx, the Genotype-Tissue Expression project, is a reference atlas of bulk RNA sequencing across normal human tissues from post-mortem donors, covering more than 50 tissues across a wide sample population. The current major release is GTEx V10 (November 2024), which expanded the prior version with roughly 12 percent more RNA-seq samples, small RNA-seq data across approximately 16,760 tissue samples, and high-coverage (~195×) deep somatic whole-genome sequencing on a substantial donor subset. In drug discovery, GTEx serves two main purposes: it is the baseline reference for where a candidate target is expressed across healthy human tissues, and its eQTL calls link genotype to tissue-specific gene expression. A target that is highly expressed only in the disease tissue starts with a safety advantage that a broadly expressed target does not."
        }
      },
      {
        "@type": "Question",
        "name": "Why does tissue expression matter for drug targets?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Where a target is expressed determines where the drug's on-target effects will happen. A target expressed only in brain will produce its pharmacology in brain; a target expressed in brain, heart, and kidney will produce pharmacology in all three. The clomethiazole / GABRB2 example shows the success case: GABRB2 is largely confined to brain, which is why clomethiazole's sedative and anticonvulsant effects happen there rather than elsewhere. The failure-side example is navitoclax, a BCL-XL inhibitor whose clinical development was dose-limited by on-target thrombocytopenia because healthy platelets also depend on BCL-XL. That is exactly the on-target, off-tissue toxicity the framework is built to predict. Narrow tissue expression gives a target a baseline safety advantage. Broad expression forces the safety margin to come from potency differences, modality choice, or patient stratification rather than from tissue distribution alone."
        }
      },
      {
        "@type": "Question",
        "name": "What is single-cell RNA sequencing used for in drug discovery?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Single-cell RNA sequencing (scRNA-seq) resolves expression at the per-cell level rather than averaging across millions of cells in a bulk sample. For drug discovery, it answers questions bulk data cannot: whether a target is expressed only in a rare cell population that drives disease, whether it is present in specific cell types within a tissue, and how cell populations communicate through ligand-receptor signaling. The three main assay classes trade off coverage versus cell count: plate-based methods like SMART-seq sequence thousands of cells with deep per-cell coverage; droplet-based methods like 10x Genomics scale to hundreds of thousands of cells at lower depth; spatial transcriptomics adds tissue-position information that dissociated methods destroy. Multi-modal extensions like CITE-seq measure surface proteins alongside transcripts, which matters for antigen-targeting modalities like CAR-T and ADCs."
        }
      },
      {
        "@type": "Question",
        "name": "How do you reduce off-target effects of a drug?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Off-target effects are often conflated. Off-target activity means the drug binds proteins outside its intended set, a potency-and-selectivity problem addressed through medicinal chemistry and broader selectivity screening. On-target, off-tissue effects mean the drug modulates its intended target in a tissue where that modulation causes harm, which is the problem tissue-specificity analysis addresses directly. The main levers for reducing the on-target version are picking targets with narrow tissue expression, choosing modalities whose distribution aligns with the target's tissue footprint (GalNAc-conjugated siRNA for liver targets, ADCs for tumor-restricted antigens), and stratifying patients by the molecular criterion that actually defines the disease. The NTRK-fusion logic is another version of the same reasoning, applied to fusion-expressed protein forms. The navitoclax / BCL-XL case shows why the on-target, off-tissue half of this distinction matters: a drug can be perfectly selective for its intended target and still fail clinically if the target is expressed in tissues where modulating it is intolerable."
        }
      }
    ]
  }
---
Only about 5% of human protein-coding genes are expressed in a single tissue. Another 17% are restricted to a small group of tissues that share a compartment, like the several structures of the brain. The remaining ~78% are distributed across many tissues or expressed across nearly all of them. For target-selection work, those numbers quickly become a safety question. The tissues that express a target are the tissues that will experience its on-target effects, whether helpful or harmful.

> **Concept Translation:** Tissue expression follows a long-tailed distribution. A few thousand genes are tightly localized; most are spread broadly across the body. Drug targets are disproportionately drawn from the localized end, for a direct reason: a drug only acts where its target lives. If the target lives everywhere, the drug acts everywhere, and so do its side effects.

## Why tissue specificity matters in 2026

Two shifts have moved tissue specificity closer to the center of target assessment in 2026.

First, the modality landscape has widened. Antisense oligonucleotides, siRNAs, PROTACs, ADCs, and CAR-T cells all create different on-target, off-tissue failure modes and now sit inside routine target assessment conversations (see [druggability in the AlphaFold 3 era]({{ '/blog/2026/druggability-assessment-alphafold-3/' | absolute_url }})). On-target, off-tissue means the drug is acting on its intended target in a tissue where that biology causes harm. A PROTAC that degrades its target in tumor tissue will also degrade it in healthy tissue where the target is expressed. An ADC whose surface antigen is not strictly tumor-restricted creates a toxicity risk. The January 2024 FDA class-wide boxed warning on CD19- and BCMA-directed autologous CAR-T products for T-cell malignancies reflected how deeply the modality can penetrate immune-cell populations, rather than a chemistry failure in the CAR construct. Tissue-specificity evidence now has to travel across more modalities, and each modality adds its own interpretation layer on top of the same expression data.

> **Concept Translation:** "Off-target" and "off-tissue" are commonly conflated. *Off-target* means the drug is hitting proteins it shouldn't, which is a selectivity problem solved by better chemistry. *On-target, off-tissue* means the drug is hitting the right protein, in the wrong place. The drug is doing exactly what it was designed to do, on the protein it was designed to do it to, but in a tissue where that action causes harm. Tissue-specificity analysis is the screen for the second kind. No amount of selectivity tuning fixes the second problem; it has to be addressed at target selection.

Second, safety-evidence standards are shifting. The FDA Modernization Act 2.0 (December 2022) authorized alternatives to traditional animal testing in IND submissions, but did not require them, and the follow-on FDAMA 3.0 passed the Senate by unanimous consent in December 2025. In April 2025, the FDA announced a roadmap to phase out routine animal testing starting with monoclonal antibodies, with faster review timelines as an incentive for sponsors that adopt validated organ-on-chip, organoid, and AI-based safety evidence. Animal testing remains the default in practice, and NAMs (new approach methodologies) are usually used alongside it rather than in place of it. Computational tissue-safety evidence, which depends heavily on the databases and methods in this post, is likely to carry more weight in future target prioritization.

In the target-discovery series, tissue specificity sits inside the safety criterion. The pillar post ([the front-of-funnel decision]({{ '/blog/2026/drug-target-discovery-phase-ii-failures/' | absolute_url }})) listed five target-assessment criteria, and the evidence-of-linkage post ([target-disease evidence frameworks]({{ '/blog/2026/target-disease-association-evidence/' | absolute_url }})) covered one of them. This post covers the part of safety that can be estimated early: where a target is expressed, and where on-target, off-tissue toxicity is therefore most likely to appear.

## What "tissue-specific" means when you look at the numbers

<!-- FIGURE 1 - The tissue-expression distribution of human protein-coding genes -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN13.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN13.png' | absolute_url }}" alt="Tissue-expression distribution of human protein-coding genes: ~5% single-tissue (accent), ~17% compartment-restricted, ~15% tissue-enriched, ~23% mixed, ~40% broadly expressed." loading="lazy">
</picture>

Only a modest fraction of human protein-coding genes are tissue-specific. The Human Protein Atlas classifies roughly 15% of protein-coding genes as tissue-enriched, while around 40% are not tissue-specific at all. About 5% are detected in just a single tissue; another ~17% are restricted to a small group of tissues that may count as a coherent compartment, such as the several structures of the brain. Compared with housekeeping genes (genes expressed consistently across tissues), tissue-specific genes are more tightly tied to organ biology and are overrepresented among drug targets.

Marketed non-cancer drugs tend to be more enriched for tissue-specific targets than anti-cancer drugs. We'll work through an example to see why.

GABRB2, the brain-specific β2 subunit of the GABA-A receptor, is the target of clomethiazole, a sedative and anticonvulsant. Because GABRB2 is largely confined to brain, clomethiazole's on-target effects are concentrated where they are wanted, while on-target activity elsewhere is limited. That is the narrow-expression logic in its clearest form: when the protein largely resides in the desired tissue, the program starts with a built-in safety advantage.

The counterexample is BCL-XL. It is an anti-apoptotic protein over-expressed in many cancers, and inhibitors of the pathway, most notably navitoclax, were designed to remove that survival defense from tumor cells. The pharmacology worked, then met a hard clinical limit. Healthy platelets, the blood cell fragments required for clotting, also depend on BCL-XL for survival, so navitoclax produced severe dose-limiting thrombocytopenia (a dangerously low platelet count) at therapeutic doses. This is on-target, off-tissue toxicity. The drug is acting on the intended protein in tumor cells and in platelets, and that broad expression compresses the therapeutic index, the gap between an effective dose and a toxic dose. Tissue-specificity analysis is meant to identify this problem before the program reaches humans.

The logic also shifts across therapeutic areas. In oncology, the primary goal is to eliminate or suppress cancer cells, so side effects that would be unacceptable for a chronic non-oncology therapy, including vomiting, alopecia, and hematological toxicity, are often tolerated because the alternative is untreated cancer. Tumor-agnostic therapies, which are selected by a shared molecular lesion rather than organ of origin, introduce a second shift. When a molecular lesion defines the target, patient selection moves from organ of origin to the cells carrying the driver alteration.

## The two canonical tissue-expression databases: GTEx and HPA

Most target-selection workflows that evaluate tissue specificity rely heavily on two public resources.

**GTEx (Genotype-Tissue Expression).** A reference atlas of bulk RNA-seq across normal human tissues from post-mortem donors, covering more than 50 tissues across a wide sample population. GTEx is the standard source for baseline RNA expression of a candidate target across healthy human tissues, and its eQTL calls (tests of whether genetic variants shift gene expression) link genotype to tissue-specific expression. The current major release at the time of writing is **GTEx V10 (released November 2024)**, which expanded the prior version with roughly 12% more RNA-seq samples, a small RNA-seq dataset spanning approximately 16,760 tissue samples, and high-coverage (~195×) deep somatic whole-genome sequencing on a substantial donor subset. The somatic-WGS layer adds a second question to the usual expression lookup. In addition to asking where a target is expressed in normal tissue, teams can ask where somatic variants in or near that gene appear in healthy donors, which helps frame whether off-tissue expression is genetically modulated in ways that matter for safety.

**Human Protein Atlas (HPA).** A parallel resource with stronger protein-level coverage. HPA integrates RNA-seq data with immunohistochemistry (antibody staining of tissue sections) across a large number of cell types and tissues, and increasingly includes cell-type-specific expression data generated by single-cell RNA sequencing. It is the resource to consult when the question is whether a candidate target is actually *translated* in a given tissue, rather than merely transcribed there.

The two resources are complementary. Most contemporary target-assessment templates expect both to be consulted before a target advances to the feasibility stage. A common workflow maps the tissue-expression footprint of a candidate target with GTEx, then checks HPA protein and cell-type views for organs where on-target modulation would create a safety risk. That sequence is now a standard pre-IND analysis (work done before an Investigational New Drug filing).

### Why both mRNA and protein matter

The central dogma's DNA → RNA → protein chain suggests that mRNA abundance should be a reasonable proxy for protein abundance. In practice, the correlation is often modest, and sometimes systematically so. Three reasons matter most.

- **Protein stability and half-life vary.** A protein with a short half-life can have a much lower steady-state abundance than its transcript would predict.
- **Post-translational modifications regulate activity.** A protein may be abundant yet inactive because it is dephosphorylated, sequestered, or proteolytically cleaved, making it less druggable than its mRNA profile suggests.
- **The tumor microenvironment is non-stationary.** Cancer tissues tend to show lower mRNA-protein correlation than normal tissues, because the proteome is changing faster than the transcriptome at any given biopsy snapshot, and post-translational modifications in the tumor microenvironment further decouple the two.

> **Concept Translation:** A reasonable mental model: DNA is the static codebase; mRNA is a dispatched job request; protein is the running worker. Counting RNA reads is like counting jobs spawned per hour, not workers currently active. Protein lifetime, modifications, sequestration, and degradation all live between dispatch and execution. The two metrics are correlated, sometimes loosely, but they answer different questions. Drug targets are proteins, so a tissue-safety claim built only on RNA is solving a related-but-not-identical problem.

A tissue-specificity claim built only on GTEx RNA is fragile for a meaningful minority of targets. The obvious next check is protein-level evidence. HPA immunohistochemistry is the most common starting point, though targeted mass spectrometry and emerging single-cell mass-spectrometry methods are becoming more relevant.

### The species-conservation problem

A related complication gets less attention than it should. Tissue-specific genes are less evolutionarily conserved than broadly expressed genes. Tissue-specific genes identified in humans have substantially fewer one-to-one mouse orthologs (genes in different species descended from the same ancestral gene) than non-tissue-specific genes, regardless of how tight the tissue specificity is. Tissue-specificity correlations between species degrade quickly below chimpanzee, with fly-to-human correlations near the bottom of the ordering.

> **Concept Translation:** The species-conservation problem is a domain-shift problem. Mouse models are "in distribution" for biology that is shared with mouse, namely broadly expressed, deeply conserved genes, and "out of distribution" for human-specific or primate-specific tissue biology. The narrow, tissue-enriched targets that the framework most wants to validate in mouse are also the ones where mouse is least informative. The mismatch is structural, not a question of model quality.

The result is a familiar blind spot in preclinical development. Mouse safety data may not faithfully reflect the human safety profile for exactly the tissue-enriched targets where the framework most wants confidence. This mismatch is one reason alternative safety-evidence methods (iPSC-derived models, where adult cells are reprogrammed into stem-like cells and redifferentiated in culture, organ-on-chip systems, organoids, and human-cell-based in silico approaches) have been gaining regulatory traction in parallel with the FDA Modernization Acts.

## Single-cell and why bulk isn't enough

<!-- FIGURE 3 - Three single-cell assay classes and their trade-offs -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN14.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN14.png' | absolute_url }}" alt="Three single-cell RNA-seq classes (plate-based, droplet-based, and spatial transcriptomics) with their respective scale, depth, and architectural-information trade-offs." loading="lazy">
</picture>

Bulk RNA-seq, the data type that underlies the classical GTEx and HPA views of tissue specificity, averages expression across millions of cells in a tissue sample. If the target of interest is expressed by a rare cell population within that tissue, or at different levels in different cell types, bulk data can miss it or average it away. In diseases where cellular heterogeneity drives phenotype, such as most cancers, most autoimmune diseases, and many neurodegenerative conditions, that averaging becomes a real limitation.

> **Concept Translation:** Bulk versus single-cell is the difference between a dataset summary and a per-row dataset. Bulk RNA-seq returns mean expression across the cells in a tissue sample, the way a query that returns `AVG(feature)` across a million rows returns one number. Single-cell RNA-seq returns one row per cell. If the disease is driven by 1% of the cells, the average is a useless statistic.

Single-cell RNA-sequencing (scRNA-seq) addresses that problem, with substantially more analytical overhead. Sample preparation requires tissue dissociation followed by isolation of individual cells. The resulting data then goes through denoising, clustering, dimensionality reduction, and visualization pipelines that bulk data does not require, and the per-sample cost is roughly 10× that of bulk RNA-seq. The result is a per-cell-type expression profile that lets you ask the question bulk data cannot answer directly: is this target really only in hepatocytes (the main functional cells of the liver), or is it also in the rarer hepatic stellate cell population?

### Three technologies, three trade-offs

Practitioners typically choose among three classes of single-cell assay, each with distinct trade-offs.

**Plate-based (SMART-seq-like).** Cells are isolated by sorting, deposited into wells, lysed, and their RNA amplified with unique identifiers before cDNA synthesis and sequencing. The method sequences thousands of cells with good per-cell gene coverage. Best when you need deep transcript characterization of a small population.

**Droplet-based (10x Genomics Chromium being the most common implementation).** Microfluidics places individual cells in droplets carrying unique barcodes; first-strand cDNA synthesis happens in-droplet, followed by sequencing. This scales to hundreds of thousands of cells, at the cost of lower gene coverage per cell. The default in most contemporary scRNA-seq-based target discovery work.

**Spatial transcriptomics.** Links sequencing data to spatial position in a histological section by placing tissue on a substrate coated with barcoded probes whose position is known. RNA is captured onto the barcoded probes, and the barcode sequence tells you where each transcript came from. This matters when tissue organization carries biological information, such as tumor margins, crypt structures in the gut, and laminar layers in the brain, that dissociated scRNA-seq destroys.

Each of these technologies carries its own analysis burden. Single-cell data is sparse and zero-inflated rather than normally distributed, meaning many measured values are zeros. That produces *dropout events*, where a gene that is present in a cell is missed in sequencing and appears absent. Droplet-based methods can capture two or more cells in one droplet, producing *multiplets*, mixed-cell profiles that inflate expression estimates or fabricate apparent cell populations. A scRNA-seq analysis that does not handle these artifacts explicitly will produce tissue-specificity claims that do not hold up on replication.

> **Concept Translation:** Two terms here collide with ML vocabulary in ways that confuse cross-disciplinary readers. *Dropout* in scRNA-seq means a gene is genuinely present in the cell but its transcripts were missed during sampling, a sparse-data artifact with nothing to do with the regularization technique. *Multiplets* are closer to hash collisions: two distinct cells assigned to the same barcode, indistinguishable downstream. Both produce systematic biases that look like real signal if not corrected, which is why standard scRNA-seq pipelines include explicit dropout-imputation and doublet-detection steps.

### Multi-modal single-cell beyond CITE-seq

Single-cell methods can be combined to cover more than just transcriptomics.

- **CITE-seq** uses antibodies conjugated to oligonucleotide barcodes to measure cell-surface proteins alongside the transcriptome. This matters most when the candidate target is a cell-surface antigen, for example when assessing the tumor selectivity of a candidate CAR-T or ADC antigen, where protein presence on the cell membrane matters more than transcript presence in the cytosol.
- **Single-cell mass spectrometry and mass cytometry** are moving from development into production use, with the goal of getting protein-level resolution at single-cell scale.
- **Combined assays** pair scRNA-seq with ATAC-seq, a readout of open and potentially regulatory DNA, or methylation, and extend the single-cell approach into multi-omic tissue-specificity analysis.

### What single-cell data unlocks for target selection

Three applications are especially relevant for tissue-specificity evaluation.

**Identifying disease-driving subpopulations.** In heterogeneous diseases, including most cancers and autoimmune disorders, a small population of cells can drive the phenotype. Single-cell data can resolve these populations and identify their expression signatures, defining both the cell type a drug should target and the tissue distribution of that cell type.

**Gene regulatory network inference.** Methods like SCENIC (Aibar et al., *Nat Methods* 2017) reconstruct transcription-factor regulatory networks from single-cell data, mapping which transcription factors appear to control which downstream genes. The follow-on SCENIC+ (2023) extends the framework to multiomic enhancer-driven networks. Networks reconstructed from patient single-cell data can highlight altered pathways in disease. That is useful for candidate target discovery and for understanding which cell populations a known target acts within.

**Cell-cell communication inference.** Ligand-receptor analysis on scRNA-seq data can predict how cell populations signal to each other. In cancer, it can show that cancer-associated fibroblasts are regulating EMT-program expression in adjacent tumor cells, where EMT refers to epithelial-to-mesenchymal transition (a cell-state program associated with invasion). That, in turn, raises the question of whether the fibroblast ligand or the tumor-cell receptor is the better target.

## Worked example on the NTRK fusion-driven cancer story

A useful counterexample to the "narrow expression equals safer target" framing is larotrectinib and the NTRK fusion story.

NTRK (neurotrophic tyrosine receptor kinase) is the canonical tumor-agnostic target, a target selected by molecular lesion rather than organ of origin. In most cancers where it has been implicated, the driver lesion is a fusion, typically with a partner that leaves the kinase in an always-on state, producing an abnormally active TRK fusion protein. NTRK fusions appear across multiple cancer types; in 2018 the FDA approved larotrectinib (Vitrakvi, Bayer/Loxo Oncology) for any cancer driven by an NTRK gene fusion, making it one of the first tumor-agnostic targeted therapies.

Larotrectinib is now one of several NTRK-fusion options. Entrectinib (Rozlytrek, Roche) was approved in 2019 with broader spectrum activity including ROS1 fusions; repotrectinib (Augtyro, BMS) was approved in 2023 with improved potency and activity against resistance mutations. Tumor-agnostic NTRK-fusion treatment is now a three-drug class.

> **Concept Translation:** Tumor-agnostic targeting is closer to predicting on a feature pattern than predicting on a category label. The classical model says: *if the organ of origin is X, treat with drug Y*. NTRK-style tumor-agnostic targeting says: *if the tumor expresses the fusion-protein feature pattern Z, treat with drug Y, regardless of where the tumor sits*. The diagnostic problem becomes pattern recognition over molecular features, and the tissue label drops out of the prediction.

The lesson for tissue-specificity reasoning is direct. Patient identification for NTRK-targeted therapy is molecular, based on NTRK fusion by IHC (immunohistochemistry) or NGS (next-generation sequencing), rather than tissue-specific. TRK kinase activity is tolerated at the doses used because the fusion-expressed form is the version doing most of the clinically relevant signaling in the tumor, while the normal distribution of wild-type TRK is not the main thing the drug is hitting. In this setting, the key question is whether the *driver form* of the target is restricted to disease tissue by the genetic lesion the patient carries.

Computationally, tumor-agnostic programs depend on cross-cancer analysis: assembling genomic and expression data across many tumor types to identify which lesions recur across tissues and which do not. The Cancer Genome Atlas (TCGA) and the pan-cancer compendia it seeded (datasets that pool tumors across many cancer types) are the backbone data for that work. Tissue specificity still matters here, but in a different form from the narrow-expression framing.

## Cross-modal tissue safety in 2026

<!-- FIGURE 4 - The modality-conditional tissue-safety matrix -->
<picture>
  <source srcset="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN15.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/target-discovery/APPH_FLYNN_UN15.png' | absolute_url }}" alt="Modality-conditional tissue-safety matrix: five modalities × five tissue-distribution considerations, with the 2024 CAR-T boxed-warning instance highlighted as the canonical case." loading="lazy">
</picture>

Up to this point, the discussion has mostly assumed a small-molecule drug, the modality where tissue-expression analysis has the longest methodological history. The modality landscape has broadened, and each new modality adds its own tissue-safety question.

- **PROTACs and molecular glues.** Catalytic degradation means even transient target expression in a non-target tissue can produce a lasting effect. Degradation half-life, the identity of the recruited E3 ligase (the ubiquitin-tagging enzyme brought in by the degrader), and the rate of resynthesis of the target protein all enter the off-tissue-exposure calculation in ways that reversible binding does not.
- **Antisense oligonucleotides and siRNA.** Distribution is heavily tissue-biased by chemistry. Unconjugated ASOs partition to liver and kidney; GalNAc-conjugated siRNA, where GalNAc is a sugar ligand used to direct uptake into hepatocytes, partitions almost exclusively to hepatocytes; lipid-nanoparticle-delivered siRNA is dominated by liver uptake. Tissue-distribution safety here is partly defined by where the chemistry delivers the molecule, not merely by target expression.
- **CAR-T.** The 2024 boxed warning is a direct consequence of CAR-T products hitting antigens that are shared with normal tissues, combined with the general genotoxic risk of lentiviral integration (the insertion of vector DNA into the engineered T-cell genome). CAR-T tissue safety therefore requires thinking about the modified T-cell's own trafficking and persistence (where those engineered cells travel and how long they remain active) alongside the antigen's tissue distribution on tumor cells.
- **ADCs.** The antibody's target antigen must be sufficiently tumor-selective because payload leakage at non-target sites is a known failure mode. There are 15 FDA-approved ADCs as of mid-2025, and both the linker chemistry (how the antibody is attached to its toxic cargo) and the payload class shape the tissue-safety calculation.

> **Concept Translation:** ASOs and siRNAs are an interesting case for ML readers because the *delivery vehicle* enforces a routing constraint that the *target* does not control. A GalNAc tag is functionally a hardcoded address: regardless of where in the genome the matching transcript lives, the molecule will be delivered to liver. The drug acts on its target only in the tissue the chemistry can reach. This decouples target tissue distribution from drug tissue distribution in a way that small-molecule pharmacology rarely does.

All of these modalities draw on tissue-expression data from GTEx, HPA, and scRNA-seq. What changes is the interpretation layer. A single generic tissue-safety score is therefore less useful than a modality-conditional one. Graph-based representations fit this structure well, because tissue, cell type, target, modality, and interaction type can all be represented as different node classes connected by learned relations.

## What's next in tissue-specificity analysis

**Multi-modal reference atlases and their integration.** The Human Cell Atlas, Tabula Sapiens, and several disease-specific scRNA-seq consortia are converging toward reference panels that include tissue-level, cell-type-level, and in some cases spatial resolution. For a candidate target, the 2026 question is how to integrate these reference atlases with patient-specific single-cell data into a tissue-safety assessment that predicts rather than merely describes. Cell-type annotation transfer, using a reference atlas to assign identities to cells in a new dataset, is an active ML problem and the benchmarks are improving, but there is no single accepted pipeline for computing a target's tissue-safety score.

> **Concept Translation:** Cell-type annotation transfer is transfer learning on atlas-scale labeled data. The reference atlas provides expert-curated cell-type labels for hundreds of thousands of cells; a new dataset comes in unlabeled. The goal is to project the new cells into the reference space and inherit the labels, accounting for batch effects, technology differences, and cell-state shifts induced by disease. The same general toolkit as cross-domain classification, applied to a domain where the label space (cell types) is itself contested and evolving.

**Modality-specific tissue-safety modeling.** The next obvious ML problem is predicting modality-specific on-target, off-tissue toxicity. The field still does not have a standard benchmark. It is a good fit for anyone with access to regulatory safety datasets and the willingness to build modality-conditional representations on top of the tissue-expression atlases.

**Regulatory relevance of computational tissue-safety evidence.** FDAMA 3.0 and the FDA's April 2025 roadmap to phase out routine animal testing for monoclonal antibodies both push computational safety evidence up the regulatory priority list. In practice, animal testing remains the default and NAMs are used alongside rather than in place of animal studies. Tissue-expression databases, now enlarged with GTEx V10's deep somatic-WGS layer, are among the most mature inputs to a computational safety dossier.

**Tissue-distribution safety for target pairs.** The synthetic-lethality case raises a question the single-target framing does not. If the therapy is a combination of two agents that hit different targets, the relevant safety question is the tissue distribution of *both* targets simultaneously. Tissue specificity of a target pair is less developed than tissue specificity of a single target and is a natural next step for methods that already reason over single targets: synthetic lethality.[^synleth]

[^synleth]: Coming in a later post: ML methods for finding drug pairs that work together.

At the narrowest level, tissue specificity retires candidates before they ever get expensive. More broadly, "where does this protein live?" can no longer be answered with a single database lookup. It now requires a stack that runs from bulk RNA and protein atlases through single-cell and spatial measurements to modality-specific safety reasoning. Much of the ML opportunity in front-of-funnel target discovery sits in stitching those layers together.


## Further reading

- GTEx Consortium. *The GTEx Consortium atlas of genetic regulatory effects across human tissues.* *Science* (2020). [doi:10.1126/science.aaz1776](https://doi.org/10.1126/science.aaz1776). The canonical primary citation for GTEx as a tissue-expression resource; the GTEx Portal (gtexportal.org) is the companion hands-on reference for practitioners working directly with the data. Cite the 2020 Consortium paper for methodological grounding, and link the portal for the live tissue-expression viewer that readers new to the resource will actually use. **2026 update:** the current major release is **GTEx V10 (November 2024)**, which expanded the prior version with ~12% more RNA-seq samples, small RNA-seq across roughly 16,760 tissue samples, and deep (~195×) somatic whole-genome sequencing on a substantial donor subset. For any release-version-specific claim, verify against the portal at publication time.

- Uhlén, Fagerberg, Hallström, Lindskog, Oksvold, Mardinoglu et al. (2015). *Tissue-based map of the human proteome.* *Science* 347, 1260419. [doi:10.1126/science.1260419](https://doi.org/10.1126/science.1260419). The foundational Human Protein Atlas publication that established the tissue-classification system this post's opening statistics rely on. The proteinatlas.org portal is the companion hands-on reference.

- Tabula Sapiens Consortium. *The Tabula Sapiens: a multiple-organ, single-cell transcriptomic atlas of humans.* *Science* (2022). [doi:10.1126/science.abl4896](https://doi.org/10.1126/science.abl4896). The natural 2026 single-cell reference atlas for target-discovery work. The Human Cell Atlas (Regev et al., *eLife* 2017; search "Human Cell Atlas Regev eLife 2017") is the parallel international consortium; both are actively expanding and coverage grows with each release. Cite one or both depending on how much real estate you want to give the single-cell reference-atlas story; Tabula Sapiens is the more concise recent citation. 

