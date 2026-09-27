---
layout: single
title: ""
permalink: /
---

<style>
/* Homepage only: static visual foundation */
body:has(#home) {
  background: #080d0b;
  color: #dce7df;
}
body:has(#home) .masthead,
body:has(#home) .greedy-nav,
body:has(#home) .page__footer {
  background: #080d0b;
  color: #dce7df;
  border-color: #20372b;
}
body:has(#home) .masthead a,
body:has(#home) .greedy-nav a,
body:has(#home) .page__footer a {
  color: #dce7df;
}
body:has(#home) .page {
  width: 100%;
  padding: 0;
}
body:has(#home) .page__inner-wrap {
  float: none;
  margin: 0;
}
body:has(#home) .page__content {
  margin: 0;
  padding: 0;
}
body:has(#home) .page__title {
  display: none;
}
#home {
  --home-bg: #080d0b;
  --home-panel: #101a15;
  --home-panel-soft: #0d1511;
  --home-border: #244032;
  --home-text: #e8f0e9;
  --home-muted: #a7b9ac;
  --home-green: #99e5a9;
  box-sizing: border-box;
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 clamp(1.25rem, 4vw, 3rem) 5rem;
  color: var(--home-text);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
#home *, #home *::before, #home *::after { box-sizing: inherit; }
#home a {
  color: var(--home-green);
  text-underline-offset: .24em;
  text-decoration-thickness: 1px;
}
#home a:focus-visible {
  outline: 2px solid var(--home-green);
  outline-offset: 5px;
  border-radius: 3px;
}
#home > header {
  min-height: 590px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  padding: 6rem 0 6.5rem;
  border-bottom: 1px solid var(--home-border);
  background: radial-gradient(ellipse 48% 55% at 83% 45%, #173525 0%, transparent 85%);
}
#home > header > p:first-child {
  margin: 0 0 1.75rem;
  color: var(--home-green);
  font-size: .76rem;
  font-weight: 700;
  letter-spacing: .19em;
  text-transform: uppercase;
}
#home h1, #home h2, #home h3 {
  color: var(--home-text);
  font-family: inherit;
  letter-spacing: -.045em;
}
#home h1 {
  max-width: 850px;
  margin: 0;
  font-size: clamp(3.1rem, 7.5vw, 6.8rem);
  line-height: 1.04;
  font-weight: 680;
}
#home > header > p:nth-of-type(2) {
  max-width: 660px;
  margin: 2rem 0 0;
  color: var(--home-muted);
  font-size: clamp(1.05rem, 1.8vw, 1.3rem);
  line-height: 1.65;
}
#home nav[aria-label="Homepage links"] {
  display: flex;
  flex-wrap: wrap;
  gap: .85rem;
  margin-top: 2.5rem;
}
#home nav[aria-label="Homepage links"] a {
  display: inline-block;
  padding: .8rem 1.15rem;
  border: 1px solid var(--home-border);
  border-radius: 7px;
  color: var(--home-text);
  font-size: .9rem;
  font-weight: 650;
  text-decoration: none;
}
#home nav[aria-label="Homepage links"] a:first-child {
  background: var(--home-green);
  border-color: var(--home-green);
  color: #07120b;
}
#home > section { padding: 5.5rem 0; border-bottom: 1px solid var(--home-border); }
#home h2 { margin: 0 0 1.25rem; font-size: clamp(2rem, 4vw, 3.4rem); line-height: 1.13; }
#home > section > p {
  max-width: 660px;
  margin: 0 0 2rem;
  color: var(--home-muted);
  font-size: 1.05rem;
  line-height: 1.75;
}
#home section[aria-labelledby="approach-title"] {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(290px, .85fr);
  column-gap: clamp(2rem, 7vw, 7rem);
  align-items: start;
}
#home section[aria-labelledby="approach-title"] h2 { grid-column: 1; }
#home section[aria-labelledby="approach-title"] > p { grid-column: 1; }
#home section[aria-labelledby="approach-title"] ul {
  grid-column: 2;
  grid-row: 1 / span 2;
  margin: 0;
  padding: .4rem 0 0;
  list-style: none;
}
#home section[aria-labelledby="approach-title"] li {
  padding: 1.15rem 0;
  border-bottom: 1px solid var(--home-border);
  color: var(--home-muted);
  line-height: 1.6;
}
#home section[aria-labelledby="approach-title"] li:first-child { padding-top: 0; }
#home strong { color: var(--home-text); }
#home section[aria-labelledby="work-title"] {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}
#home section[aria-labelledby="work-title"] > h2,
#home section[aria-labelledby="work-title"] > p { grid-column: 1 / -1; }
#home section[aria-labelledby="work-title"] > p { margin-bottom: 1.4rem; }
#home article {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  min-height: 260px;
  padding: clamp(1.5rem, 3vw, 2.3rem);
  background: var(--home-panel-soft);
  border: 1px solid var(--home-border);
  border-radius: 12px;
}
#home article:first-of-type {
  grid-column: 1 / -1;
  min-height: 300px;
  background: linear-gradient(125deg, #13271b, #0d1511 72%);
}
#home article h3 { margin: 0 0 1rem; font-size: clamp(1.4rem, 2.3vw, 2rem); line-height: 1.2; }
#home article p { max-width: 680px; margin: 0 0 1rem; color: var(--home-muted); line-height: 1.65; }
#home article a { margin-top: auto; padding-top: 1.5rem; font-weight: 650; }
#home > footer {
  padding: 5.5rem 0 2rem;
}
#home > footer p { max-width: 580px; color: var(--home-muted); font-size: 1.08rem; }
#home > footer a { display: inline-block; margin: .8rem 1.6rem .4rem 0; font-weight: 650; }
@media (max-width: 760px) {
  #home > header { min-height: 0; padding: 5rem 0; background-position: center; }
  #home > section { padding: 4rem 0; }
  #home section[aria-labelledby="approach-title"],
  #home section[aria-labelledby="work-title"] { display: block; }
  #home section[aria-labelledby="approach-title"] ul { margin-top: 2rem; }
  #home article { min-height: 0; margin-top: 1rem; }
  #home > footer { padding-top: 4rem; }
}

/* Phase 3.1: scroll reveals */
@media (prefers-reduced-motion: no-preference) {
  #home.motion-ready .reveal:not(.is-visible) {
    opacity: 0;
    transform: translate3d(0, 18px, 0);
  }
  #home.motion-ready .reveal {
    transition:
      opacity .7s cubic-bezier(.22, 1, .36, 1),
      transform .8s cubic-bezier(.22, 1, .36, 1);
    transition-delay: var(--reveal-delay, 0ms);
  }
}
@media (prefers-reduced-motion: reduce) {
  #home.motion-ready .reveal {
    opacity: 1;
    transform: none;
    transition: none;
  }
}

/* Phase 3.2: attention states */
#home article,
#home nav[aria-label="Homepage links"] a,
#home section[aria-labelledby="approach-title"] li,
#home article a,
#home > footer a {
  transition-property: transform, background-color, border-color, box-shadow, color;
  transition-duration: .32s;
  transition-timing-function: cubic-bezier(.22, 1, .36, 1);
}
#home article:focus-within {
  border-color: #72b984;
  background-color: #14251a;
  box-shadow: 0 16px 42px rgba(0, 0, 0, .22), inset 0 0 0 1px rgba(153, 229, 169, .1);
}
#home nav[aria-label="Homepage links"] a:focus-visible {
  border-color: var(--home-green);
  box-shadow: 0 0 0 4px rgba(153, 229, 169, .12);
}
#home nav[aria-label="Homepage links"] a:first-child:focus-visible {
  background: #b8efc2;
}
#home nav[aria-label="Homepage links"] a:not(:first-child):focus-visible {
  background: #15271b;
}
#home article > a::after {
  content: "";
  display: inline-block;
  width: .43em;
  height: .43em;
  margin-left: .45em;
  border-top: 1.5px solid currentColor;
  border-right: 1.5px solid currentColor;
  opacity: 0;
  transform: translate(-4px, 3px) rotate(45deg);
  transition: opacity .25s ease, transform .35s cubic-bezier(.22, 1, .36, 1);
}
#home article:focus-within > a::after {
  opacity: 1;
  transform: translate(0, 0) rotate(45deg);
}
#home > footer a:focus-visible { color: #d8ffe0; }
@media (hover: hover) and (pointer: fine) {
  body:has(#home) .masthead a:hover { color: #b8efc2; }
  #home nav[aria-label="Homepage links"] a:hover { transform: translateY(-3px); }
  #home nav[aria-label="Homepage links"] a:first-child:hover {
    background: #b8efc2;
    border-color: #b8efc2;
    box-shadow: 0 10px 28px rgba(66, 147, 83, .16);
  }
  #home nav[aria-label="Homepage links"] a:not(:first-child):hover {
    border-color: #72b984;
    background: #15271b;
  }
  #home section[aria-labelledby="approach-title"] li:hover {
    transform: translateX(5px);
    border-color: #5b936a;
  }
  #home section[aria-labelledby="approach-title"] li:hover strong { color: var(--home-green); }
  #home article:hover {
    transform: translateY(-5px);
    border-color: #72b984;
    box-shadow: 0 16px 42px rgba(0, 0, 0, .22), inset 0 0 0 1px rgba(153, 229, 169, .1);
  }
  #home article:hover > a::after { opacity: 1; transform: translate(0, 0) rotate(45deg); }
  #home > footer a:hover { color: #d8ffe0; }
}
@media (prefers-reduced-motion: reduce) {
  #home article,
  #home nav[aria-label="Homepage links"] a,
  #home section[aria-labelledby="approach-title"] li,
  #home article a,
  #home article > a::after,
  #home > footer a { transition: none; }
  #home nav[aria-label="Homepage links"] a:hover,
  #home section[aria-labelledby="approach-title"] li:hover,
  #home article:hover { transform: none; }
}

#home .header-link { display: none; }

/* Phase 3.3: ambient breathing, with stationary text */
#home > header,
#home article,
#home > footer {
  position: relative;
  isolation: isolate;
}
#home > header { overflow: hidden; }
#home > header > *,
#home article > *,
#home > footer > * { position: relative; z-index: 1; }
#home > header::before,
#home article::before,
#home > footer::before {
  content: "";
  position: absolute;
  pointer-events: none;
  z-index: 0;
}
#home > header::before {
  inset: 2% -12% 0 34%;
  background: radial-gradient(ellipse at 55% 47%, rgba(73, 163, 99, .31), transparent 65%);
  opacity: .42;
  transform: scale(.96);
}
#home article::before {
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(ellipse at 82% 12%, rgba(119, 212, 141, .18), transparent 57%);
  opacity: .24;
}
#home > footer::before {
  width: 42%;
  height: 100%;
  right: 0;
  top: 0;
  background: radial-gradient(ellipse at center, rgba(80, 158, 97, .14), transparent 70%);
  opacity: .28;
}
@media (prefers-reduced-motion: no-preference) {
  @keyframes home-breathe {
    0%, 100% { opacity: .26; transform: scale(.96); }
    38% { opacity: .52; transform: scale(1.065); }
    73% { opacity: .34; transform: scale(1.015); }
  }
  @keyframes surface-breathe {
    0%, 100% { opacity: .16; transform: scale(1); }
    43% { opacity: .38; transform: scale(1.035); }
    79% { opacity: .22; transform: scale(1.01); }
  }
  #home > header::before { animation: home-breathe 14.3s cubic-bezier(.45, 0, .3, 1) infinite; }
  #home article::before { animation: surface-breathe 11.6s ease-in-out infinite; }
  #home article:nth-of-type(2)::before { animation-duration: 13.4s; animation-delay: -4.2s; }
  #home article:nth-of-type(3)::before { animation-duration: 10.8s; animation-delay: -6.8s; }
  #home > footer::before { animation: surface-breathe 16.1s ease-in-out infinite; animation-delay: -3.5s; }
}

/* Visible but restrained rhythm cues */
#home > header > p:first-child::before,
#home > footer h2::after {
  content: "";
  display: inline-block;
  width: .55rem;
  height: .55rem;
  border-radius: 50%;
  background: var(--home-green);
  box-shadow: 0 0 0 5px rgba(153, 229, 169, .1);
  opacity: .8;
  vertical-align: middle;
}
#home > header > p:first-child::before { margin-right: .85rem; }
#home > footer h2::after { margin-left: .6rem; }
#home article::after {
  content: "";
  position: absolute;
  z-index: 2;
  pointer-events: none;
  top: 0;
  left: clamp(1.5rem, 3vw, 2.3rem);
  width: 42px;
  height: 2px;
  border-radius: 2px;
  background: var(--home-green);
  opacity: .7;
  transform-origin: left center;
}
@media (prefers-reduced-motion: no-preference) {
  @keyframes accent-breathe {
    0%, 100% { opacity: .48; transform: scale(.8); }
    41% { opacity: 1; transform: scale(1.22); }
    76% { opacity: .68; transform: scale(.94); }
  }
  @keyframes line-breathe {
    0%, 100% { opacity: .36; transform: scaleX(.64); }
    46% { opacity: .9; transform: scaleX(1.15); }
    78% { opacity: .55; transform: scaleX(.86); }
  }
  #home > header > p:first-child::before { animation: accent-breathe 4.8s cubic-bezier(.45, 0, .3, 1) infinite; }
  #home > footer h2::after { animation: accent-breathe 5.6s ease-in-out infinite; animation-delay: -2s; }
  #home article::after { animation: line-breathe 6.9s ease-in-out infinite; }
  #home article:nth-of-type(2)::after { animation-duration: 8.1s; animation-delay: -3s; }
  #home article:nth-of-type(3)::after { animation-duration: 7.4s; animation-delay: -5s; }
}

/* Phase 3 refinement: a shared breathing rhythm across primary elements */
#home .hero-accent { color: #b4efc0; }
#home nav[aria-label="Homepage links"] a {
  position: relative;
  isolation: isolate;
  overflow: hidden;
}
#home nav[aria-label="Homepage links"] a::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: radial-gradient(ellipse at 50% 100%, rgba(255, 255, 255, .3), transparent 75%);
  opacity: .18;
}
#home nav[aria-label="Homepage links"] a:not(:first-child)::before {
  background: radial-gradient(ellipse at 50% 100%, rgba(130, 226, 150, .32), transparent 75%);
}
#home > section > h2 {
  position: relative;
}
#home > section > h2::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -1px;
  width: 84px;
  height: 2px;
  border-radius: 2px;
  background: var(--home-green);
  transform-origin: left center;
}
#home section[aria-labelledby="approach-title"] li {
  position: relative;
  padding-left: 1.25rem;
}
#home section[aria-labelledby="approach-title"] li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 1.85rem;
  width: .42rem;
  height: .42rem;
  border-radius: 50%;
  background: var(--home-green);
  opacity: .75;
  box-shadow: 0 0 0 4px rgba(153, 229, 169, .08);
}
#home section[aria-labelledby="approach-title"] li:first-child::before { top: .72rem; }
#home article::after { width: 68px; height: 3px; }
#home > footer a::after {
  content: "";
  display: inline-block;
  width: .35rem;
  height: .35rem;
  margin-left: .55rem;
  border-radius: 50%;
  background: currentColor;
  vertical-align: middle;
  opacity: .75;
}
@media (prefers-reduced-motion: no-preference) {
  @keyframes headline-breathe {
    0%, 100% { color: #e8f0e9; text-shadow: 0 0 0 rgba(116, 228, 142, 0); }
    43% { color: #99e5a9; text-shadow: 0 0 26px rgba(116, 228, 142, .24); }
    77% { color: #c9f0d0; text-shadow: 0 0 12px rgba(116, 228, 142, .1); }
  }
  @keyframes light-breathe {
    0%, 100% { opacity: .08; transform: scale(.92); }
    44% { opacity: .55; transform: scale(1.12); }
    78% { opacity: .22; transform: scale(1); }
  }
  #home .hero-accent { animation: headline-breathe 9.2s ease-in-out infinite; }
  #home nav[aria-label="Homepage links"] a::before { animation: light-breathe 7.3s ease-in-out infinite; }
  #home nav[aria-label="Homepage links"] a:nth-child(2)::before { animation-duration: 8.6s; animation-delay: -2.7s; }
  #home > section > h2::after { animation: line-breathe 7.8s ease-in-out infinite; }
  #home section[aria-labelledby="work-title"] > h2::after { animation-duration: 9.1s; animation-delay: -3.3s; }
  #home section[aria-labelledby="approach-title"] li::before { animation: accent-breathe 5.7s ease-in-out infinite; }
  #home section[aria-labelledby="approach-title"] li:nth-child(2)::before { animation-duration: 6.5s; animation-delay: -2s; }
  #home section[aria-labelledby="approach-title"] li:nth-child(3)::before { animation-duration: 5.9s; animation-delay: -4s; }
  #home > footer a::after { animation: accent-breathe 5.8s ease-in-out infinite; }
  #home > footer a:last-child::after { animation-delay: -2.6s; animation-duration: 6.7s; }
}
</style>

<main id="home">
  <header aria-labelledby="home-title">
    <p>Joseph Noonan · Developer</p>
    <h1 id="home-title">I build practical tools for <span class="hero-accent">real problems.</span></h1>
    <p>
      I work across interfaces, backend logic, and data to make useful systems
      clear and dependable. This is a selection of what I have built and how I think.
    </p>
    <nav aria-label="Homepage links">
      <a href="/projects/">Explore my work</a>
      <a href="#contact">Get in touch</a>
    </nav>
  </header>

  <section aria-labelledby="approach-title">
    <h2 id="approach-title">How I work</h2>
    <p>
      I like taking a process that feels cumbersome and making it easier to use.
      My projects combine thoughtful interfaces with the less visible work:
      validation, data structure, automation, and documentation.
    </p>
    <ul>
      <li><strong>Full-stack development:</strong> HTML, CSS, JavaScript, PHP, and MySQL.</li>
      <li><strong>Automation:</strong> Python scripts that remove repetitive upkeep.</li>
      <li><strong>Product thinking:</strong> workflows that people can understand and use.</li>
    </ul>
  </section>

  <section aria-labelledby="work-title">
    <h2 id="work-title">Selected work</h2>
    <p>Projects that show how I turn an idea into a working system.</p>

    <article aria-labelledby="compost-title">
      <h3 id="compost-title">Compost Tracker</h3>
      <p>
        A full-stack tool for Victory Garden Initiative that replaces paper and
        spreadsheet tracking with compost entry logging, calculations, reports,
        and role-based access for administrators and volunteers.
      </p>
      <p>My role: system design, frontend, PHP backend, MySQL database, and documentation.</p>
      <a href="/projects/">Read the case study</a>
    </article>

    <article aria-labelledby="portfolio-title">
      <h3 id="portfolio-title">Portfolio and photo gallery</h3>
      <p>
        A Jekyll site with custom pages and a gallery whose image manifest is
        generated by a Python script, making collection updates easier to manage.
      </p>
      <a href="/gallery/">Explore the gallery</a>
    </article>

    <article aria-labelledby="dashboard-title">
      <h3 id="dashboard-title">Remote Work Dashboard</h3>
      <p>
        A browser-based dashboard bringing together weather, public GitHub activity,
        calendar entries, and a locally stored task list.
      </p>
      <a href="/dashboard/">Open the dashboard</a>
    </article>
  </section>

  <footer id="contact" aria-labelledby="contact-title">
    <h2 id="contact-title">Let’s connect</h2>
    <p>Interested in the work or want to talk through a project?</p>
    <a href="https://github.com/noonan-portfolio">Find me on GitHub</a>
    <a href="/about/">More about me</a>
  </footer>
</main>

<script>
(() => {
  const home = document.getElementById('home');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const groups = home.querySelectorAll(':scope > section, :scope > footer');
  const targets = [];

  groups.forEach(group => {
    const items = group.querySelectorAll(':scope > h2, :scope > p, :scope > ul > li, :scope > article, :scope > a');
    items.forEach((item, index) => {
      item.classList.add('reveal');
      item.style.setProperty('--reveal-delay', Math.min(index, 3) * 75 + 'ms');
      targets.push(item);
    });
  });

  let observer;
  function configureReveals() {
    observer?.disconnect();
    if (reducedMotion.matches || !('IntersectionObserver' in window)) {
      home.classList.remove('motion-ready');
      return;
    }
    home.classList.add('motion-ready');
    observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -5% 0px' });
    targets.filter(item => !item.classList.contains('is-visible')).forEach(item => observer.observe(item));
  }

  configureReveals();
  reducedMotion.addEventListener('change', configureReveals);
})();
</script>
