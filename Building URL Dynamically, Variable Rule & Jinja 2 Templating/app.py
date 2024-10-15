from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return "home page"


@app.route('/succ/<int:score>')
def index(score):
    res = ''
    if score < 0:
        res = "Invalid score"
    elif score < 40:
        res = 'fail'
    exp = {'result': res, "Score": score}
    return render_template('index.html', result=exp)


if __name__ == '__main__':
    app.run(debug=True)
