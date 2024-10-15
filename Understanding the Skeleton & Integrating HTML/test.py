from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("wellcome.html")


@app.route("/about")
def about():
    return "about"


@app.route("/contact")
def contact():
    return "contact"


@app.route("/blog")
def blog():
    return "blog"


@app.route("/sale")
def sale():
    return "sale"


# Entry of the program to start it's execution
if __name__ == '__main__':
    app.run(debug=True)
