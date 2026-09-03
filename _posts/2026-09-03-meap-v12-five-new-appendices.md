---
layout: "post"
title: "Build AI Drug Discovery Pipelines, MEAP v12: five new appendices and the last update before production"
date: "2026-09-03 00:30:00-0700"
description: "What changed in version 12: new appendices on computational target discovery and on diffusion and flow matching, a rebuilt glossary and data catalog, 87 exercises, and code for Chapter 13."
tags:
  - "machine learning"
  - "drug discovery"
  - "book"
  - "writing"
categories:
  - "book"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/blog/meap-v12/book-map-og.png"
og_image: "https://noahrflynn.com/assets/img/blog/meap-v12/book-map-og.png"
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is new in MEAP v12 of Build AI Drug Discovery Pipelines?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Version 12 adds five appendices. E collects theory relocated out of Chapters 3, 4, 9, 10, and 11 and adds a new section on single-sequence protein folding. F consolidates 202 chapter references. G adds 87 exercises with structured metadata. H is a 28,000-word treatment of computational drug target discovery. I covers diffusion and flow matching with five runnable notebooks. All thirteen chapters and Appendices A through D were revised, Chapter 13 gained code for the first time, and the book now carries over 250 figures and over 180 code listings."
        }
      },
      {
        "@type": "Question",
        "name": "Do existing MEAP owners have to pay for version 12?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Manning MEAP updates are included with the original purchase, so version 12 is already available in the account of anyone who owns the MEAP. There is nothing to buy and nothing to claim. Readers who do not own the book yet can buy it at manning.com, and Manning is running a Labor Day sale from September 3 through September 7 in 2026 with all titles at half price, applied automatically without a discount code."
        }
      },
      {
        "@type": "Question",
        "name": "What does Appendix H cover?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Appendix H is a treatment of computational drug target discovery framed around the economics of target selection. It covers target-disease linkage and the omics stack, druggability and modality choice across small molecules, degraders, oligonucleotides, antibody-drug conjugates, peptides and cell therapies, tissue specificity as a safety filter, and likelihood of approval by therapeutic area. Four ML-heavy sections then cover novelty quantification and repurposing, knowledge graphs and network medicine, synthetic lethality, and virtual cells, with the rentosertib program as a worked case study."
        }
      },
      {
        "@type": "Question",
        "name": "What does Appendix I cover?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Appendix I builds diffusion and flow matching from scratch. It starts with a two-dimensional toy problem, implementing DDPM with a cosine schedule, then flow matching with straight-line interpolation, then ODE sampling. It then applies both to real chemistry and structural biology through FlowMol3 for 3D molecule generation, DiffSBDD for pocket-conditioned ligand design, RFdiffusion for protein backbone design, and Boltz-2 for binding triage. Five companion notebooks ship with it, and most of the work runs on CPU."
        }
      },
      {
        "@type": "Question",
        "name": "What is left before the book goes to print?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Copyedit, figure finalization, and an errata pass. Version 12 is very likely the last MEAP update before production. The fastest way to report an error is the liveBook forum, and the companion code repository at github.com/nrflynn2/ml-drug-discovery accepts issues and pull requests. Two readers already have fixes in version 12 through that repository."
        }
      }
    ]
  }
---

Version 12 of the MEAP for [*Build AI Drug Discovery Pipelines*]({{ '/book/' | absolute_url }}) is out. It adds five appendices, revises all thirteen chapters and the four appendices that already existed, and brings the book to over 250 figures and over 180 code listings.

I streamlined chapters 3, 4, 9, 10, and 11 to the more practical components and moved several theoretical elements into a new Appendix E. Similarly, references and exercises have been relocated out of the chapters and into Appendices F and G, where I've further expanded them.

The two largest additions were based on topics that readers showed the largest desire in having incorporated into the book. Readers coming from biology and chemistry wanted to know how a target gets chosen in the first place, and how deep learning is changing that decision. Readers coming from machine learning wanted to know how diffusion, which has taken over so much of the field, gets applied to molecules and proteins. Appendix H and Appendix I now cover both topics, respectively.

v12 is very likely the last MEAP update before production!

## TL;DR

- **Five new appendices.** E collects the theory that came out of the longest chapters. F consolidates every chapter's references. G collects 87 exercises. H is a full treatment of computational drug target discovery. I builds diffusion and flow matching from a two-dimensional toy up to FlowMol3, DiffSBDD, RFdiffusion, and Boltz-2.
- **Chapters 1 through 13 and Appendices A through D revised throughout.** Chapter 13 now ships with a companion notebook.
- **The glossary went from 107 entries to 718,** written so a reader arriving with only ML or only biology can more easily work through the full book.
- **The data catalog went from 19 resources to 84,** current to 2026.
- **The code repository got a full quality pass:** hardware portability for local runs, bug fixes, dependency modernization, and new notebooks for Chapter 13 and Appendix I.
- **About twenty reviewers** read the manuscript and provided useful feedback and corrections, which have led to improvements in the overall quality of the book. Thank you to all reviewers.
- **v12 is very likely the last MEAP update before production.** If you already own the MEAP, v12 is yours at no extra cost. If not, Manning is running a Labor Day sale from September 3 through September 7 with everything at half price.

<!-- FIGURE 1 - Map of the whole book with v12 status encoded per chapter and appendix -->
<picture>
  <source srcset="{{ '/assets/img/blog/meap-v12/book-map.webp' | absolute_url }}" type="image/webp">
  <img src="{{ '/assets/img/blog/meap-v12/book-map.png' | absolute_url }}" alt="Three-column map of Build AI Drug Discovery Pipelines. Part 1 lists Chapters 1 through 7 on cheminformatics and machine learning fundamentals, Part 2 lists Chapters 8 through 13 on deep learning for molecules and structural biology, and the third column lists Appendices A through I. Appendices E, F, G, H, and I are filled solid teal as new in version 12; Appendices A and B are outlined in teal as rebuilt; every chapter is shaded pale blue as revised. Chapters 3, 4, 9, 10, and 11 are tagged as having moved theory into Appendix E, and Chapter 13 is tagged as having gained a notebook." loading="lazy">
</picture>

## What moved out of the chapters

Chapters 3, 4, 9, 10, and 11 contained stretches of theoretical deep dives that we thought might be overwhelming for readers working through the code on a first pass. I've migrated this material to Appendix E, with the goal that the chapters that lost it read faster.

**E.1, from Chapter 3.** The formal target-function setup, the three-component decomposition of a learning algorithm, the parametric and nonparametric distinction, coefficient distribution diagnostics, the variance inflation factor with its thresholds at 10 and 5, and the cost functions for L1, L2, and elastic-net regularization.

**E.2, from Chapter 4.** The ordinary-least-squares normal-equation derivation with its O(NM²) complexity, the full gradient-descent walkthrough with convergence criteria, the stochastic and mini-batch variants, gradient cliffs and clipping, the feature-scaling formulas, and the RANSAC and support-vector-regression treatments.

**E.3, from Chapter 9.** The unabridged Deep Docking implementation: the preprocessor class with its full PDBFixer walkthrough, Meeko conversion to PDBQT, the nine-pose AutoDock Vina results with a best pose at -9.246 kcal/mol, the four-tier validation ladder, and ProLIF interaction fingerprints.

**E.4, from Chapter 10.** The variational autoencoder derivation, including the closed-form Gaussian KL divergence, the reparameterization trick, cyclical annealing with its schedule formula, and perplexity and per-dimension KL monitoring. Table E.4.1, which compares a plain autoencoder against a cyclically annealed VAE, now appears only here. The section closes with a sidebar on training and debugging VAEs for molecules that names three failure modes and gives a diagnostic threshold for each.

**E.5, from Chapter 11.** The graph-neural-network mathematics: message passing, GCN with symmetric normalization, GAT with multi-head attention, GIN with its injectivity argument and the link to the Weisfeiler-Lehman test, graph-level pooling through the Battaglia generalized message-passing equations, and over-smoothing with residual and jumping-knowledge remedies.

Additional details regarding SimpleFold from chapter 12 are predominantly in Appendix D, with a few additional details in Appendix E.

> **Concept Translation:** A multiple sequence alignment is the evolutionary record of a protein family, and AlphaFold2 reads it as a feature. A single-sequence model has to infer the same constraints from the amino acid string alone, the way a language model infers syntax with no parse tree. On common targets that works. On a protein with few known relatives, the alignment is carrying information the sequence does not contain, and the benchmark gap illustrates this. I.e., while PLMs are approaching parity on standard targets, the "explicit" signal provided by MSAs remains indispensable for more challenging, evolutionarily distinct protein structures.

## References and exercises now have their own appendices

Appendix F collects every chapter's reference list in one place (202 references across 13 chapters). Appendix G collects every chapter's exercise list in one place, while also expanding the initial set of 22 exercises to 87 exercises across the core 13 chapters.
Every exercise contains information on: Level, Type, Time, Format, Reinforces, and Objective, plus Hint, Check, and Extension metadata. My goal was to incorporate exercises that mix after-chapter review, self-study projects, classroom or reading-group discussion (i.e., meant to spark debate), and research preparation, along with ideas for a closing capstone project.

## Appendix H, computational drug target discovery

Appendix H is the largest single addition in this update, covering target discovery through an economic framing. My intent was to flag target selection's stature as a (relatively) cheap stage as a potential trap, given that decisions made at this stage affect the price of every stage after it:

> Roughly seventy-two percent of drugs entering Phase II do not transition to Phase III, and approximately ninety percent of investigational drugs fail somewhere in clinical development. Lack of efficacy is the single largest reason, accounting for about half of all clinical-trial failures.



Appendix H includes 10 sections:

- H.1 sets the stakes and the five criteria a target has to satisfy.

- H.2 through H.5 detail four assessment axes: target-disease linkage and the omics stack, druggability and modality choice, tissue specificity as a safety filter, and likelihood of approval by therapeutic area.
- H.6 through H.9 cover related ML-heavy methods: novelty quantification and repurposing, knowledge graphs and network medicine, synthetic lethality and combination targets, and virtual cells.

## Appendix I, diffusion and flow matching

From the initial book proposal I presented to Manning, I always wanted to compose a chapter on diffusion-based methods and their application in drug discovery. It took some time to get to it, but I'm glad we were able to fit in one last appendix for it. The resulting Appendix I starts from a limitation in Chapter 10's variational autoencoder (this is a similar framing to Appendix C, which also branches off Chapter 10 with method improvements in generative molecular design).



The appendix starts from basics, building an alternative from scratch with an initial application on a two-dimensional two-moons toy: DDPM with a cosine schedule and a closed-form forward jump, then flow matching with straight-line interpolation and a conditional velocity target, then ODE sampling with forward Euler. Only after that does it touch a molecule. From then on, we continue to scale complexity as the chapter progresses, involving discussion and usage of FlowMol3, DiffSBDD, QED optimization, RFdiffusion, and Boltz-2.

> **Concept Translation:** Diffusion and flow matching both turn noise into a molecule over many small steps. The difference is the shape of the path. Diffusion learns to reverse a noising process, so it retraces whatever curve that process carved. Flow matching trains on a straight line from noise to data, so it follows something closer to a straight shot. Straighter paths need fewer steps, and steps are what you pay for every time you sample.

Notably, almost all of it can run on a laptop. Only RFdiffusion and Boltz-2 need a GPU, with the whole designability loop costing under a dollar of GPU time.

## Glossary and data catalog updates

I've extended Appendix A from 107 entries to 718.

The book has always had two primary audiences arriving from orthogonal directions (life science and ML domain experts), and the new glossary targets breadth. Roughly, the term concept coverage is 98 neural-network fundamentals, 57 entries on structural biology and protein folding, 47 on target discovery and systems biology, 35 on newer modalities including degraders, biologics, oligonucleotides, and cell and gene therapy, 31 on docking and simulation, 29 on transformers and attention, 27 on medicinal chemistry and library design, 25 on metrics and calibration, 20 on graph ML, and 19 on ADMET.

I've also extended Appendix B, the data catalog, from 19 resources to 84 resources.
v12 has ten thematic catalog sections plus four guidance sections covering usage notes, data quality, where to look next, and references.

The benchmark section is the largest at 14, and includes references to MoleculeNet, Therapeutics Data Commons, Polaris Hub, PoseBusters, PLINDER, CrossDocked2020, OGB, GuacaMol, MOSES, LIT-PCBA, the Astex Diverse Set, DUD-E, CASP, and CAMEO. Twelve target-discovery resources were added, including Open Targets, DepMap, LINCS L1000, STRING, Reactome, GEO, GTEx, and TCGA, along with seven for specialized modalities and five each for toxicity and for reactions.



## Code

All code remains available at [github.com/nrflynn2/ml-drug-discovery](https://github.com/nrflynn2/ml-drug-discovery), with the following additions.

**Chapter 13 ships code for the first time.** It previously had no companion notebook. `CH13_FLYNN_ML4DD.ipynb` calls NVIDIA's hosted Boltz-2 and DiffDock endpoints, keyed off an `NVIDIA_API_KEY` read from the environment or from Colab secrets. It defaults to `USE_CACHED = True`, so it reads committed CSVs and can run with no key and no network.

**Appendix I ships five notebooks.** The notebooks are "Diffusion Models, from the Ground Up"; "Flow Matching: Straight-Line Generative Modeling"; "FlowMol3: Flow Matching for Real 3D Molecules"; "DiffSBDD: Designing Ligands Inside a Binding Pocket"; and "Frontier Read-Alongs: Diffusion at the Protein Scale." As before, with the intent of making learning more practical regardless of compute resources, every notebook that trains a model defaults `USE_CACHED = True`, and the first one trains its toy diffusion model from scratch in about a minute on CPU.

**The rest of the repository caught up.** Every chapter notebook was re-run and reviewed at listing granularity across Chapters 1 through 12 and Appendix C. Dependencies were modernized across the board, which provided a chance to improve several listings and also resolve some nasty bugs.

## Reviewers and contributors

About twenty reviewers of varying backgrounds and expertise read this manuscript. Reviewing a technical book is unglamorous work that mostly consists of telling the author that something they were proud of is confusing. I am grateful for it, and the book is better in ways I would not have found alone.
While I don't know the identity of any of these reviewers, I wanted to take some space to thank them for their contributions.

Two readers contributed to the repository itself. Thomas To (`thomas-to-bcheme`) contributed the pull requests that made Chapters 8 through 12 run across accelerators. Thiago Britto-Borges (`tbrittoborges`) fixed a working-directory bug in the Chapter 2 data loader that broke the notebook for anyone who ran it from the wrong place.

## What is left

Copyedit, figure finalization, an errata pass, and other miscellaneous production steps.


If you find something wrong, let me know. The repository also welcomes issues and pull requests.

If you have the MEAP, v12 is already in your account. If you do not, Manning's Labor Day sale runs September 3 through September 7 with everything at half price, applied automatically at [Manning](https://www.manning.com/books/build-ai-drug-discovery-pipelines?utm_source=flynn&utm_medium=affiliate&utm_campaign=book_flynn_machine_2_29_24&a_aid=flynn&a_bid=ddb44578&chan=mm_website).


## Further reading

Below are a few of the primary sources behind the two new appendices. Worth reading whether or not you buy the book :)

- Wang, Y., Lu, J. et al. (2025). *SimpleFold: Folding Proteins is Simpler than You Think.* *ICLR 2026*. [arXiv:2509.18480](https://arxiv.org/abs/2509.18480). The single-sequence folding model discussed in Appendix D, and the source of the CAMEO22 against CASP14 comparison that keeps alignments in the picture.
- Passaro, S., Corso, G. et al. (2025). *Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction.* *bioRxiv*. [10.1101/2025.06.14.659707](https://doi.org/10.1101/2025.06.14.659707). The co-folding and affinity model that triages generated molecules at the end of Appendix I. Read it next to its reported false-positive rate.
- Dunn, I. and Koes, D.R. (2026). *FlowMol3: flow matching for 3D de novo small-molecule generation.* *Digital Discovery* 5, 2052-2066. [10.1039/D5DD00363F](https://doi.org/10.1039/D5DD00363F). The generator behind the step-count result. Its weights carry no license statement, which is why the model inventory tracks code and weights separately.
- Schneuing, A., Harris, C. et al. (2024). *Structure-based drug design with equivariant diffusion models.* *Nature Computational Science* 4, 899-909. [10.1038/s43588-024-00737-x](https://doi.org/10.1038/s43588-024-00737-x). DiffSBDD. One 17.86 MB checkpoint does pocket-conditioned generation, property optimization, and scaffold inpainting with no retraining.
- Watson, J.L., Juergens, D. et al. (2023). *De novo design of protein structure and function with RFdiffusion.* *Nature* 620, 1089-1100. [10.1038/s41586-023-06415-8](https://doi.org/10.1038/s41586-023-06415-8). The backbone generator in the designability loop. Its license extends to its weights, which is less common than it should be.
- Buttenschoen, M., Morris, G.M. et al. (2024). *PoseBusters: AI-based docking methods fail to generate physically valid poses or generalise to novel sequences.* *Chemical Science* 15, 3130-3139. [10.1039/D3SC04185A](https://doi.org/10.1039/D3SC04185A). The paper that turns "100% valid" into a claim you have to defend, and the reason Appendix I measures geometry separately from graph legality.
- Roohani, Y.H., Hua, T.J. et al. (2025). *Virtual Cell Challenge: Toward a Turing test for the virtual cell.* *Cell* 188, 3370-3374. [10.1016/j.cell.2025.06.008](https://doi.org/10.1016/j.cell.2025.06.008). The challenge design behind H.9. Results arrived later in Arc Institute's [December 2025 wrap-up](https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up), which reported that perturbation prediction models were not yet consistently beating naive baselines across all metrics.
- Xu, Z., Ren, F. et al. (2025). *A generative AI-discovered TNIK inhibitor for idiopathic pulmonary fibrosis: a randomized phase 2a trial.* *Nature Medicine* 31, 2602-2610. [10.1038/s41591-025-03743-2](https://doi.org/10.1038/s41591-025-03743-2). Rentosertib. Seventy-one patients over twelve weeks, and the most-cited evidence that an AI-originated target can reach a clinical readout. Read the confidence intervals before the headlines.
