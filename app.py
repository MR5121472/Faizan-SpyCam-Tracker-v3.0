from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "7590817261:AAGL6vH2hi4NPd9x1Iikaqlk40p5xxQ0cBc"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.json
        if "message" in data:
            chat_id = data["message"]["chat"]["id"]
            text = data["message"].get("text", "📷 New visitor")
            requests.post(URL, json={"chat_id": chat_id, "text": f"👁 Message: {text}"})
        return {"ok": True}
    return "💥 Faizan™ SpyCam Bot is Active"

if __name__ == "__main__":
    app.run(debug=False)
