from pyrogram import Client, filters
from pyrogram.types import Message
from database import get_user_count
from config import ADMINS

@Client.on_message(filters.command("users") & filters.user(ADMINS))
async def show_user_count(client: Client, message: Message):
    count = await get_user_count()
    await message.reply_text(f"Total users in database: {count}")
