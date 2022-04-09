from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello!"

@app.route("/add")
def add():
    a = request.args.get("a", "")
    b = request.args.get("b", "")
    return str(int(a) + int(b))

app.run(host="127.0.0.1", port=8080)
