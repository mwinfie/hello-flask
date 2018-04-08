import socket
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>{}</h1>".socket.gethostname()

if __name__ == "__main__":
    application.run(host='0.0.0.0')