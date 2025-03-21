import os
import telebot
import time
from flask import Flask, request
import threading

# Ініціалізація Flask додатку
app = Flask('')

# Маршрут для перевірки стану
@app.route('/')
def home():
    return "I'm alive"

# Функція для запуску Flask сервера
def run():
    app.run(host='0.0.0.0', port=8080)

# Функція для підтримки активності Replit
def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# Ініціалізація бота
TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']
bot = telebot.TeleBot(TOKEN)

def send_affirmation():
    message = ("Ти сама ахуєнна і піздата. "
               "У тебе все складається найкращим чином. "
               "Ти живеш у любові, достатку і злагоді.")
    bot.send_message(CHAT_ID, message)

# Запуск keep_alive для підтримки активності
keep_alive()

# Основний цикл для надсилання повідомлень щогодини
while True:
    send_affirmation()
    time.sleep(3600)  # 3600 секунд = 1 година
