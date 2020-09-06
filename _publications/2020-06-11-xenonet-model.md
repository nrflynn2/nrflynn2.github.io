---
title: "XenoNet: Inference and Likelihood of Intermediate Metabolite Formation"
collection: publications
permalink: /publication/2020-06-11-xenonet-model
excerpt: ''
date: 2020-06-11
venue: 'Journal of Chemical Information and Modeling'
citation: 'Noah R. Flynn, Na Le Dang, Michael D. Ward, and S. Joshua Swamidass, Journal of Chemical Information and Modeling 2020 60 (7), 3431-3449, DOI: 10.1021/acs.jcim.0c00361'

---

[Paper can be accessed here.](https://pubs.acs.org/doi/abs/10.1021/acs.jcim.0c00361)

## Abstract

Drug metabolism is a common cause of adverse drug reactions. Drug molecules can be metabolized into reactive metabolites, which can conjugate to biomolecules, like protein and DNA, in a process termed bioactivation. To mitigate adverse reactions caused by bioactivation, both experimental and computational screening assays are utilized. Experimental assays for assessing the formation of reactive metabolites are low throughput and expensive to perform, so they are often reserved until later stages of the drug development pipeline when the drug candidate pools are already significantly narrowed. In contrast, computational methods are high throughput and cheap to perform to screen thousands to millions of compounds for potentially toxic molecules during the early stages of the drug development pipeline. Commonly used computational methods focus on detecting and structurally characterizing reactive metabolite–biomolecule adducts or predicting sites on a drug molecule that are liable to form reactive metabolites. However, such methods are often only concerned with the structure of the initial drug molecule or of the adduct formed when a biomolecule conjugates to a reactive metabolite. Thus, these methods are likely to miss intermediate metabolites that may lead to subsequent reactive metabolite formation. To address these shortcomings, we create XenoNet, a metabolic network predictor, that can take a pair of a substrate and a target product as input and (1) enumerate pathways, or sequences of intermediate metabolite structures, between the pair, and (2) compute the likelihood of those pathways and intermediate metabolites. We validate XenoNet on a large, chemically diverse data set of 17 054 metabolic networks built from a literature-derived reaction database. Each metabolic network has a defined substrate molecule that has been experimentally observed to undergo metabolism into a defined product metabolite. XenoNet can predict experimentally observed pathways and intermediate metabolites linking the input substrate and product pair with a recall of 88 and 46%, respectively. Using likelihood scoring, XenoNet also achieves a top-one pathway and intermediate metabolite accuracy of 93.6 and 51.9%, respectively. We further validate XenoNet against prior methods for metabolite prediction. XenoNet significantly outperforms all prior methods across multiple metrics. XenoNet is available at https://swami.wustl.edu/xenonet.

## Citation
XenoNet: Inference and Likelihood of Intermediate Metabolite Formation. Noah R. Flynn, Na Le Dang, Michael D. Ward, and S. Joshua Swamidass, Journal of Chemical Information and Modeling 2020 60 (7), 3431-3449 DOI: 10.1021/acs.jcim.0c00361

