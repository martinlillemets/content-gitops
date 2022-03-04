from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! Trigger rebuild because we changed requirements withhout pull request like a dummy"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
