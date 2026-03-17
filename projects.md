---
layout: single
title: Projects
permalink: /projects/
---

<style>

/* Expand page width beyond default theme container */
.page__content {
  max-width: 1400px;
}

/* Intro text */
.projects-intro {
  margin-bottom: 2rem;
  font-size: 1.1rem;
  max-width: 900px;
}

/* Project grid */
.project-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 2rem;
}

@media (min-width: 900px) {
  .project-grid {
    grid-template-columns: 1fr 1fr;
  }
}

/* Project card */
.project-card {
  background: #111827;
  border: 1px solid #2a2f3a;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 10px 28px rgba(0,0,0,.22);
  color: #e8eaf0;
  transition: transform .2s ease, box-shadow .2s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 18px 40px rgba(0,0,0,.28);
}

/* Card image */
.project-card img {
  display: block;
  width: 100%;
  height: 360px;
  object-fit: cover;
}

/* Card body */
.project-card-body {
  padding: 1.6rem;
}

/* Title */
.project-card h2 {
  margin-top: 0;
  margin-bottom: 1rem;
  font-size: 1.45rem;
  line-height: 1.25;
  color: #ffffff;
}

/* Description */
.project-card p {
  color: #cfd6e3;
  line-height: 1.7;
  margin-bottom: 1.2rem;
}

/* Bullet list */
.project-meta {
  margin: 0 0 1rem 0;
  padding-left: 1.1rem;
}

.project-meta li {
  margin-bottom: .5rem;
  color: #d8dbe3;
}

/* Tags */
.project-tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-top: 1rem;
}

.project-tag {
  padding: .35rem .7rem;
  border-radius: 999px;
  background: #263247;
  color: #e8eaf0;
  font-size: .85rem;
  border: 1px solid #3a4a61;
}

.project-coming {
  border: 1px dashed #3a4a61;
  background: #0f141b;
}

.project-note {
  margin-top: .75rem;
  font-size: .95rem;
  opacity: .85;
}

</style>

# Projects

<div class="projects-intro">
Here are a few projects that reflect my interest in infrastructure, automation, web development, and building practical systems with real-world use.
</div>

<div class="project-grid">

<div class="project-card">

<img src="/assets/images/projects/homelab-setup.jpg">

<div class="project-card-body">

<h2>Home Lab Infrastructure</h2>

<p>
I built a personal home lab to explore infrastructure, security, virtualization, and network-based storage in a hands-on environment. It functions as a safe place to test systems, manage services, and build practical IT skills outside of production environments.
</p>

<ul class="project-meta">
<li>Built a virtualized environment using VirtualBox</li>
<li>Deployed a Windows Server Domain Controller with Active Directory</li>
<li>Designed network topologies using Cisco Packet Tracer</li>
<li>Automated system configuration with Python and PowerShell</li>
<li>Configured centralized storage accessible across the network</li>
</ul>

<div class="project-tag-row">
<span class="project-tag">Virtualization</span>
<span class="project-tag">Active Directory</span>
<span class="project-tag">Networking</span>
<span class="project-tag">PowerShell</span>
<span class="project-tag">Python</span>
<span class="project-tag">Infrastructure</span>
</div>

</div>
</div>

<div class="project-card">

<img src="/assets/images/projects/homelab-power.jpg">

<div class="project-card-body">

<h2>Home Lab Design Goals</h2>

<p>
Beyond being a technical learning environment, the lab is designed to support security experimentation and centralized network storage. It allows me to test infrastructure concepts safely while gaining experience with real system administration workflows.
</p>

<ul class="project-meta">
<li>Security testing within an isolated network environment</li>
<li>Centralized storage accessible across devices on the network</li>
<li>Hands-on experience with system administration</li>
<li>Infrastructure designed to expand as new projects are added</li>
</ul>

<div class="project-tag-row">
<span class="project-tag">Security</span>
<span class="project-tag">Storage</span>
<span class="project-tag">Infrastructure</span>
<span class="project-tag">System Administration</span>
</div>

</div>
</div>

<div class="project-card project-coming">

<div class="project-card-body">

<h2>Eco Champs Website</h2>

<p>
A custom website built for a nonprofit organization focused on environmental initiatives.
</p>

<div class="project-tag-row">
<span class="project-tag">Web Development</span>
<span class="project-tag">Nonprofit</span>
<span class="project-tag">Frontend</span>
</div>

<div class="project-note">
Full project details coming soon.
</div>

</div>
</div>

<div class="project-card project-coming">

<div class="project-card-body">

<h2>Web-Based Compost Tracker</h2>

<p>
A web application designed to track compost activity and environmental impact metrics.
</p>

<div class="project-tag-row">
<span class="project-tag">Web App</span>
<span class="project-tag">Sustainability</span>
<span class="project-tag">Data Tracking</span>
</div>

<div class="project-note">
Full project details coming soon.
</div>

</div>
</div>

<div class="project-card project-coming">

<div class="project-card-body">

<h2>Aerographix</h2>

<p>
My freelance drone photography and aerial media project focused on landscape, real estate, and creative aerial imagery.
</p>

<div class="project-tag-row">
<span class="project-tag">Drone Photography</span>
<span class="project-tag">Creative Work</span>
<span class="project-tag">Freelance</span>
</div>

<div class="project-note">
Full project details coming soon.
</div>

</div>
</div>

</div>


