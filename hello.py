from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("abc")
    return "Hello World deployed using AWS pipeline, also trying out git"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
