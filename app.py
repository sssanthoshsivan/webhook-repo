from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from db import events
from handlers import handle_push, handle_pr

load_dotenv()

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.json
    if not payload:
        return jsonify({"error": "Invalid payload"}), 400

    event = request.headers.get("X-GitHub-Event")
    data = None

    try:
        if event == "push":
            data = handle_push(payload)

        elif event == "pull_request":
            data = handle_pr(payload)

        if data:
            events.insert_one(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "ok"})


@app.route("/events", methods=["GET"])
def get_events():
    data = list(
        events.find({}, {"_id": 0})
        .sort("created_at", -1)
        .limit(10)
    )
    return jsonify(data)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000)
