from pyrogram import Client, filters
from pyrogram.types import Message
from config import BANNED_USERS, ADMINS

@Client.on_message(filters.command("ban") & filters.user(ADMINS))
async def ban_user(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /ban user_id")
        return
    try:
        user_id = int(message.command[1])
        BANNED_USERS.add(user_id)
        await message.reply_text(f"User {user_id} banned.")
    except Exception as e:
        await message.reply_text(f"Failed to ban user: {e}")

@Client.on_message(filters.command("unban") & filters.user(ADMINS))
async def unban_user(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("Usage: /unban user_id")
        return
    try:
        user_id = int(message.command[1])
        BANNED_USERS.discard(user_id)
        await message.reply_text(f"User {user_id} unbanned.")
    except Exception as e:
        await message.reply_text(f"Failed to unban user: {e}")
