---
layout: single
title: ""
permalink: /
---

<style>
.page__content {
  max-width: 1000px;
  margin: 0 auto;
}

/* HERO LAYOUT */
.page__content .home-hero {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 2.5rem;
  padding: 3.5rem 2rem;
  border-radius: 20px;
  background: linear-gradient(135deg, #f8fafc 0%, #eef3f8 100%);
  box-shadow: 0 18px 45px rgba(15, 23, 42, 0.08);
  border: 1px solid rgba(148, 163, 184, 0.18);
}

/* PROFILE IMAGE */
.page__content .profile-wrap {
  flex-shrink: 0;
}

.page__content .profile-img {
  width: 140px;
  height: 140px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
  border: 3px solid white;
}

/* HERO TEXT */
.page__content .hero-text {
  text-align: left;
  max-width: 600px;
}

.page__content .hero-text h1 {
  font-size: 2.8rem;
  margin-bottom: 0.5rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: #111827;
}

.page__content .home-subtext {
  font-size: 1.2rem;
  color: #475569;
  min-height: 1.6rem;
  margin-bottom: 1.2rem;
}

/* BUTTONS */
.page__content .button-row {
  margin-top: 0.5rem;
}

.page__content .home-btn {
  display: inline-block;
  margin: 0.3rem;
  padding: 0.7rem 1.2rem;
  border-radius: 10px;
  text-decoration: none !important;
  font-weight: 600;
  border: 1px solid #0f172a;
  background: #0f172a;
  color: white !important;
  transition: all 0.2s ease;
  box-shadow: 0 8px 18px rgba(15, 23, 42, 0.12);
}

.page__content .home-btn:hover {
  transform: translateY(-2px);
  background: #1e293b;
}

.page__content .home-btn.secondary {
  background: transparent;
  color: #0f172a !important;
  border: 1px solid #cbd5e1;
  box-shadow: none;
}

.page__content .home-btn.secondary:hover {
  background: #f1f5f9;
}

/* TEXT BLOCK */
.page__content .intro-block {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #334155;
  max-width: 800px;
  margin: 3rem auto 0 auto;
  text-align: center;
}

/* SECTION TITLES */
.page__content h2 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  color: #111827;
}

.page__content .section-kicker {
  color: #64748b;
  font-size: 0.95rem;
}

/* HIGHLIGHTS */
.page__content .highlights-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.page__content .highlight-pill {
  background: linear-gradient(135deg, #111827, #1e293b);
  color: white;
  border-radius: 14px;
  padding: 1rem;
  text-align: center;
}

.page__content .highlight-number {
  font-size: 1.3rem;
  font-weight: 700;
}

.page__content .highlight-label {
  font-size: 0.9rem;
  opacity: 0.9;
}

/* CARDS */
.page__content .quick-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.2rem;
  margin-top: 1rem;
}

.page__content .quick-card {
  background: white;
  border-radius: 14px;
  padding: 1.2rem;
  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
  border: 1px solid rgba(148, 163, 184, 0.15);
  transition: all 0.2s ease;
}

.page__content .quick-card:hover {
  transform: translateY(-4px);
}

/* FEATURED */
.page__content .featured-box {
  margin-top: 1rem;
  background: white;
  border-radius: 16px;
  padding: 1.8rem;
  box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
}

/* MOBILE */
@media (max-width: 768px) {
  .page__content .home-hero {
    flex-direction: column;
    text-align: center;
  }

  .page__content .hero-text {
    text-align: center;
  }
}
</style>

<!-- HERO -->
<div class="home-hero">
  <div class="profile-wrap">
    <img src="/assets/images/profile.jpg" class="profile-img" alt="Joseph Noonan">
  </div>

  <div class="hero-text">
    <h1>Hi, I'm Joseph Noonan</h1>
    <div class="home-subtext" id="typed-line"></div>

    <div class="button-row">
      <a class="home-btn" href="/projects/">View Projects</a>
      <a class="home-btn secondary" href="/gallery/">Photo Gallery</a>
      <a class="home-btn secondary" href="/about/">About Me</a>
    </div>
  </div>
</div>

<!-- INTRO -->
<div class="intro-block">
  <p>
    I’m an aspiring technology professional focused on IT, automation, front-end development,
    and building digital tools that are useful, polished, and easy to navigate.
  </p>

  <p>
    This portfolio brings together my technical projects, photography, and ongoing work
    as I continue developing my skills and building systems that solve real problems.
  </p>
</div>

<!-- HIGHLIGHTS -->
<div class="home-section">
  <div class="section-kicker"></div>
  <h2>Site Highlights</h2>

  <div class="highlights-strip">
    <div class="highlight-pill">
      <span class="highlight-number">5+</span>
      <span class="highlight-label">Custom Pages</span>
    </div>

    <div class="highlight-pill">
      <span class="highlight-number">100+</span>
      <span class="highlight-label">Images</span>
    </div>

    <div class="highlight-pill">
      <span class="highlight-number">Python</span>
      <span class="highlight-label">Automation</span>
    </div>

    <div class="highlight-pill">
      <span class="highlight-number">JS</span>
      <span class="highlight-label">Frontend</span>
    </div>
  </div>
</div>

<!-- BUILT -->
<div class="home-section">
  <div class="section-kicker"></div>
  <h2>What I've Built</h2>

  <div class="quick-grid">
    <div class="quick-card">
      <strong>Portfolio Website</strong>
      <p>Built with GitHub Pages and Jekyll with custom styling and interactivity.</p>
    </div>

    <div class="quick-card">
      <strong>Dynamic Photo Gallery</strong>
      <p>Loads images dynamically from a JSON manifest generated automatically.</p>
    </div>

    <div class="quick-card">
      <strong>Automation Script</strong>
      <p>Python tool that scans folders and updates gallery data automatically.</p>
    </div>

    <div class="quick-card">
      <strong>Dashboard</strong>
      <p>Project focused on productivity and useful real-world data display.</p>
    </div>
  </div>
</div>

<!-- FEATURED -->
<div class="home-section">
  <div class="section-kicker"></div>
  <h2>Featured Work</h2>

  <div class="featured-box">
    <h3 id="featured-title"></h3>
    <p id="featured-text"></p>
    <a class="home-btn" id="featured-link" href="#">View More</a>
  </div>
</div>

<script>
const typingLines = [
  "I build practical digital projects.",
  "I enjoy automation and problem-solving.",
  "I focus on clean and efficient design."
];

let lineIndex = 0;
let charIndex = 0;
let removing = false;
const typedLine = document.getElementById("typed-line");

function updateTyping() {
  const current = typingLines[lineIndex];

  if (!removing) {
    typedLine.textContent = current.slice(0, charIndex + 1);
    charIndex++;
    if (charIndex === current.length) {
      removing = true;
      setTimeout(updateTyping, 1200);
      return;
    }
  } else {
    typedLine.textContent = current.slice(0, charIndex - 1);
    charIndex--;
    if (charIndex === 0) {
      removing = false;
      lineIndex = (lineIndex + 1) % typingLines.length;
    }
  }

  setTimeout(updateTyping, removing ? 30 : 60);
}

updateTyping();
</script>
