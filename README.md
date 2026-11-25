# Rock Paper Scissors 🎮

A small browser game with two modes: play against a randomly choosing computer or take turns with a friend on the same device.

## Play online

After GitHub Pages is configured, the game can be played at:

**https://tanshi2003.github.io/Rock-Paper-Scisssors/**

The browser game is self-contained. It does not require a Python server, API calls, or any JavaScript packages. The computer opponent runs in the browser, so it is playable as a static site.

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/tanshi2003/Rock-Paper-Scisssors.git
   cd Rock-Paper-Scisssors
   ```
2. Open `frontend/index.html` directly in a browser. Or serve it locally:

   ```bash
   cd frontend
   python -m http.server 8000
   ```
3. Open **http://localhost:8000**.

## Deploy with GitHub Pages

This repository keeps the game page and image assets in `frontend/`. GitHub Pages' branch picker doesn't directly publish arbitrary subfolders, so use the included GitHub Actions workflow (`.github/workflows/pages.yml`):


1. Commit and push the workflow to the `main` branch.
2. In GitHub, open **Settings → Pages** and set **Build and deployment → Source** to **GitHub Actions**.
3. On the next push to `main`, the workflow deploys the contents of `frontend/`.
4. Open the Pages URL shown in Settings → Pages. It should be `https://tanshi2003.github.io/Rock-Paper-Scisssors/` for this repository.


## Controls and features

- Click a move or use keyboard keys **1**, **2**, **3** (Rock, Paper, Scissors).
- Toggle sound with the **Sound** control.
- **Against the computer:** the computer chooses randomly. Scores remain for the current session.
- **With a friend:** player one chooses, the selection stays hidden, then the device is handed to player two. Both choices reveal after player two plays.
- Select **Change mode** to return to the mode picker.


## Optional Flask API

The original project includes a small Flask API. The frontend no longer needs it, but it remains available for API experimentation or another client.

### Install and run

Python 3.9+ recommended.

```bash
python -m venv .venv
```

Activate it:


- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

Install requirements and start the API:

```bash
pip install -r requirements.txt
python app.py
```

API runs at **http://localhost:5000**.

### Endpoint

`POST /play` with JSON body:


```json
{"choice":"rock"}
```

Valid choices are `rock`, `paper`, and `scissors`. Invalid or missing choices return HTTP 400.

Example response:


```json
{"yourChoice":"rock","computerChoice":"scissors","result":"win"}
```

## Files

```text
.
├── app.py                 # Optional Flask API
├── requirements.txt        # API dependencies only
├── README.md
├── .github/workflows/
│   └── pages.yml          # GitHub Pages deployment
└── frontend/
    ├── index.html        # Browser game, no build dependencies
    ├── fist.png         # Rock image
    ├── peace.png        # Paper image
    ├── scissors.png     # Scissors image
    └── rock-paper-scissors.png
```

## Dependencies

- **Browser game:** none (plain HTML, CSS, JavaScript)
- **Optional API:** Python and Flask / Flask-Cors (listed in `requirements.txt`)

No package manager or bundler is required.
