from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/resume")
def resume():
    with open("data/resume.json") as f:
        resume_data = json.load(f)
    return render_template("resume.html", resume=resume_data)

@app.route("/portfolio")
def portfolio():
    with open("data/portfolio.json") as f:
        portfolio_data = json.load(f)
    return render_template("portfolio.html", projects=portfolio_data)

@app.route("/blog")
def blog():
    with open("data/blog_posts.json") as f:
        posts = json.load(f)
    return render_template("blog.html", posts=posts)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("Form submitted:", request.form)
        return redirect("/")
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
