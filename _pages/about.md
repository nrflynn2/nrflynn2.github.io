---
layout: default
title: About
permalink: /
home_work_brand: true
selected_papers: true
description: Noah Flynn builds production AI systems, agentic research workflows, and machine learning tools for drug discovery.
---

<main class="home-redesign">
  <section class="home-hero">
    <div>
      {% include eyebrow.html text="Senior Research Scientist · Google Cloud AI" %}
      <h1 class="home-hero-title">AI systems for <span class="home-hero-highlight">agents, science, and drug discovery.</span></h1>
      <p class="home-hero-lead">
        I build production AI systems and research agents, write practical machine learning for
        pharmaceutical science, and teach molecular software engineering at UC Berkeley. This site is
        the canonical home for my writing, book, talks, and research.
      </p>
      <div class="home-hero-actions">
        <a class="brand-button-primary" href="{{ '/blog/' | relative_url }}">Read Blog &rarr;</a>
        <a class="brand-button-ghost" href="{{ '/book/' | relative_url }}">Book &rarr;</a>
        <a class="brand-button-ghost" href="{{ '/cv/' | relative_url }}">CV &rarr;</a>
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

  <section class="home-section" aria-labelledby="latest-posts-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Blog" %}
        <h2 id="latest-posts-heading">Latest posts</h2>
      </div>
      <div class="home-section-links">
        <a class="home-section-link" href="{{ '/blog/' | relative_url }}">All posts &rarr;</a>
        <a class="home-section-link" href="{{ '/feed.xml' | relative_url }}">RSS &rarr;</a>
        <a class="home-section-link" href="{{ site.substack_url }}" target="_blank" rel="noopener">Substack &rarr;</a>
      </div>
    </div>
    {% include latest_posts.liquid %}
  </section>

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
        <p>Starting as a Senior Research Scientist on Google Cloud AI's Gemini Enterprise team, building agentic systems for deep research, coding, and data science workflows.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Writing</span>
        <p><em>Machine Learning for Drug Discovery</em> is 100% complete with Manning and nearing full release: real case studies, PyTorch code, and practical molecular science.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Teaching</span>
        <p>Teaching graduate molecular science and software engineering at UC Berkeley, from RDKit and PyTorch to graph neural networks and generative design.</p>
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
      {% include work-row.html year="2026" title="DREAM" venue="Preprint" type="Paper" href="/publications/#li2026dreambench" %}
      {% include work-row.html year="2026" title="COMPASS" venue="TMLR / arXiv" type="Paper" href="/publications/#flynn2025compass" %}
      {% include work-row.html year="2024" title="Amazon Nova Family of Models" venue="Amazon AGI" type="Model" href="/publications/#amazonnova2024" %}
      {% include work-row.html year="2025" title="Designing Medicines from Scratch" venue="PyTorch Conference" type="Talk" href="/talks/" %}
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
