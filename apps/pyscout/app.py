import os

import requests
from flask import Flask

app = Flask(__name__)

ELIXSCOUT_URL = os.environ.get("ELIXSCOUT_URL", "http://localhost:4000")


@app.route("/")
def hello():
    return "Hello, dscout!"


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/login")
def login():
    resp = requests.get(f"{ELIXSCOUT_URL}/auth/ping", timeout=5)
    return resp.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
