from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<name>")
def name_guess(name):
    age = requests.get(url=f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(url=f"https://api.genderize.io/?name={name}").json()["gender"]
    return render_template("names.html", name=name, age=age, gender=gender)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
