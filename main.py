import os
import telebot
import time
from flask import Flask
import threading
import datetime
import pytz

# 🔐 Токен і Chat ID
TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

bot = telebot.TeleBot(TOKEN)

affirmations = {
    "11:11": "Я сама ахуєнна і піздата. У мене все складається найкращим чином. Я живу у любові, достатку і злагоді.",
    "17:17": "Я головний герой свого життя і в мене все складається найкращим чином, бо я на це заслуговую.",
    "22:22": "Я вдячна всесвіту і собі за все, що я маю і буду мати, я найщасливіша і життя прекрасне."
}

def send_affirmation(current_time):
    message = affirmations[current_time]
    bot.send_message(CHAT_ID, message)

def affirmation_loop():
    sent_today = set()
    tz = pytz.timezone('Europe/Kyiv')
    while True:
        now = datetime.datetime.now(tz)
        current_time = now.strftime("%H:%M")

        if current_time in affirmations and current_time not in sent_today:
            send_affirmation(current_time)
            sent_today.add(current_time)

        if current_time == "00:01":
            sent_today.clear()

        time.sleep(30)

app = Flask(__name__)

@app.route('/')
def home():
    return "Я живий!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# 🚀 Запуск двох потоків
threading.Thread(target=run_flask).start()
threading.Thread(target=affirmation_loop).start()
