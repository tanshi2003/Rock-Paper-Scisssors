from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow frontend requests from different port

@app.route('/')
def home():
    return "Flask RPS backend is running 🎮"

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data.get('choice')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = 'draw'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = 'win'
    else:
        result = 'lose'

    return jsonify({
        'yourChoice': user_choice,
        'computerChoice': computer_choice,
        'result': result
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

