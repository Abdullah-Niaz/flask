from flask import Flask, render_template
'''
    It creates an instance of the Flask class, 
    Which will be your WSGI (WEB SERVER GATEWAY INTERFACE) application.
'''
app = Flask(__name__)


@app.route('/')
def wellcome():
    return render_template('wellcome.html')


@app.route("/index")
def index():
    return render_template('index.html')


# Entry of the program to start it's execution
if __name__ == '__main__':
    app.run(debug=True)
