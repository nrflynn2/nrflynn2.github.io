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
      A small page for the parts of life that do not fit neatly into papers, products, or a CV:
      getting outside, going somewhere new, staying curious, and building communities where technical
      ideas feel a little more human.
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
        <p>Lake Tahoe is my favorite winter reset: a place to trade screens for snow, movement, and a different kind of focus.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Scuba</span>
        <p>I like traveling to new places to scuba dive. It is hard to beat learning a place by seeing what is happening under the surface.</p>
      </div>
      <div class="now-item">
        <span class="now-item-label">Learning</span>
        <p>I like being a beginner. New subjects, tools, and skills have a way of improving the work you thought was unrelated.</p>
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
        <h2 id="community-heading">Builder Energy Beyond the Day Job</h2>
      </div>
    </div>
    <p>
      These are not hobbies in the narrow sense, but they belong on a personal page because they show
      what I tend to care about outside my formal role: helping technical ideas become teachable,
      fundable, public, and useful.
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
          <span class="work-row-description">Translated PhD research into a B2B commercialization proposal that won 1st place and $20K in pre-seed funding.</span>
        </span>
        <span class="work-row-meta">Boston, MA</span>
        <span class="work-row-type">Venture</span>
      </div>
      <div class="work-row">
        <span class="work-row-year">2016-2017</span>
        <span>
          <span class="work-row-title">Director, UIUC Engineering Open House</span>
          <span class="work-row-description">Led an educational nonprofit and public engineering showcase built around hands-on demonstrations, student teams, and community outreach.</span>
        </span>
        <span class="work-row-meta">Champaign, IL</span>
        <span class="work-row-type">Community</span>
      </div>
    </div>
  </section>
</main>
