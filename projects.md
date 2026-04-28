---
layout: single
title: Projects
permalink: /projects/
---

<style>

.page__content .featured-project {

  margin-top: 2rem;

  margin-bottom: 4rem;

  padding: 2rem;

  border-radius: 18px;

  background: linear-gradient(135deg, #f8fafc 0%, #eef3f8 100%);

  border: 1px solid rgba(148, 163, 184, 0.18);

  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.08);

}

.page__content .featured-project .section-label {

  font-size: 0.95rem;

  color: #64748b;

  margin-bottom: 0.5rem;

}

.page__content .featured-project h2 {

  margin-top: 0;

  margin-bottom: 1rem;

  font-size: 2.2rem;

  color: #111827;

}

.page__content .featured-project h3 {

  margin-top: 0;

  margin-bottom: 0.75rem;

  font-size: 1.5rem;

  color: #0f172a;

}

.page__content .featured-project p,

.page__content .featured-project li {

  color: #334155;

  line-height: 1.75;

}

.page__content .featured-project .project-meta {

  display: grid;

  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));

  gap: 1rem;

  margin: 1.5rem 0 2rem 0;

}

.page__content .featured-project .meta-card {

  background: white;

  border-radius: 14px;

  padding: 1rem 1.1rem;

  border: 1px solid rgba(148, 163, 184, 0.14);

  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);

}

.page__content .featured-project .meta-card strong {

  display: block;

  margin-bottom: 0.35rem;

  color: #111827;

}

.page__content .featured-project .benefits-list,

.page__content .featured-project .contrib-list,

.page__content .featured-project .takeaways-list {

  margin-top: 0.5rem;

  margin-bottom: 1.5rem;

}

.page__content .featured-project .screenshots-grid {

  display: grid;

  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));

  gap: 1.1rem;

  margin-top: 1.5rem;

}

.page__content .featured-project figure {

  margin: 0;

  background: white;

  border-radius: 14px;

  overflow: hidden;

  border: 1px solid rgba(148, 163, 184, 0.15);

  box-shadow: 0 12px 28px rgba(15, 23, 42, 0.07);

}

.page__content .featured-project figure img {

  width: 100%;

  display: block;

}

.page__content .featured-project figcaption {

  padding: 0.85rem 1rem;

  font-size: 0.95rem;

  color: #475569;

}

.page__content .featured-project .project-note {

  margin-top: 1.5rem;

  font-size: 0.98rem;

  color: #475569;

}

@media (max-width: 768px) {

  .page__content .featured-project {

    padding: 1.25rem;

  }

}

</style>

<div class="featured-project">

  <div class="section-label">Featured Project</div>

  <h2>Large Projects</h2>

  <h3>Web-Based Compost Tracker</h3>

  <p>

    I designed and developed a full-stack, web-based Compost Tracker for Victory Garden Initiative (VGI), a Milwaukee nonprofit focused on sustainable food systems and community composting. The system was built to replace manual spreadsheet and paper-based tracking processes, which were inefficient, error-prone, and limited the organization’s ability to analyze compost data and scale operations.

  </p>

  <p>

    The application centralizes compost data collection, improves accuracy, and gives users real-time visibility into compost activity. It includes compost entry logging, automated calculations, reporting dashboards, and role-based access control for both administrators and volunteers.

  </p>

  <div class="project-meta">

    <div class="meta-card">

      <strong>Frontend</strong>

      HTML, CSS, JavaScript

    </div>

    <div class="meta-card">

      <strong>Backend</strong>

      PHP

    </div>

    <div class="meta-card">

      <strong>Database</strong>

      MySQL using cPanel / phpMyAdmin

    </div>

    <div class="meta-card">

      <strong>Workflow</strong>

      Log compost data → validate inputs → store in database → view summaries and reports

    </div>

  </div>

  <h3>Potential Impact</h3>

  <ul class="benefits-list">

    <li>Improves overall composting efficiency by identifying trends in material input and output.</li>

    <li>Supports faster turnover from food scraps to nutrient-rich soil through better tracking of compost conditions such as temperature and material ratios.</li>

    <li>Reduces human error and improves accuracy compared to spreadsheet or paper-based tracking.</li>

    <li>Saves administrative time by automating logging, storage, and reporting.</li>

    <li>Supports data-driven decisions for optimizing compost processes and allocating resources more effectively.</li>

    <li>Creates a scalable foundation for expanded compost operations across multiple sites or volunteer teams.</li>

    <li>Lays the groundwork for future enhancements like predictive analytics, process optimization, and environmental impact reporting.</li>

  </ul>

  <h3>My Contributions</h3>

  <ul class="contrib-list">

    <li>Designed and built the full system independently, including frontend, backend, and database structure.</li>

    <li>Implemented CRUD functionality, validation, authentication, and reporting features.</li>

    <li>Designed the database schema and integrated it with a live web interface.</li>

    <li>Created both technical and user documentation for deployment and use.</li>

  </ul>

  <h3>What I Learned</h3>

  <ul class="takeaways-list">

    <li>End-to-end development depends on strong integration between UI, backend logic, and database design.</li>

    <li>Building without frameworks strengthened my understanding of core web technologies and debugging.</li>

    <li>Early planning and scope control are critical for delivering a stable prototype on time.</li>

  </ul>

  <h3>Project Screenshots</h3>

  <div class="screenshots-grid">

    <figure>

      <img src="{{ '/assets/images/projects/compost/dashboard.jpg' | relative_url }}" alt="Compost Tracker dashboard overview">

      <figcaption>Dashboard overview showing live metrics, quick stats, and recent compost entries.</figcaption>

    </figure>

    <figure>

      <img src="{{ '/assets/images/projects/compost/log-entry.jpg' | relative_url }}" alt="Compost Tracker log entry form">

      <figcaption>Log entry workflow used to record greens, browns, food scraps, temperature, and notes.</figcaption>

    </figure>

    <figure>

      <img src="{{ '/assets/images/projects/compost/reports.jpg' | relative_url }}" alt="Compost Tracker reports page">

      <figcaption>Reporting view used to summarize yearly activity, material ratios, and soil output.</figcaption>

    </figure>

    <figure>

      <img src="{{ '/assets/images/projects/compost/database.jpg' | relative_url }}" alt="Database records for the compost tracker">

      <figcaption>Database layer showing compost log records stored and managed through MySQL.</figcaption>

    </figure>

    <figure>

      <img src="{{ '/assets/images/projects/compost/admin-panel.jpg' | relative_url }}" alt="Compost Tracker admin panel">

      <figcaption>Admin panel for user management, compost log oversight, and system-level control.</figcaption>

    </figure>

  </div>

  <p class="project-note">

    This project reflects full-stack development, data design, and real-world problem-solving for a mission-driven nonprofit environment.

  </p>

</div>
