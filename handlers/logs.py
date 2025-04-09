from pyrogram import Client, filters
from pyrogram.types import Message
from utils.logger import read_logs
from config import ADMINS

@Client.on_message(filters.command("logs") & filters.user(ADMINS))
async def send_logs(client: Client, message: Message):
    logs = read_logs()
    await message.reply_document(document=logs, caption="Bot Logs File")
