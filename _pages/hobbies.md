---
layout: default
permalink: /hobbies/
title: Hobbies
nav: true
nav_order: 8
description: A more personal page about skiing, scuba diving, travel, learning, and community work.
home_work_brand: true
---

<main class="work-redesign">
  <header class="work-page-header">
    <h1>Hobbies & Community</h1>
    <p>
      What I do when I'm not working on research or teaching.
    </p>
  </header>

  <section class="home-section" aria-labelledby="outside-heading">
    <div class="home-section-header">
      <div>
        {% include eyebrow.html text="Outside Work" %}
        <h2 id="outside-heading">What I Make Time For</h2>
      </div>
    </div>

    <div class="now-grid">
      <div class="now-item">
        <span class="now-item-label">Skiing</span>
        <p>Lake Tahoe most weekends in winter. It's the best way I've found to actually stop thinking about work for a few hours.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Scuba</span>
        <p>I try to dive somewhere new whenever I travel. You learn a lot about a place by seeing what's going on underwater.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Learning</span>
        <p>I like being a beginner. Picking up a new subject or skill tends to make everything else click a little differently.</p>
      </div>
      {% comment %}
      <div class="now-item">
        <span class="now-item-label">Travel</span>
        <p>Travel keeps me alert to different ways people build, teach, eat, move, and solve problems.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Making</span>
        <p>I am drawn to projects that turn abstract ideas into something people can touch, use, question, or teach from.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Conversation</span>
        <p>Some of my favorite technical moments start as ordinary conversation: a whiteboard, a half-formed question, and enough time to follow it.</p>
      </div>
      {% endcomment %}
    </div>
  </section>

  <section class="work-section" aria-labelledby="community-heading">
    <div class="work-section-header">
      <div>
        {% include eyebrow.html text="Community" %}
        <h2 id="community-heading">Select Projects I've Enjoyed Beyond my Day Job</h2>
      </div>
    </div>
    <p>
      I spend a lot of time outside my day job helping people take technical work and make it teachable or fundable.
    </p>

    <div class="work-list">
      <div class="work-row">
        <span class="work-row-year">2025</span>
        <span>
          <span class="work-row-title">Berkeley SkyDeck Technical Advisor</span>
          <span class="work-row-description">Advising early-stage founders where AI, science, technical strategy, and product judgment meet.</span>
        </span>
        <span class="work-row-meta">Berkeley, CA</span>
        <span class="work-row-type">Advising</span>
      </div>
      <div class="work-row">
        <span class="work-row-year">2022</span>
        <span>
          <span class="work-row-title">Boston University New Venture Competition</span>
          <span class="work-row-description">Turned my PhD research into a B2B commercialization proposal. Won 1st place and $20K in pre-seed funding.</span>
        </span>
        <span class="work-row-meta">Boston, MA</span>
        <span class="work-row-type">Venture</span>
      </div>
      <div class="work-row">
        <span class="work-row-year">2016-2017</span>
        <span>
          <span class="work-row-title">Director, UIUC Engineering Open House</span>
          <span class="work-row-description">Ran an educational nonprofit and public engineering showcase — hands-on demos, student teams, community outreach.</span>
        </span>
        <span class="work-row-meta">Champaign, IL</span>
        <span class="work-row-type">Community</span>
      </div>
    </div>
  </section>
</main>