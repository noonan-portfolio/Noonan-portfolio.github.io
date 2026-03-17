---
layout: single
title: Projects
permalink: /projects/
---

<style>
.projects-intro {
  margin-bottom: 2rem;
  font-size: 1.05rem;
}

.project-grid {
  max-width: 1100px;
  margin: 1.5rem auto;
  display: grid;
  grid-template-columns: 1fr;
  gap: 2rem;
  margin-top: 1.5rem;
  margin-left: auto;
  margin-right: auto;
}

@media (min-width: 900px) {
  .project-grid {
    grid-template-columns: 1fr 1fr;
  }
}

.project-card {
  background: #111827;
  border: 1px solid #2a2f3a;
  border-radius: 18px;
  overflow: hidden;
  box-shadow: 0 8px 24px rgba(0,0,0,.18);
  color: #e8eaf0;
}

.project-card img {
  display: block;
  width: 100%;
  height: 360px;
  object-fit: cover;
}

.project-card-body {
  padding: 1.25rem;
}

.project-card h2 {
  margin-top: 0;
  margin-bottom: .75rem;
  font-size: 1.4rem;
  color: #ffffff;
}

.project-card p {
  margin-bottom: 1rem;
  color: #cfd6e3;
}

.project-meta {
  margin: 0 0 1rem 0;
  padding-left: 1.1rem;
}

.project-meta li {
  margin-bottom: .45rem;
  color: #d8dbe3;
}

.project-tag-row {
  display: flex;
  flex-wrap: wrap;
  gap: .5rem;
  margin-top: .75rem;
}

.project-tag {
  display: inline-block;
  padding: .35rem .7rem;
  border-radius: 999px;
  background: #263247;
  color: #e8eaf0;
  font-size: .9rem;
  border: 1px solid #3a4a61;
}

.project-note {
  margin-top: .75rem;
  font-size: .95rem;
  opacity: .9;
}

.project-coming {
  border: 1px dashed #3a4a61;
  background: #11151c;
}

.project-coming img {
  opacity: .9;
}

.section-title {
  margin-top: 2.5rem;
  margin-bottom: .75rem;
}
</style>



<div class="projects-intro">
  Here are a few projects that reflect my interest in infrastructure, automation, web development, and building practical systems with real-world use.
</div>

<div class="project-grid">

  <div class="project-card">
    <img src="/assets/images/projects/homelab-setup.jpg" alt="Home lab infrastructure setup">
    <div class="project-card-body">
      <h2>Home Lab Infrastructure</h2>
      <p>
        I built a personal home lab to explore infrastructure, security, virtualization, and network-based storage in a hands-on environment. It functions as a safe place to test systems, manage services, and build practical IT skills outside of production environments.
      </p>

      <ul class="project-meta">
        <li>Built a virtualized environment to simulate enterprise-style infrastructure</li>
        <li>Configured a Windows Server domain controller and Active Directory</li>
        <li>Practiced routing and switching concepts with Cisco Packet Tracer</li>
        <li>Used Python and PowerShell to automate configuration and repetitive tasks</li>
        <li>Designed the lab with security experimentation and shared network storage in mind</li>
      </ul>

      <div class="project-tag-row">
        <span class="project-tag">Virtualization</span>
        <span class="project-tag">Windows Server</span>
        <span class="project-tag">Active Directory</span>
        <span class="project-tag">PowerShell</span>
        <span class="project-tag">Python</span>
        <span class="project-tag">Networking</span>
      </div>
    </div>
  </div>

  <div class="project-card">
    <img src="/assets/images/projects/homelab-power.jpg" alt="Home lab power and infrastructure view">
    <div class="project-card-body">
      <h2>Home Lab Design Goals</h2>
      <p>
        Beyond being a technical learning environment, the lab is also designed to support secure experimentation and centralized storage across my network. It gives me a place to test new ideas, strengthen troubleshooting skills, and understand how systems work together at both the hardware and software level.
      </p>

      <ul class="project-meta">
        <li>Focus on security-oriented experimentation in an isolated environment</li>
        <li>Support for large-capacity storage accessible across the network</li>
        <li>Practical exposure to system administration and infrastructure planning</li>
        <li>Built to evolve over time as new services and projects are added</li>
      </ul>

      <div class="project-tag-row">
        <span class="project-tag">Infrastructure</span>
        <span class="project-tag">Security</span>
        <span class="project-tag">Storage</span>
        <span class="project-tag">System Administration</span>
      </div>
    </div>
  </div>

  <div class="project-card project-coming">
    <div class="project-card-body">
      <h2>Eco Champs Website</h2>
      <p>
        A custom website project built for a nonprofit organization. This section will showcase the planning, design, and development work involved in creating a web presence for a mission-driven group.
      </p>

      <div class="project-tag-row">
        <span class="project-tag">Web Design</span>
        <span class="project-tag">Frontend Development</span>
        <span class="project-tag">Client Project</span>
      </div>

      <div class="project-note">
        Full project details and visuals will be added here.
      </div>
    </div>
  </div>

  <div class="project-card project-coming">
    <div class="project-card-body">
      <h2>Web-Based Compost Tracker</h2>
      <p>
        A web application concept focused on tracking compost activity, environmental impact, and sustainability-related data. This project will highlight both technical implementation and mission-driven problem solving.
      </p>

      <div class="project-tag-row">
        <span class="project-tag">Web App</span>
        <span class="project-tag">Tracking System</span>
        <span class="project-tag">Sustainability</span>
      </div>

      <div class="project-note">
        Full project details and visuals will be added here.
      </div>
    </div>
  </div>

  <div class="project-card project-coming">
    <div class="project-card-body">
      <h2>Aerographix</h2>
      <p>
        My freelance drone photography and aerial media project. This section will highlight the creative, technical, and business aspects of building and operating a drone-based visual service.
      </p>

      <div class="project-tag-row">
        <span class="project-tag">Drone Photography</span>
        <span class="project-tag">Creative Work</span>
        <span class="project-tag">Freelance</span>
      </div>

      <div class="project-note">
        Full project details and visuals will be added here.
      </div>
    </div>
  </div>

</div>

## Why These Projects Matter

These projects reflect the way I like to learn and build:

- solving real problems through technology
- working independently and troubleshooting complex systems
- improving through hands-on experimentation
- combining technical structure with creativity and long-term thinking


