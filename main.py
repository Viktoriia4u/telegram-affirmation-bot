import os
import telebot
import time
from flask import Flask
import threading
import requests

# 🔐 ВСТАВ СВІЙ ТОКЕН І CHAT ID ТУТ:
TOKEN = '7935951867:AAGeV3hPxh3v-TtrBI2PGewn_XL7IbIBLiA'
CHAT_ID = '404304037'

# 🔧 Створення бота
bot = telebot.TeleBot(TOKEN)

# 🔁 Повідомлення, яке надсилатиметься
def send_affirmation():
    message = ("Я сама ахуєнна і піздата. "
               "У мене все складається найкращим чином. "
               "Я живу у любові, достатку і злагоді.")
    bot.send_message(CHAT_ID, message)

# 🌐 Flask-сервер для підтримки Replit активним
app = Flask('')

@app.route('/')
def home():
    return "Я живий!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = threading.Thread(target=run)
    thread.start()

# 🔁 Запуск
keep_alive()

while True:
    send_affirmation()
    time.sleep(300)  # 3600 секунд = 1 година (можеш тимчасово поставити 10)
