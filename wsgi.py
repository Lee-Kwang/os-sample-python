from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! and Test by Lkw!"

if __name__ == "__main__":
    application.run()
