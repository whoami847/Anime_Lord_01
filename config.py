import os

API_ID = int(os.getenv("API_ID", "28774737"))
API_HASH = os.getenv("API_HASH", "851190ab85bb0b6dd547fff8e3c35b73")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7352104242:AAEpIiqsTduGBYON09wYdK-T9JLXBw7JdJE")
PLUGIN_FOLDER = "handlers"

ADMINS = [123456789]  # Your Telegram user ID
CHANNELS = ["@log_chana", "@just_test_only_0"]

AUTO_REPLY = {
    "text": "Hello! I am alive."
}

BANNED_USERS = set()
