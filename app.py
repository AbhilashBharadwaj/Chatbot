from flask import Flask, render_template, request
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=['POST'])
def get_bot_response():
    query = request.json['message']
    topic = request.json['topic']
    print(request.json)
    answer = get_response(query)
    response = {'reply': answer}
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")