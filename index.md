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
</style>

<main id="home">
  <header aria-labelledby="home-title">
    <p>Joseph Noonan · Developer</p>
    <h1 id="home-title">I build practical tools for real problems.</h1>
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
