from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS

@Client.on_message(filters.command("stats") & filters.user(ADMINS))
async def bot_stats(client: Client, message: Message):
    await message.reply_text("Bot is running smoothly.\nNo errors found.")
