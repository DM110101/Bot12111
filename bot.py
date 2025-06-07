from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Конфигурация
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = "@LiquidHunters_x100"

TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route("/", methods=["GET"])
def index():
    return "Bot is running."

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)

    # Извлекаем сигнал (настрой, как тебе нужно)
    message = data.get("message") or data.get("text") or str(data)

    payload = {
        "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(TELEGRAM_API_URL, json=payload)

    if response.status_code == 200:
        return {"ok": True}, 200
    else:
        return {"ok": False, "error": response.text}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)