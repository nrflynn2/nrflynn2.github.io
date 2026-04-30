---
layout: page
title: Book
permalink: /book/
nav: true
nav_order: 2
description: Machine Learning for Drug Discovery is a practical Manning book on using PyTorch, cheminformatics, and modern ML to solve real pharmaceutical research problems.
og_image: https://noahrflynn.com/assets/img/og/book.png
---

<div class="row align-items-start mb-5">
  <div class="col-12 col-md-4 mb-4 mb-md-0 text-center">
    <img
      src="{{ '/assets/img/book_cover_manning.png' | relative_url }}"
      alt="Machine Learning for Drug Discovery book cover"
      class="img-fluid rounded z-depth-1"
      style="max-width: 280px;"
    >
  </div>
  <div class="col-12 col-md-8">
    <h2 class="mt-0">Machine Learning for Drug Discovery</h2>
    <p class="lead text-muted">Hands-on deep learning for pharmaceutical research, from molecular fingerprints to AlphaFold.</p>

    <p><strong>Status:</strong> all chapters are available in Manning MEAP, the manuscript is 100% complete, and the full release is estimated for Summer 2026.</p>

    <p>This book teaches machine learning and deep learning through real drug discovery case studies. Each chapter starts with a concrete pharmaceutical problem--screening antimalarial compounds, predicting cancer drug targets, generating new molecules--then walks through the code and modeling decisions needed to reproduce and extend the work in PyTorch.</p>

    <p>No chemistry background is required. If you know Python and basic ML, the book builds the molecular science as you go. If you are a chemist, biologist, or pharmacologist learning ML, the modeling concepts stay anchored in problems you already care about.</p>

    <p>Written during my PhD, sharpened while teaching at UC Berkeley, and informed by production AI work at Amazon scale and Google Cloud AI. It is the practical bridge I wanted when I started.</p>

    <div class="mt-4">
      <a
        href="https://www.manning.com/books/machine-learning-for-drug-discovery?utm_source=flynn&utm_medium=affiliate&utm_campaign=book_flynn_machine_2_29_24&a_aid=flynn&a_bid=ddb44578&chan=mm_website"
        class="btn btn-book-primary me-2"
        target="_blank"
        rel="noopener"
      >Get the Book &rarr;</a>
      <a
        href="https://github.com/nrflynn2/ml-drug-discovery"
        class="btn btn-book-secondary"
        target="_blank"
        rel="noopener"
      >View Code &rarr;</a>
    </div>
    <p class="mt-2" style="font-size: 0.85rem; color: var(--global-text-color-light);">
      Use code <strong>au35fly</strong> for 35% off
    </p>
  </div>
</div>

---

## Chapters

**Part 1: Fundamentals of Cheminformatics &amp; Machine Learning**

1. The Drug Discovery Process
2. Ligand-based Screening: Filtering &amp; Similarity Searching
3. Ligand-based Screening: Machine Learning
4. Solubility Deep Dive with Linear Models
5. Classification: Cytochrome P450 Inhibition
6. Case Study: Small Molecule Binding to an RNA Target
7. Unsupervised Learning: Repurposing Drugs, Curating Compounds, &amp; Screening Fragments

**Part 2: Deep Learning for Molecules &amp; Structural Biology**

{:start="8"}
8. Introduction to Deep Learning
9. Structure-based Drug Design with Active Learning
10. Generative Models for De Novo Design
11. Graph Neural Networks for Drug Target Affinity Prediction
12. Transformer Architectures for Protein Structure Prediction
13. Multimodal AI Systems for End-to-End Drug Discovery Pipelines

**Appendices**

- A: Glossary
- B: Chemical Data Repositories
- C: Knowledge Distillation: Shrinking Models for Efficient, Hierarchical Molecular Generation
- D: Technical Deep Dive into Protein Structure Prediction

---

## Testimonials

Early reader notes:

> "It's a compelling blend of machine learning and drug development insights. A must-read for anyone seeking to harness the power of AI in pharmaceutical innovation."
>
> --- **Meghal Gandhi**, Machine Learning Researcher, Charles R. Drew University of Medicine and Science

> "I would recommend this book to my colleagues by emphasizing its practical approach to applying machine learning in drug discovery. I'd highlight how it bridges the gap between technical concepts and real-world applications, making it an essential resource for anyone in healthcare or biotech looking to leverage AI/ML for innovation."
>
> --- **Srikanth Daggumalli**, Senior Analytics and AI Specialist Solutions Architect, Amazon Web Services

---

## Cite This Book

{% highlight bibtex %}
@book{flynn2025mldd,
  title     = {Machine Learning for Drug Discovery},
  author    = {Flynn, Noah},
  isbn      = {9781633437661},
  year      = {2025},
  publisher = {Manning Publications}
}
{% endhighlight %}

<style>
.btn-book-primary {
  background-color: var(--global-hover-color);
  color: #fff !important;
  border: 1px solid var(--global-hover-color);
  padding: 0.5rem 1.2rem;
  border-radius: 999px;
  font-weight: 500;
  font-size: 0.95rem;
  text-decoration: none !important;
  display: inline-block;
  transition: background-color 160ms ease, border-color 160ms ease, color 160ms ease;
}
.btn-book-primary:hover {
  background-color: var(--global-theme-color);
  border-color: var(--global-theme-color);
  color: #fff !important;
}
.btn-book-secondary {
  background-color: transparent;
  color: var(--global-text-color) !important;
  border: 1px solid var(--global-divider-color);
  padding: 0.5rem 1.2rem;
  border-radius: 999px;
  font-weight: 500;
  font-size: 0.95rem;
  text-decoration: none !important;
  display: inline-block;
  transition: border-color 160ms ease, color 160ms ease;
}
.btn-book-secondary:hover {
  border-color: var(--global-theme-color);
  color: var(--global-hover-color) !important;
}
</style>
