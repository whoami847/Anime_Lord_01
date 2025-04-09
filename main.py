from pyrogram import Client
from flask import Flask
import threading
import os

API_ID = int(os.getenv("API_ID", "28774737")) 
API_HASH = os.getenv("API_HASH", "851190ab85bb0b6dd547fff8e3c35b73")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7352104242:AAEpIiqsTduGBYON09wYdK-T9JLXBw7JdJE")

# Pyrogram Bot setup
bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask HTTP Server setup
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

# Flask run function for 8000 port (for Koyeb)
def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

# Main
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()  # Flask চালাও আলাদা থ্রেডে
    bot.run()  # Pyrogram bot চালাও
