"""Optional API for the Rock Paper Scissors game."""
from flask import Flask, request, jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)
CHOICES = ("rock", "paper", "scissors")


def winner(player, computer):
    if player == computer:
        return "draw"
    if (player, computer) in (("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")):
        return "win"
    return "lose"


@app.get("/")
def home():
    return jsonify({"message": "Rock Paper Scissors API is running", "endpoint": "POST /play"})


@app.post("/play")
def play():
    data = request.get_json(silent=True) or {}
    choice = data.get("choice")
    if choice not in CHOICES:
        return jsonify({"error": "Invalid choice. Choose rock, paper, or scissors."}), 400
    computer = random.choice(CHOICES)
    return jsonify({"yourChoice": choice, "computerChoice": computer, "result": winner(choice, computer)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
