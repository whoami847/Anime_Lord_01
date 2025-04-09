from pyrogram import Client
from handlers import bulk_share, channel, users, automation, logs, security, advanced
from config import API_ID, API_HASH, BOT_TOKEN, PLUGIN_FOLDER

app = Client(
    "Anime_Lord_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": PLUGIN_FOLDER}
)

print("Bot is running...")
app.run()
