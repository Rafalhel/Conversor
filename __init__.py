from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=["POST", "GET"])
def index():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)