---
layout: "post"
title: "Virtual cells for target discovery, perturbation models, and benchmarks"
date: "2026-06-19 09:00:00-0700"
description: "Virtual cell models try to predict how cells respond to genetic and chemical perturbations. A practitioner's guide to what they can do for target discovery, what the benchmarks say, and where the current limits still matter."
tags:
  - "machine learning"
  - "drug discovery"
  - "target discovery"
  - "single-cell"
categories:
  - "target discovery"
toc:
  sidebar: true
giscus_comments: false
thumbnail: "/assets/img/og/default.png"
og_image: "https://noahrflynn.com/assets/img/og/default.png"
series: "Drug Target Discovery"
series_order: 8
faq_schema: |
  {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "What is a virtual cell model?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "A virtual cell model is a learned model of cellular state transitions. Given a starting cell state and an intervention, such as a gene knockdown, CRISPR perturbation, drug exposure, cytokine treatment, or combination, it predicts a likely next state or readout. In current drug-discovery workflows, the output is usually a transcriptomic response, pathway shift, cell-state embedding, morphology profile, viability phenotype, or related assay readout. A virtual cell is not a whole human in software and does not replace experimental biology. Its practical role is to rank target-validation experiments before a team runs expensive perturbation screens."
        }
      },
      {
        "@type": "Question",
        "name": "How do virtual cells help target discovery?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Virtual cells help target discovery by turning candidate targets into intervention hypotheses. A team can start with disease-relevant cells, encode the baseline cell state, specify a perturbation such as knocking down a target gene, predict the response, and rank which perturbations should move into wet-lab validation. This adds a functional layer to evidence frameworks, tissue-specificity analysis, druggability assessment, and knowledge graphs. The model does not prove that a target will work clinically, but it can decide which targets deserve Perturb-seq, organoid, animal-model, or other validation spending."
        }
      },
      {
        "@type": "Question",
        "name": "What data do virtual cell models need?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Virtual cell models depend on large single-cell atlases, perturbation datasets, and increasingly multimodal readouts. Single-cell RNA-seq atlases provide baseline cell states across tissues and diseases. Perturb-seq and related CRISPR screens connect an intervention label to a single-cell transcriptional response. Drug-perturbation datasets add chemical interventions across many cell contexts. Imaging, spatial transcriptomics, protein abundance, chromatin accessibility, secreted factors, and viability readouts are important because RNA alone is an upstream proxy for the phenotypes drug discovery ultimately cares about."
        }
      },
      {
        "@type": "Question",
        "name": "Are virtual cells ready to replace lab experiments?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "No. Virtual cells are best understood as experiment-prioritization tools, not replacements for lab validation. Benchmarks such as the 2025 Virtual Cell Challenge show that perturbation prediction remains hard, especially when models must generalize to held-out cell types or unfamiliar interventions. Many models still predict RNA rather than protein-level, morphological, electrophysiological, immune, safety, or clinical outcomes. A useful deployment should include uncertainty estimates, abstention when the model is outside its training distribution, and prospective experimental validation."
        }
      },
      {
        "@type": "Question",
        "name": "What is the Virtual Cell Challenge?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "The Virtual Cell Challenge is a benchmark launched by the Arc Institute in 2025 to test whether models can predict transcriptional responses to perturbations in a held-out cell type. The first challenge asked computational models to stand in for a Perturb-seq experiment using approximately 300,000 single-cell RNA-seq profiles from H1 human embryonic stem cells with 300 CRISPRi perturbations. The early results were intentionally sobering: many models struggled against simple baselines on some metrics. That makes the challenge valuable because it measures context generalization rather than polished demonstrations."
        }
      }
    ]
  }
---
A target-discovery team has narrowed an inflammatory disease program to two candidate genes. Both are differentially expressed in diseased tissue. One has modest human-genetic support and sits in a pathway already implicated by patient samples. The other is newer, more cell-state specific, and easier to imagine dosing safely.

The next step is experimental. Knock each gene down in the relevant cell type and measure the transcriptional response. See whether the disease program shifts. Then decide which target deserves deeper validation. A virtual cell model moves part of that workflow into computation. Given a starting cell state and a perturbation, it predicts what the cell is likely to do next.

That is the useful claim. A virtual cell is not a whole human in software or a substitute for biology. It is a learned model of cellular state transitions, usually trained on single-cell atlases plus perturbation data, and used to rank experiments before the lab runs them.

For target discovery, that is enough. The field has spent decades asking whether a target matters. Virtual cells recast that question in intervention terms by asking what happens when a gene is reduced, a pathway is blocked, or a cell population sees a drug.

## Why virtual cells matter in 2026

Target discovery already asks whether a target is linked to disease, expressed in the right tissue, and supported by network or multi-omics evidence. Virtual cells pick up at the next step. Once a target looks plausible on paper, the practical question is how a relevant cell state changes when the team perturbs it.

Three changes made that question computationally serious. Single-cell atlases are now large enough to serve as training corpora. Perturbation datasets have moved from boutique experiments to industrial scale. Public benchmarks are finally testing whether models generalize instead of rewarding polished demos.

First, single-cell scale is no longer hypothetical. Public atlases contain tens to hundreds of millions of cells, and platforms such as CZ CELLxGENE make those data usable as model-training corpora. Models such as Geneformer, scGPT, scFoundation, AIDO.Cell, Universal Cell Embeddings, and TranscriptFormer treat gene-expression profiles as structured biological objects that can be embedded, compared, and transferred across tissues or species.

Second, perturbation data now exist at sizes that can train models rather than merely illustrate them. Perturb-seq combines CRISPR-based perturbation with single-cell RNA sequencing, so each perturbed cell carries both the intervention label and the transcriptomic readout. Genome-scale Perturb-seq has already been run across millions of human cells.

Drug-perturbation datasets are larger still. Tahoe-100M contains 100 million single cells across 50 cancer models and 1,100 drug perturbations, and the 2026 Tahoe, Arc Institute, and Biohub partnership announced a plan to generate more than 120 million cells across 225,000 drug-patient interactions (Tahoe Therapeutics, 2025 and 2026).

Third, the field now faces real benchmark pressure. In 2025, the Arc Institute launched the Virtual Cell Challenge to test whether models can predict transcriptional responses to perturbations in a held-out cell type. The first round did not produce an AlphaFold-style breakaway win. On some metrics, many models struggled against naive baselines. That makes the benchmark more useful, not less. It marks where the field is ready for deployment and where it is still doing research.

> **Concept Translation:** A virtual cell is a learned transition model for biology. The input is a cell state plus an intervention. The output is a predicted next state or readout. In reinforcement-learning terms, the cell is the state, the perturbation is the action, and the transcriptomic or phenotypic response is the transition. The catch is observability. RNA counts are a narrow sensor, not the whole cell.

That ambiguity matters because target discovery does not return a clean software object called `target`. It returns a probabilistic, context-dependent intervention hypothesis. Virtual cells do not remove that uncertainty. They make it easier to interrogate.

## What a virtual cell actually predicts

The phrase "virtual cell" covers several model classes. In drug-discovery writing, it is often stretched beyond its useful meaning.

A virtual cell model predicts cellular behavior under conditions that were not directly measured. The condition might be a gene knockout, gene knockdown, CRISPR activation, small-molecule exposure, cytokine treatment, disease context, species transfer, or a combination. The output might be a transcriptome, a protein-expression profile, an image-derived morphology vector, a viability phenotype, a pathway score, or a cell-state label.

Near-term work still predicts RNA most of the time. That is a convenience rather than the endpoint biology cares about. Single-cell RNA-seq is high-throughput, broadly available, and already organized into public atlases. It also gives a rich readout of cell state, but the tradeoff is clear. Drug targets are usually proteins, safety phenotypes can be electrophysiological or immunological, and clinical endpoints sit far downstream. In practice, virtual-cell models operate as assay models and sit well upstream of clinical-response modeling.

In practice, the workflow is direct.

1. Start with disease-relevant cells, ideally patient-derived cells or a strong surrogate.
2. Encode the baseline cell state, including cell type, disease state, and any available molecular context.
3. Specify a perturbation, such as knocking down a candidate target or exposing the cell to a tool compound.
4. Predict the response, often as differential expression, pathway activation, or movement in a learned cell-state space.
5. Rank perturbations for wet-lab validation.
6. Feed the validation data back into the model or the next screen.

That loop is much narrower than "simulate biology." It is active learning for target validation.

Three model layers show up repeatedly.

**Cell-state encoders.** These models map a single-cell profile into an embedding. The embedding can support cell-type annotation, disease-state classification, batch correction, cross-species transfer, and clustering. Geneformer, scGPT, scFoundation, Universal Cell Embeddings, AIDO.Cell, and TranscriptFormer mostly live here, although several also support perturbation tasks.

**Perturbation response predictors.** These models try to predict how gene expression changes after an intervention. CPA, GEARS, scGen, scGenePT, TxPert, STATE, and newer virtual-cell systems belong here. GEARS is a useful reference point because it predicts transcriptional outcomes of multi-gene perturbations using a graph of gene relationships, which makes the link to knowledge graphs explicit.

**Multimodal virtual instruments.** The 2024 *Cell* virtual-cell perspective uses the phrase "virtual instruments" for models that expose the cell through different readouts. One instrument may predict RNA, another protein localization, another imaging morphology, and another pathway response. That matters because target discovery rarely fails on RNA alone. It fails when the downstream phenotype does not follow.

## The data substrate for virtual cells

Virtual cells are data-hungry because cells have many degrees of freedom. A mammalian cell has tens of thousands of transcripts, thousands of proteins, many possible states, and many interventions that can push it around. Scaling a language model mostly means collecting more text. Scaling a virtual cell means collecting more cells under controlled perturbations.

The data come from five main sources.

**Reference atlases.** CZ CELLxGENE, Tabula Sapiens, the Human Cell Atlas, GTEx-derived resources, organoid atlases, and disease-specific single-cell collections provide baseline cell states. They teach the model what a cell type looks like across tissues, donors, diseases, and species. Their best use is representation learning.

**Genetic perturbation screens.** Perturb-seq, CRISPRi, CRISPRa, and CROP-seq-style methods create labeled intervention data. Replogle and colleagues showed genome-scale Perturb-seq across more than 2.5 million human cells, using CRISPRi to target expressed genes and read out transcriptional phenotypes. This is the core signal for predicting what happens when a gene is reduced or activated.

**Chemical perturbation screens.** Drug perturbations connect target biology to pharmacology. They are messier than genetic perturbations because drugs have dose, exposure time, uptake, polypharmacology, metabolism, and off-target activity. They are also closer to the real question in drug discovery. A target perturbation asks what happens when the target changes. A drug perturbation asks what happens when a molecule enters a cell and hits whatever it actually hits.

**Imaging and spatial data.** RNA readouts lose morphology and tissue architecture. Image-based profiling, spatial transcriptomics, subcellular localization data, and multiplexed protein imaging put some of that structure back into the model. This is where virtual cells begin to connect with tissue specificity and on-target, off-tissue safety.

**Clinical and patient-derived context.** Patient-derived organoids, ex vivo tumor samples, disease tissue atlases, and electronic health record-linked molecular data are the route from cell models toward patient stratification. This layer is thin compared with public atlas data. It is also the layer that matters most for translation.

Scale alone is not enough. Coverage matters more than raw cell count. A hundred million cells from a narrow set of cancer cell lines will not teach the model how a macrophage behaves in fibrotic lung tissue. A perturbation-rich dataset can teach intervention response in one assay and still fail on another platform, donor population, or disease model.

This ambiguity is also a data problem. A cell-line perturbation is not the same object as a patient-tissue perturbation. A transcriptional response is not the same object as a clinical response. A virtual cell learns a conditional distribution over what it was shown. When the deployment setting changes, the model has to show that it transfers.

> **Concept Translation:** Scaling a virtual cell is closer to scaling a robotics dataset than scaling a language model. Text-based scaling laws exploit the fact that text is nearly free to collect at internet scale. Cellular perturbation data has to be generated experimentally - every additional perturbation × cell-type × dose × timepoint combination is a wet-lab experiment. The cost curve, the coverage problem, and the data-quality concerns are closer to robotics or autonomous-driving data collection than to LLM pretraining. That asymmetry shapes which scaling strategies actually pay off here.

## Model families behind virtual cells

Current models fall into four broad families.

### Foundation models for cell representations

Geneformer brought the language-model analogy into a form many ML readers immediately recognize. It treats a cell as an ordered sequence of expressed genes and pretrains a transformer over millions of single-cell transcriptomes. The original corpus covered roughly 30 million human single-cell transcriptomes. Later scaling work expanded the corpus beyond 100 million transcriptomes and reported scaling behavior across model sizes.

scGPT follows a related transformer approach, training on more than 33 million cells and supporting tasks such as batch correction, cell-type annotation, multi-omics integration, gene-network inference, and perturbation prediction. scFoundation scales in a different architectural direction, using a large model trained on more than 50 million cells with whole-transcriptome input space. TranscriptFormer extends the idea across species, with CZI reporting training on 112 million cells from 12 species and downstream use for cross-species cell-type and disease-state tasks.

> **Concept Translation:** Treating a cell as an ordered sequence of genes is the move that makes the rest of the foundation-model toolkit drop in. In NLP, a sentence is an ordered sequence of tokens; the transformer learns contextual embeddings by predicting masked tokens or next tokens given context. In Geneformer and scGPT, a cell is an ordered list of its expressed genes (typically ranked by expression level), and the transformer learns contextual gene embeddings by predicting masked genes given the rest of the cell. The architecture is the same. What changes is the vocabulary (genes instead of tokens), the corpus (single-cell transcriptomes instead of text), and the downstream tasks (cell-type classification, perturbation prediction). The same scaling arguments and pretraining intuitions apply, with the data-cost asymmetry above as the main caveat.

These models matter even when they fall short on perturbation prediction. Strong cell embeddings can surface rare disease states, align patient samples with reference atlases, and provide features for downstream target-prioritization models. That alone is already useful in target discovery.

### Perturbation predictors

Perturbation models sit closest to the virtual-cell promise. CPA learns a latent representation that separates basal cell state from perturbation effects. GEARS uses graph neural networks over gene relationships to predict responses to novel multi-gene perturbations. scGenePT injects gene-level language embeddings into a single-cell perturbation architecture. Tahoe-x1 trains a billion-parameter-scale model on perturbation-rich single-cell data, with explicit attention to genes, cells, and drugs.

The output is usually a vector of expression changes. That makes evaluation awkward. One model may capture the broad cell-state shift while missing a few disease-relevant genes. Another may rank the differentially expressed genes well while giving poor absolute values. A third may do well on global averages by predicting something close to the mean cell. A benchmark has to say which failure matters for the use case.

### Graph and knowledge-guided models

Virtual-cell prediction is also a graph problem. Genes already sit inside regulatory, signaling, and protein-interaction networks. Perturb one gene and the effect propagates through that graph. The knowledge-graph article made the same point at the level of target nomination. Here the same logic operates inside the cell.

GEARS is the clearest example for target-discovery readers because it uses a gene-gene knowledge graph to generalize from observed perturbations to unseen combinations. Graph-aware models such as GREmLN encode regulatory structure into attention mechanisms. Knowledge-guided world models such as VCWorld push further, trying to produce stepwise mechanistic predictions rather than only final output vectors.

The open question is how much explicit biological structure still helps once datasets become very large. In chemistry, learned representations and physics priors now coexist. Virtual cells are likely to settle into the same pattern. Scaling helps, but models that ignore known biology still throw away signal.

### Generative and world-model approaches

Some of the most ambitious virtual-cell papers describe world models that simulate cellular trajectories under intervention. Flow matching, diffusion-style generation, state-space models, and latent dynamical systems all point in that direction. The aim is to represent a path through cell states rather than a static expression vector.

> **Concept Translation:** "World model" is borrowed from reinforcement learning and robotics, where it means a learned dynamics model the agent can roll out in simulation to plan or imagine consequences before acting in the real environment. Used for cells, it means a model that predicts how cellular state evolves under a perturbation across time, not just what the endpoint looks like. The same questions that come up for RL world models - does it predict accurate trajectories, does it generalize to unseen actions, does it stay calibrated under longer rollouts - come up here too. The drug-discovery payoff is that the resulting model can be queried about dose timing, exposure duration, combination order, and resistance trajectories, not just final endpoints.

This matters for drug discovery because many therapeutic effects are temporal. A target may look safe at 6 hours and toxic at 6 days. A gene knockdown may shift a disease marker quickly, while the functional phenotype follows later. A virtual cell that predicts only one endpoint has limited reach. A virtual cell that predicts trajectories could guide dose, timing, combination order, and resistance hypotheses.

In 2026, "world model" often means "a model trained to predict perturbation-conditioned cell-state distributions." It is not a full simulator of cellular physiology.

## Benchmarks for virtual cells

Benchmarks are now the most useful part of the field because claims have outrun evidence.

The 2025 Virtual Cell Challenge framed the test in concrete terms. A computational model was asked to stand in for a Perturb-seq experiment. The challenge used approximately 300,000 single-cell RNA-seq profiles from H1 human embryonic stem cells with 300 CRISPRi perturbations. H1 cells created a distribution shift from common training data such as K562 and A375. That design forced context generalization rather than memorization.

> **Concept Translation:** The H1 vs K562/A375 design is the standard out-of-distribution generalization test from ML, applied to cell biology. K562 and A375 are the workhorse cell lines that dominate Perturb-seq training data - they are the in-distribution majority. Holding out H1 forces the model to predict perturbation responses in a cell type it has never seen perturbed. A model that succeeds is doing real generalization across cell-type domain shift; a model that fails is doing memorization of the training distribution. This is the same evaluation discipline that distinguishes a vision model that generalizes from one that overfits to ImageNet's specific photographic conventions.

The evaluation used three primary metrics.

**Perturbation Discrimination Score (PDS)** measured whether predicted perturbation effects were distinguishable from each other.

**Differential Expression Score (DES)** measured whether models identified the correct upregulated and downregulated genes.

**Mean Absolute Error (MAE)** measured gene-level prediction accuracy across the transcriptome.

The results were sobering in a productive way. Arc's wrap-up reported that perturbation prediction models were not consistently outperforming naive baselines across all metrics, although they improved on perturbation discrimination and differentially expressed gene identification. Winning approaches mixed deep learning with classical statistical features. Pure end-to-end learning did not settle the problem.

A *Nature Methods* benchmark reached a similar caution from a different angle. Ahlmann-Eltze, Huber, and Anders compared five foundation models and two other deep learning models against simple baselines for predicting transcriptome changes after single or double perturbations. None outperformed the baselines in their setup. The result shows that perturbation prediction is harder than cell embedding, and model papers need baselines simple enough to embarrass weak claims.

> **Concept Translation:** A naive baseline is the negative control for a model paper. If a transformer cannot beat "predict no change" or "add the two single perturbation effects," it has not learned the biological interaction the paper claims. The same discipline applies in docking against decoys or in testing a classifier against a majority-class predictor.

For target discovery, a benchmark should answer practical questions.

- Prediction of perturbation effects in a new cell type.
- Prediction for a new perturbation target when related genes were seen during training.
- Prediction of combinations where the single perturbations were seen but the pair was not.
- Recovery of disease-relevant differentially expressed genes rather than only the largest global shift.
- Prediction of functional endpoints such as viability, cytokine release, differentiation, or drug sensitivity.
- Uncertainty estimates calibrated well enough to guide experimental triage.

A target-discovery benchmark that cannot answer those questions is a model-quality benchmark, not a decision benchmark.

That is why AlphaFold analogies still overreach. The field looks closer to CASP before the jump, when the community was still deciding what useful prediction meant.

## How virtual cells change target discovery

Virtual cells add a new layer to the target-validation stack. They do not replace evidence frameworks, tissue-specificity analysis, druggability assessment, or knowledge graphs. They carry those pieces into a perturbation forecast.

### Candidate-target triage

A knowledge graph can nominate a target-disease edge. Human genetics can make that edge more credible. Tissue specificity can warn that modulation may be unsafe. A virtual cell adds the intervention question by predicting response in a relevant cell context.

Suppose a target is upregulated in diseased fibroblasts and sits near a fibrosis pathway in a knowledge graph. A virtual-cell workflow can simulate knockdown in disease-like fibroblast states and rank whether the predicted response moves away from the fibrotic program. That is not proof. It is a cheaper way to decide which targets deserve Perturb-seq, organoid testing, or animal studies.

### Screen design

Perturbation experiments are expensive because the search space is large. There are thousands of genes, many cell types, multiple disease contexts, and long lists of chemical interventions. Virtual cells can help choose the next experiment.

This is active learning in practice. The model proposes perturbations with high expected information gain or high expected therapeutic relevance, the lab runs the selected experiments, and the new data update the model. The aim is to cut wasted assays rather than chase perfect accuracy.

### Biomarker, combination, and resistance hypotheses

A target only matters in the patients whose disease biology depends on it. Virtual cells can test whether a perturbation response is specific to a cell state, genotype, subtype, or disease stage. If predicted target knockdown reverses a disease program only in cells carrying a particular pathway signature, that signature becomes a responder hypothesis. The same logic extends to combination settings, where synthetic lethality and drug synergy turn target discovery into a pair problem. GEARS-style models were built for multi-gene perturbation prediction, and newer generative approaches can represent response distributions under combinations.

Evaluation is the hard part. Additive baselines are strong. If perturbation A and perturbation B each have known effects, summing them will often work surprisingly well. A useful combination model has to find the cases where additivity breaks and show whether the deviation reflects synergy, buffering, toxicity, or assay noise.

### Tissue safety and cell-type specificity

On-target, off-tissue toxicity is already a target-selection problem. Virtual cells can sharpen that analysis. Instead of asking only where a target is expressed, ask how each cell type is predicted to respond when the target is perturbed.

That shift matters. Two cell types can express the same target and react very differently. One may tolerate inhibition because a backup pathway is active. Another may die or release inflammatory cytokines. A virtual cell that predicts response across cell types could turn expression atlases into functional safety screens.

This use case is still early, and RNA alone misses many safety phenotypes. Even so, the field is moving in the right direction, from maps of target location to predictions of cellular response after modulation.

## What virtual cells cannot do yet

The useful caution is more specific than "virtual cells are overhyped." Most models are trained on proxies for the thing drug discovery actually wants.

**RNA is not phenotype, and cell lines are not tissues.** A transcriptome can move in the right direction while protein activity, secretion, morphology, electrophysiology, or viability does not. This is the core mRNA-protein gap in target biology. RNA is easy to measure at scale, but drug effects live across more layers.

The model systems create another gap. Many perturbation datasets come from cell lines because they are scalable, yet cell lines lack immune context, vascular signaling, liver metabolism, microbiome effects, tissue stiffness, and developmental history. Patient-derived organoids and ex vivo systems help, but they are harder to scale and standardize.

**Coverage is sparse, and technical variation is easy to learn.** A model trained on a few thousand perturbations has seen a tiny slice of the intervention space. Even 225,000 drug-patient interactions cover only a small part of possible drugs, doses, combinations, cell states, and exposure times. Batch effects, donor effects, guide efficiency, multiplicity of infection, sequencing depth, dissociation stress, and dropout all create patterns a model can learn. A model that performs well inside one assay distribution can fail when the assay changes.

**Causality and translation remain the hardest gaps.** A perturbation experiment is closer to causal evidence than an observational atlas, but most models still see the intervention label and the outcome rather than the full causal path between them. A target-discovery decision needs mechanism in addition to prediction.

The clinical question is whether a drug helps a patient population. A virtual cell usually predicts a cellular readout in a model system, and many steps separate those two objects. The model can reduce uncertainty at one step. It cannot compress the whole pipeline into a software call.

These limits tell you how to use the models. They are strongest for ranking, triage, experiment design, and hypothesis generation. They are weakest when treated as proof that a target is validated.

## Where the field is heading

The next few years will decide whether virtual cells become routine target-discovery infrastructure or remain a research theme with polished demos.

Four directions matter most.

**Perturbation-rich data instead of larger atlases alone.** Atlases teach a model what cells look like. Perturbations teach it what cells do when pushed. The Tahoe, Arc, and Biohub partnership matters because it treats perturbation diversity as the bottleneck.

**Multimodal readouts.** RNA alone will not carry the field. Imaging, protein abundance, chromatin accessibility, secreted factors, viability, electrophysiology, and spatial position each answer different biological questions. A virtual cell that predicts several readouts can support target decisions better than one that predicts expression alone.

**Uncertainty and abstention.** A virtual cell used for target selection should know when it is outside its training distribution. Abstaining is a useful behavior. A confident wrong prediction can send a team into a wasted screen.

**Lab-in-the-loop learning.** The best near-term systems will look less like static foundation models and more like experimental-design engines. They will propose the next perturbation, observe the result, update the model, and repeat. That is a plausible way for ML to shorten the target-validation cycle without pretending to replace it.

Biology does not expose a clean `target_discovery(disease)` API. The useful destination is a tighter loop between hypothesis, perturbation, prediction, validation, and revision.

In 2026, the answer is mixed. Virtual-cell models already help organize single-cell data, align disease states, prioritize perturbation experiments, and generate target hypotheses. Benchmarks also show that perturbation prediction remains hard and that simple baselines still win in some settings. That is the right kind of progress.

A target hypothesis becomes more useful once it can be stress-tested as a perturbation forecast, and a virtual cell gives a team one more place to do that before the next round of validation spending.

---

## Further reading

- Bunne, C., Roohani, Y., Rosen, Y., Gupta, A. et al. (2024). *How to build the virtual cell with artificial intelligence: priorities and opportunities.* *Cell* 187, 7045-7063. The main field-defining perspective for AI virtual cells.

- Roohani, Y. H., Hua, T. J., Tung, P. Y. et al. (2025). *Virtual Cell Challenge: toward a Turing test for the virtual cell.* *Cell* 188, 3370-3374. The benchmark framing for perturbation-response prediction.

- Ahlmann-Eltze, C., Huber, W. and Anders, S. (2025). *Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines.* *Nature Methods* 22, 1657-1661. The cautionary benchmark paper every virtual-cell model claim should be read against.

- Roohani, Y. H., Huang, K. and Leskovec, J. (2024). *Predicting transcriptional outcomes of novel multigene perturbations with GEARS.* *Nature Biotechnology* 42, 927-935. A graph-learning reference point for perturbation prediction.

- Replogle, J. M. et al. (2022). *Mapping information-rich genotype-phenotype landscapes with genome-scale Perturb-seq.* *Cell* 185, 2559-2575.e28. A key data-generation paper for single-cell perturbation maps.

- Cui, H. et al. (2024). *scGPT: toward building a foundation model for single-cell multi-omics using generative AI.* *Nature Methods* 21, 1470-1480. A widely used transformer model for single-cell biology.

- Theodoris, C. V. et al. (2023). *Transfer learning enables predictions in network biology.* *Nature* 618, 616-624. The Geneformer paper and a useful example of transfer learning for gene-network dynamics.

- Hao, M. et al. (2024). *Large-scale foundation model on single-cell transcriptomics.* *Nature Methods* 21, 1481-1491. The scFoundation paper.

- CZI Virtual Cells Platform. A public platform for models, datasets, benchmarks, and workflows related to virtual cell modeling.

- Arc Institute Virtual Cell Challenge 2025 Wrap-Up. A clear public summary of the first challenge's results, including the role of baselines and hybrid methods.
