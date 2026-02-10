from flask import Flask, render_template, request, redirect, session, url_for
import json
import os

app = Flask(__name__)
# A secret key is required to use sessions. In production, keep this secret!
app.secret_key = 'sule-smith-secret-key-change-this-in-prod'

# SET YOUR SECRET ACCESS CODE HERE
ACCESS_CODE = "IRIE2026" 

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

@app.route("/shop")
def shop():
    with open("data/shop.json", encoding='utf-8') as f:
        shop_data = json.load(f)
    return render_template("shop.html", products=shop_data)

@app.route("/shop-preview")
def shop_preview():
    # Make sure you have data/shop.json created, even if dummy data
    try:
        with open("data/shop.json", encoding='utf-8') as f:
            shop_data = json.load(f)
    except FileNotFoundError:
        shop_data = [] # Handle case where file doesn't exist yet
        
    return render_template("shop_full.html", products=shop_data)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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
    # Check session
    is_authorized = session.get('authorized', False)
    error_message = None

    if request.method == "POST":
        # Check if they are submitting the Access Code
        user_code = request.form.get("access_code")
        
        if user_code == ACCESS_CODE:
            session['authorized'] = True
            return redirect(url_for('contact'))
        else:
            error_message = "Incorrect Access Code."

    return render_template("contact.html", authorized=is_authorized, error=error_message)


if __name__ == "__main__":
    app.run(debug=True)