# Sule Smith - Personal Portfolio & Engineering Hub

A dynamic, full-stack personal portfolio website built with Python and Flask. This platform serves as a digital resume, project showcase, and brand hub for my work as a Mechatronics Engineer, Full-Stack Developer, and STEM Educator.

## 🚀 Features

* **Dynamic Data Rendering:** Uses JSON files as a lightweight database to render complex portfolio suites, blog posts, and resume details without needing a heavy SQL setup.
* **Custom Media Engine:** 
  * Seamless track-based JavaScript slideshows with automated playback and caption overlays.
  * Embedded MP4 video support configured for both "silent looping GIF" style and standard playback.
  * In-app PDF viewer utilizing custom modal popups.
* **Interactive UI/UX:** 
  * "Glassmorphism" sticky navigation bar.
  * Animated HTML5 Canvas particle background (neural network/constellation effect).
  * Responsive Flexbox and CSS Grid layouts optimized for all devices.
* **Secure Access Portal:** A custom session-based authorization system for private contact links, protected by a server-side access code.
* **Production Ready:** Pre-configured with Gunicorn and a `Procfile` for seamless deployment on Render.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask, Gunicorn
* **Frontend:** HTML5 (Jinja2 Templating), CSS3 (Flexbox/Grid), Vanilla JavaScript (ES6)
* **Data Storage:** JSON
* **Hosting Configuration:** Render (PaaS)

## 📁 Project Structure

```text
personal-site/
├── app.py                 # Main Flask routing and logic
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment instructions for Render
├── data/                  # JSON databases 
│   ├── portfolio.json     # Project suites (Robotics, CAD, Apps, etc.)
│   ├── resume.json        # CV data
│   ├── blog_posts.json    # Blog entries
│   └── shop.json          # E-commerce inventory (Stripe integration)
├── static/                
│   ├── css/               # Modular stylesheets (style.css, resume.css)
│   ├── js/                # Client-side logic (main.js)
│   ├── img/               # Image assets and video files
│   └── docs/              # PDF engineering drawings
└── templates/             # Jinja2 HTML templates
    ├── base.html          # Master layout and navbar
    ├── index.html         # Hero landing page
    ├── project_detail.html# Dynamic template for complex project suites
    └── ...
```

## 💻 Local Development Setup

To run this project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask server:**
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`

## 🔒 Configuration Notes

* **Private Links:** To test the locked personal contact section, enter the code defined by the `ACCESS_CODE` variable in `app.py` (Default is `IRIE2026`).
* **Contact Forms:** Email requests are currently configured to route through Formspree. Ensure the endpoint URLs in `contact.html` and `shop.html` match your active Formspree IDs.

---
*Engineered by Sule Smith. Based in Taiwan.*
```