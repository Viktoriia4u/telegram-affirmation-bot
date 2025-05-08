import os
import telebot
import time
from flask import Flask
import threading
import datetime

# 🔐 Токен і Chat ID
TOKEN = '7935951867:AAGeV3hPxh3v-TtrBI2PGewn_XL7IbIBLiA'
CHAT_ID = '404304037'

# 🔧 Створення бота
bot = telebot.TeleBot(TOKEN)

# 🌟 Афірмації по годинах
affirmations = {
    "11:11": "Я сама ахуєнна і піздата. У мене все складається найкращим чином. Я живу у любові, достатку і злагоді.",
    "17:17": "Я головний герой свого життя і в мене все складається найкращим чином, бо я на це заслуговую.",
    "22:22": "Я вдячна всесвіту і собі за все, що я маю і буду мати, я найщасливіша і життя прекрасне."
}

# 📤 Функція надсилання афірмації
def send_affirmation(current_time):
    message = affirmations[current_time]
    bot.send_message(CHAT_ID, message)

# 🕒 Цикл афірмацій у окремому потоці
def affirmation_loop():
    sent_today = set()
    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time in affirmations and current_time not in sent_today:
            send_affirmation(current_time)
            sent_today.add(current_time)

        if current_time == "00:01":
            sent_today.clear()

        time.sleep(30)

# 🌐 Flask для Railway
app = Flask(__name__)

@app.route('/')
def home():
    return "Я живий!"

# 🚀 Запуск Flask і афірмацій у потоках
def run():
    app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run).start()
threading.Thread(target=affirmation_loop).start()
