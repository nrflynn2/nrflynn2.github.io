---
layout: default
title: Work
permalink: /work/
description: Selected research, writing, models, talks, and teaching.
nav: true
nav_order: 2
home_work_brand: true
---

<main class="work-redesign">
  <header class="work-page-header">
    {% include eyebrow.html text="Work" %}
    <h1>Selected work</h1>
    <p>
      A compact index of research, writing, models, talks, and teaching. The underlying al-folio
      project collection remains in place; this page simply uses a denser row layout.
    </p>
  </header>

  <section class="work-section" aria-label="Selected work list">
    <div class="work-list">
      {% include work-row.html year="2026" title="Machine Learning for Drug Discovery" venue="Manning" type="Book" href="/book/" %}
      {% include work-row.html year="2026" title="GenCircuit-RL" venue="Research" type="Paper" href="/publications/#flynn2026gencircuit" %}
      {% include work-row.html year="2026" title="DreamBench" venue="Research" type="Paper" href="/publications/#li2026dreambench" %}
      {% include work-row.html year="2025" title="COMPASS" venue="Research" type="Paper" href="/publications/#flynn2025compass" %}
      {% include work-row.html year="2024" title="Amazon Nova Family of Models" venue="Amazon AGI" type="Model" href="/publications/#amazonnova2024" %}
      {% include work-row.html year="2024" title="Designing Medicines from Scratch" venue="PyTorch Conference" type="Talk" href="/news/" %}
      {% include work-row.html year="2022" title="ML + cheminformatics teaching" venue="UC Berkeley" type="Teaching" href="/teaching/" %}
    </div>
  </section>
</main>
