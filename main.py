import os
import telebot
from flask import Flask, request
import threading

# Дані з env
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Бот
bot = telebot.TeleBot(TOKEN)

affirmations = {
    "11:11": "Я сама ахуєнна і піздата. У мене все вийде 💋",
    "17:17": "Я головний герой свого життя і в мене все складається найкращим чином, бо я на це заслуговую",
    "22:22": "Я вдячна всесвіту і собі за все, що я маю і буду мати, я найщасливіша і життя прекрасне"
}

def check_time():
    import time
    from datetime import datetime
    import pytz

    tz = pytz.timezone('Europe/Kyiv')

    while True:
        now = datetime.now(tz)
        current_time = now.strftime("%H:%M")
        if current_time in affirmations:
            bot.send_message(CHAT_ID, affirmations[current_time])
            time.sleep(60)
        time.sleep(10)

threading.Thread(target=check_time).start()

# Flask для Railway
app = Flask(__name__)

@app.route('/')
def index():
    return "Бот працює 🐍"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
