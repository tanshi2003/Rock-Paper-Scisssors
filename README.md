# Rock Paper Scissors 🎮

A simple, interactive Rock Paper Scissors game with two game modes. Play against the computer or challenge a friend on the same device.

## 🎮 Play the Game

**[Play Rock Paper Scissors](https://tanshi2003.github.io/Rock-Paper-Scisssors/)**

## ✨ Features

- **Play vs Computer:** Compete against a randomly generated computer move.
- **2 Player Mode:** Play with a friend on the same device, with hidden moves until both players have chosen.
- **Score Tracking:** Keep track of wins across rounds.
- **Sound Effects:** Toggle game sounds on or off.
- **Keyboard Controls:** Use `1`, `2`, and `3` to select Rock, Paper, and Scissors.
- **Responsive Design:** Play on desktop or mobile devices.
- **No Installation Required:** Runs directly in your browser.

## 🛠️ Tech Stack

- HTML5
- CSS3
- JavaScript
- Python & Flask (optional API)

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/tanshi2003/Rock-Paper-Scisssors.git
cd Rock-Paper-Scisssors
```

Open `frontend/index.html` in your browser.

Alternatively, start a local server:

```bash
cd frontend
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## 🎯 How to Play

### Against the Computer
Choose Rock, Paper, or Scissors. The computer randomly selects its move, and the winner is decided automatically.

### With a Friend
Player 1 selects a move, passes the device to Player 2, and Player 2 selects their move. Both moves are revealed to determine the winner.

### Keyboard Controls

| Key | Move |
|---|---|
| `1` | Rock |
| `2` | Paper |
| `3` | Scissors |
| `Esc` | Return to the home screen |

## ⚙️ Optional Flask API

The project also includes a Flask API for experimenting with the game logic independently of the browser frontend.

### Setup

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
python app.py
```

The API runs at `http://localhost:5000`.

### API Endpoint

`POST /play`

Request:

```json
{
  "choice": "rock"
}
```

Valid choices: `rock`, `paper`, `scissors`.

Example response:

```json
{
  "yourChoice": "rock",
  "computerChoice": "scissors",
  "result": "win"
}
```

Invalid or missing choices return HTTP `400`.

## 📁 Project Structure

```text
Rock-Paper-Scisssors/
├── app.py
├── requirements.txt
├── README.md
├── .github/
│   └── workflows/
│       └── pages.yml
└── frontend/
    ├── index.html
    ├── fist.png
    ├── peace.png
    ├── scissors.png
    └── rock-paper-scissors.png
```

## 📦 Dependencies

- **Frontend:** No external dependencies
- **Optional API:** Flask and Flask-Cors

The browser game uses vanilla HTML, CSS, and JavaScript. No build tools, bundlers, or package managers are required.
