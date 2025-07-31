from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_key', methods=['POST'])
def check_key():
    api_key = request.json.get('key')
    if not api_key:
        return jsonify({"valid": False, "error": "No key provided"}), 400

    headers = {"Authorization": f"Bearer {api_key}"}
    try:
        r = requests.get("https://api.openai.com/v1/models", headers=headers, timeout=10)
        if r.status_code == 200:
            return jsonify({"valid": True})
        else:
            return jsonify({"valid": False, "status": r.status_code})
    except Exception as e:
        return jsonify({"valid": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)