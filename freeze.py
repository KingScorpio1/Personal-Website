import os
import shutil
import re
import json
import werkzeug

# Monkey-patch Werkzeug version for Flask test client compatibility in Python 3.14
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "3.0.1"

from app import app

# Initialize the Flask test client
client = app.test_client()

# Define the build output directory
BUILD_DIR = 'build'
if os.path.exists(BUILD_DIR):
    print(f"Cleaning existing '{BUILD_DIR}' directory...")
    shutil.rmtree(BUILD_DIR)

print(f"Creating '{BUILD_DIR}' directory...")
os.makedirs(BUILD_DIR)

# Copy static directory to build/static
if os.path.exists('static'):
    shutil.copytree('static', os.path.join(BUILD_DIR, 'static'))
    print("Copied static assets folder.")

# Links rewriter function for static CDNs
def rewrite_links(html_content):
    def replace_link(match):
        link = match.group(1)
        if link == '/':
            return 'href="/index.html"'
        if link.startswith('/static/'):
            return match.group(0)
        # Match clean internal links (no dot in the final path segment, not an anchor)
        if '.' not in link.split('/')[-1] and not link.startswith('#'):
            return f'href="{link}.html"'
        return match.group(0)
    
    # Rewrite relative site paths
    html_content = re.sub(r'href="(/[^"]+)"', replace_link, html_content)
    
    # Replace Flask test client localhost URLs with the production Render domain
    html_content = html_content.replace('http://localhost/', 'https://sule-smiths-personal-website.onrender.com/')
    
    return html_content

# Define all routes to freeze
routes = [
    '/',
    '/about',
    '/resume',
    '/credentials',
    '/shop',
    '/shop-preview',
    '/portfolio',
    '/blog',
    '/contact',
    '/404'
]

# Dynamically query and add all portfolio project pages
try:
    with open(os.path.join("data", "portfolio.json"), "r", encoding="utf-8") as f:
        projects = json.load(f)
        for p in projects:
            project_id = p.get("id")
            if project_id:
                routes.append(f"/portfolio/{project_id}")
except Exception as e:
    print(f"Warning: Could not load portfolio.json to scan projects: {e}")

# Process and freeze all routes
for route in routes:
    print(f"Freezing route: {route}")
    response = client.get(route)
    if response.status_code != 200 and route != '/404':
        print(f"Warning: route '{route}' returned status code {response.status_code}")
    
    html = response.data.decode('utf-8')
    html = rewrite_links(html)
    
    # Determine the destination file path
    if route == '/':
        out_path = os.path.join(BUILD_DIR, 'index.html')
    else:
        # e.g., /about -> build/about.html
        # e.g., /portfolio/project-1 -> build/portfolio/project-1.html
        clean_route = route.lstrip('/')
        out_path = os.path.join(BUILD_DIR, f"{clean_route}.html")
        
    # Ensure nested subdirectories are created (e.g. build/portfolio/)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

print("\nStatic site compilation complete! Output written to the 'build/' folder.")
