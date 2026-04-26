---
layout: default
title: About
permalink: /
home_work_brand: true
selected_papers: true
---

<main class="home-redesign">
  <section class="home-hero">
    <div>
      {% include eyebrow.html text="Senior Research Scientist · Google" %}
      <h1 class="home-hero-title">Scalable, robust AI — <span class="home-hero-highlight">plainly written.</span></h1>
      <p class="home-hero-lead">
        I build agentic systems that generalize — across verticals, contexts, and the long tail of
        problems we ask research models to handle. This is where I publish what I learn.
      </p>
      <div class="home-hero-actions">
        <a class="brand-button-primary" href="{{ '/blog/' | relative_url }}">Read Blog &rarr;</a>
        <a class="brand-button-ghost" href="{{ '/cv/' | relative_url }}">About me &rarr;</a>
      </div>
    </div>
    <aside class="home-hero-aside" aria-label="Social links">
      <img
        class="home-hero-photo"
        src="{{ '/0062Flynn_Noah-Retouched.png' | relative_url }}"
        alt="Noah Flynn"
      >
      <div class="contact-icons">{% include social.liquid %}</div>
    </aside>
  </section>

  {% include book-band.html %}

  <section class="home-section" aria-labelledby="now-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Now" %}
        <h2 id="now-heading">Current focus</h2>
      </div>
    </div>
    <div class="now-grid">
      <div class="now-item">
        <span class="now-item-label">Research</span>
        <p>Starting as a Senior Research Scientist at Google, working on agentic frameworks that generalize across deep research, coding, and data science.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Writing</span>
        <p>Finishing Machine Learning for Drug Discovery with Manning — a hands-on tour of the ML that powers modern pharma, including a deep AlphaFold case study.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Teaching</span>
        <p>Teaching graduate ML + cheminformatics at UC Berkeley as an adjunct.</p>
      </div>
    </div>
  </section>

  <section class="home-section" aria-labelledby="selected-work-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Selected Work" %}
        <h2 id="selected-work-heading">Research, teaching, and tools</h2>
      </div>
      <a class="home-section-link" href="{{ '/work/' | relative_url }}">All work &rarr;</a>
    </div>
    <div class="work-list">
      {% include work-row.html year="2026" title="Machine Learning for Drug Discovery" venue="Manning" type="Book" href="/book/" %}
      {% include work-row.html year="2026" title="GenCircuit-RL" venue="Research" type="Paper" href="/publications/#flynn2026gencircuit" %}
      {% include work-row.html year="2025" title="COMPASS" venue="TMLR" type="Paper" href="/publications/#flynn2025compass" %}
      {% include work-row.html year="2024" title="Amazon Nova Family of Models" venue="Amazon AGI" type="Model" href="/publications/#amazonnova2024" %}
      {% include work-row.html year="2022" title="ML + cheminformatics teaching" venue="UC Berkeley" type="Teaching" href="/teaching/" %}
    </div>
  </section>

  <section class="home-publications" aria-labelledby="selected-publications-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Selected Publications" %}
        <h2 id="selected-publications-heading">Recent publication highlights</h2>
      </div>
      <a class="home-section-link" href="{{ '/publications/' | relative_url }}">All publications &rarr;</a>
    </div>
    {% include selected_papers.liquid %}
  </section>
</main>
