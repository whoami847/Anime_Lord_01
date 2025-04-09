import os

API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your_api_hash")
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
PLUGIN_FOLDER = "handlers"

ADMINS = [123456789]  # Your Telegram user ID
CHANNELS = ["@yourchannel1", "@yourchannel2"]

AUTO_REPLY = {
    "text": "Hello! I am alive."
}

BANNED_USERS = set()
