from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/tok")
def thello():
    return "Hello Tok!"

@application.route("/class")
def thello():
    return "<h1>Hello Tok!</h1>"

if __name__ == "__main__":
    application.run()
