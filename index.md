---
layout: single
title: ""
permalink: /
---

<style>
.home-hero {
  text-align: center;
  margin-top: 2rem;
}

.home-hero h1 {
  font-size: 2.4rem;
  margin-bottom: 0.4rem;
}

.home-subtext {
  font-size: 1.15rem;
  color: #6b7280;
  min-height: 1.6rem;
}

.home-section {
  margin-top: 3rem;
}

.quick-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.quick-card {
  background: #f8f8f8;
  border: 1px solid #dddddd;
  border-radius: 10px;
  padding: 1rem;
}

.featured-box {
  margin-top: 1rem;
  background: #f8f8f8;
  border: 1px solid #dddddd;
  border-radius: 12px;
  padding: 1.5rem;
}

.featured-box h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.button-row {
  margin-top: 1rem;
}

.home-btn {
  display: inline-block;
  margin: 0.3rem;
  padding: 0.55rem 1rem;
  border: 1px solid #333333;
  border-radius: 6px;
  text-decoration: none;
  color: #333333;
  transition: 0.2s ease;
}

.home-btn:hover {
  background: #333333;
  color: white;
  text-decoration: none;
}
</style>

<div class="home-hero">
  <h1>Hi, I'm Joseph Noonan</h1>
  <div class="home-subtext" id="typed-line"></div>

  <div class="button-row">
    <a class="home-btn" href="/projects/">View Projects</a>
    <a class="home-btn" href="/gallery/">Photo Gallery</a>
    <a class="home-btn" href="/about/">About Me</a>
  </div>
</div>

<div class="home-section">
  <p>
    I'm an aspiring technology professional with interests in IT, automation,
    web development, and building digital tools that are useful, efficient,
    and easy to navigate.
  </p>

  <p>
    This portfolio brings together my projects, photography, and ongoing work
    as I continue developing my technical skills.
  </p>
</div>

<div class="home-section">
  <h2>What I've Built</h2>

  <div class="quick-grid">
    <div class="quick-card">
      <strong>Portfolio Website</strong>
      <p>A custom site built with GitHub Pages, Jekyll, HTML, CSS, and JavaScript.</p>
    </div>

    <div class="quick-card">
      <strong>Dynamic Photo Gallery</strong>
      <p>A responsive gallery that loads images from a generated JSON manifest.</p>
    </div>

    <div class="quick-card">
      <strong>Automation Workflow</strong>
      <p>A Python script that scans folders and updates the gallery automatically.</p>
    </div>

    <div class="quick-card">
      <strong>Personal Dashboard</strong>
      <p>A dashboard project focused on productivity, organization, and useful data display.</p>
    </div>
  </div>
</div>

<div class="home-section">
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
  "I enjoy automation, problem-solving, and clean design.",
  "I'm always looking for better ways to organize and improve workflows."
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
      setTimeout(updateTyping, 1400);
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

  setTimeout(updateTyping, removing ? 35 : 70);
}

updateTyping();

const featuredProjects = [
  {
    title: "Dynamic Photo Gallery",
    text: "Built a category-based gallery with a masonry layout, lightbox viewing, and a Python-generated image manifest.",
    link: "/gallery/"
  },
  {
    title: "Portfolio Website",
    text: "Designed and deployed this site using GitHub Pages and Jekyll, with custom styling and interactive features.",
    link: "/"
  },
  {
    title: "Automated Workflow",
    text: "Created a Python script to scan gallery folders and automatically rebuild the JSON file used by the site.",
    link: "/projects/"
  }
];

let featureIndex = 0;

function rotateFeature() {
  const item = featuredProjects[featureIndex];
  document.getElementById("featured-title").textContent = item.title;
  document.getElementById("featured-text").textContent = item.text;
  document.getElementById("featured-link").href = item.link;

  featureIndex = (featureIndex + 1) % featuredProjects.length;
}

rotateFeature();
setInterval(rotateFeature, 4500);
</script>
