import threading
from flask import Flask, request, jsonify
import telebot
from flask_cors import CORS

# Читаем токен из config.txt
with open('config.txt', 'r') as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app)  # Разрешаем CORS для запросов с сайта

# Хранение кликов в памяти (для простоты)
clicks_data = {}

@app.route('/')
def index():
    return "Сервер запущен и работает!"

@app.route('/increment_clicks', methods=['POST'])
def increment_clicks():
    data = request.json
    user_id = str(data.get('user_id'))
    if not user_id:
        return jsonify({'error': 'user_id required'}), 400

    clicks_data[user_id] = clicks_data.get(user_id, 0) + 1
    return jsonify({'user_id': user_id, 'clicks': clicks_data[user_id]})

@app.route('/get_clicks', methods=['GET'])
def get_clicks():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id required'}), 400

    clicks = clicks_data.get(user_id, 0)
    return jsonify({'user_id': user_id, 'clicks': clicks})

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    web_app = telebot.types.WebAppInfo(url="https://zunii.netlify.app/")  # Замени на свой URL
    button = telebot.types.InlineKeyboardButton(text="Играть 🎮", web_app=web_app)
    keyboard.add(button)
    bot.send_message(message.chat.id,
                     "👋 <b>Привет!</b>\nНачни играть и получай удовольствие! 🎉",
                     parse_mode='HTML',
                     reply_markup=keyboard)

if __name__ == '__main__':
    # НЕ запускаем Flask через app.run(), Render сделает это за нас через gunicorn
    # Просто запускаем бота
    bot.infinity_polling()
