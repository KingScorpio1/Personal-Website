from flask import Flask, render_template, request, redirect, session, url_for
import json
import os

app = Flask(__name__)
# A secret key is required to use sessions. In production, keep this secret!
app.secret_key = 'sule-smith-secret-key-change-this-in-prod'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    # ADDED: encoding='utf-8'
    with open("data/resume.json", encoding='utf-8') as f:
        resume_data = json.load(f)
    return render_template("resume.html", resume=resume_data)

@app.route("/resume/request", methods=["POST"])
def request_resume():
    requester = request.form.get("requester_email")
    print(f"--- RESUME REQUEST ---")
    print(f"User {requester} requested a copy of the resume.")
    print(f"----------------------")
    
    # In a real app with an email server, you would send the email here.
    # For now, we flash a message or redirect.
    # Since we aren't using Flask 'flash' messages yet, we'll just redirect to contact
    # or back to resume.
    
    return redirect("/resume")

@app.route("/portfolio")
def portfolio():
    # ADDED: encoding='utf-8'
    with open("data/portfolio.json", encoding='utf-8') as f:
        portfolio_data = json.load(f)
    return render_template("portfolio.html", projects=portfolio_data)

@app.route("/blog")
def blog():
    # ADDED: encoding='utf-8'
    with open("data/blog_posts.json", encoding='utf-8') as f:
        posts = json.load(f)
    return render_template("blog.html", posts=posts)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    # Check if the user is already authorized via session
    is_authorized = session.get('authorized', False)

    if request.method == "POST":
        # If the form being submitted is the "Unlock" form
        if "auth_email" in request.form:
            email = request.form.get("auth_email")
            # Here you could save this email to a file or database to track who viewed it
            print(f"User authorized with email: {email}") 
            
            # Set session to true
            session['authorized'] = True
            return redirect(url_for('contact'))
        
        # If it's a general contact form submission
        print("General Form submitted:", request.form)
        return redirect(url_for('contact'))

    return render_template("contact.html", authorized=is_authorized)

if __name__ == "__main__":
    app.run(debug=True)