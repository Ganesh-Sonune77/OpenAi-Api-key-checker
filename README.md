openai-key-checker/
├── app.py
├── requirements.txt
├── static/
│   ├── styles.css
│   └── favicon.ico   ← optional
├── templates/
│   └── index.html
├── README.md
└── .gitignore


# 🔐 OpenAI API Key Checker

A simple Flask-based web tool to verify the validity of OpenAI API keys. Just paste multiple keys and get instant feedback on their status—VALID or INVALID.

## 🚀 How to Run

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run server
flask run
Visit http://localhost:5000 in your browser.

📦 Tech Stack
Python (Flask)

HTML, CSS, JavaScript (Vanilla)

OpenAI API v1

🔧 Endpoints
GET /
Returns the web interface.

POST /check_key

Accepts JSON: { "key": "your_api_key" } Returns status: { "valid": true } or error info.

⚠️ Notes
This is a dev tool, not recommended for production without a proper WSGI server.

Handles API rate limits gracefully, but use responsibly.

🎨 Credits
Built by Ganesh Sanjay Sonune


---

## 📦 requirements.txt

```txt
Flask
requests

🧼 .gitignore
venv/
__pycache__/
*.pyc
.env

