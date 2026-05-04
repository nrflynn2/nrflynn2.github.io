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
    <div class="home-hero-copy">
      <p class="eyebrow home-hero-eyebrow">Senior Research Scientist · Google Cloud AI · Gemini Enterprise</p>
      <h1 class="home-hero-title">AI Systems for <span class="home-hero-highlight">Agents, Science, and Medicine.</span></h1>
    </div>
    <aside class="home-hero-aside" aria-label="Portrait">
      <img
        class="home-hero-photo"
        src="{{ '/0062Flynn_Noah-Retouched.png' | relative_url }}"
        alt="Noah Flynn"
      >
    </aside>
    <div class="home-hero-bottom">
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
  </section>

  {% include book-band.html %}

  <section class="home-section" aria-labelledby="latest-posts-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Blog" %}
        <h2 id="latest-posts-heading">Latest Posts</h2>
      </div>
      <div class="home-section-links">
        <a class="home-section-link" href="{{ '/blog/' | relative_url }}">All posts &rarr;</a>
        <a class="home-section-link" href="{{ '/feed.xml' | relative_url }}">RSS &rarr;</a>
        <a class="home-section-link" href="{{ site.substack_url }}" target="_blank" rel="noopener">Substack &rarr;</a>
      </div>
    </div>
    {% include latest_posts.liquid %}
  </section>

  <section class="home-bio" aria-labelledby="bio-heading">
    <div class="home-bio-header">
      {% include eyebrow.html text="About" %}
      <h2 id="bio-heading">Noah Flynn</h2>
    </div>
    <div class="home-bio-copy">
      <p>
        I am a Senior Research Scientist at Google Cloud AI, where I work on Gemini Enterprise. My current work focuses on agentic AI systems for deep research, coding, and data science workflows: the practical pieces of getting models to reason over long context, use tools, and produce work people can trust.
      </p>
      <p>
        Before Google, I was an Applied Scientist at AWS Agentic AI and a Research Scientist on Amazon's Alexa and AGI team, where I contributed to the Amazon Nova model family. Across those roles, I worked on foundation model adaptation, tool use, evaluation, multilingual data selection, and production release cycles.
      </p>
      <p>
        My scientific background is in deep learning for drug discovery. I earned my PhD in Computational Biology at Washington University in St. Louis, with research on graph neural networks for drug metabolism and toxicity, and I have worked at AbbVie and Merck on gene regulatory network analysis and generative compound design.
      </p>
      <p>
        I teach graduate machine learning and cheminformatics at UC Berkeley, and wrote <a href="{{ '/book/' | relative_url }}">Machine Learning for Drug Discovery</a> to make that intersection easier to enter. I am always glad to hear from people building at the boundary of agentic AI, computational drug discovery, and scientific software.
      </p>
      <div class="home-bio-cta">
        <p>Working on a research collaboration, invited talk, or teaching project around AI systems or computational drug discovery?</p>
        <a class="brand-button-primary" href="https://www.linkedin.com/in/{{ site.linkedin_username }}" target="_blank" rel="noopener">Reach Out &rarr;</a>
      </div>
    </div>
    <div class="home-bio-focus" aria-labelledby="current-focus-heading">
      <h3 class="home-bio-subheading" id="current-focus-heading">Current Focus</h3>
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
    </div>
  </section>

  <section class="home-section" aria-labelledby="selected-work-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Selected Work" %}
        <h2 id="selected-work-heading">Research, Teaching, and Tools</h2>
      </div>
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
        <h2 id="selected-publications-heading">Recent Publication Highlights</h2>
      </div>
      <a class="home-section-link" href="{{ '/publications/' | relative_url }}">All publications &rarr;</a>
    </div>
    {% include selected_papers.liquid %}
  </section>
</main>
