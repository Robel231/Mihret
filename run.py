from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    # Generate static files
    with app.app_context():
        os.makedirs("static_build", exist_ok=True)
        for route, file_name in [
            ("/", "index.html"),
            ("/about", "about.html"),
            ("/portfolio", "portfolio.html"),
            ("/contact", "contact.html"),
        ]:
            with open(f"static_build/{file_name}", "w") as f:
                f.write(render_template(file_name))
