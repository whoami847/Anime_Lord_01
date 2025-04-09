import os
from pyrogram import Client, filters
from flask import Flask
import threading

# API and Bot Token from environment variables
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

# Flask run function for 8080 port (for Koyeb)
def run_flask():
    flask_app.run(host="0.0.0.0", port=8080, debug=True)  # Added debug=True

# Main
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()  # Run Flask in a separate thread
    bot.run()  # Run the Pyrogram bot
