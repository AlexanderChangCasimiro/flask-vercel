from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return "Hola Mundo con Flask 🚀"

def handler(environ, start_response):
    return app(environ, start_response)