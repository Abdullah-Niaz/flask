from flask import Flask
'''
    It creates an instance of the Flask class, 
    Which will be your WSGI (WEB SERVER GATEWAY INTERFACE) application.
'''
app = Flask(__name__)


@app.route('/')
def wellcome():
    return "Hello world"


@app.route("/index")
def index():
    return "this is the index page "


# Entry of the program to start it's execution
if __name__ == '__main__':
    app.run(debug=True)
