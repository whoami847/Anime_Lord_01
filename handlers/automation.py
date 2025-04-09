from pyrogram import Client, filters
from pyrogram.types import Message
from config import ADMINS, AUTO_REPLY

@Client.on_message(filters.private & filters.text & filters.user(ADMINS))
async def set_auto_reply(client: Client, message: Message):
    if message.text.startswith("/setreply "):
        reply_text = message.text.split("/setreply ", 1)[1]
        AUTO_REPLY["text"] = reply_text
        await message.reply_text("Auto reply set successfully.")
    elif message.text == "/getreply":
        await message.reply_text(f"Current auto reply:\n\n{AUTO_REPLY.get('text', 'Not set')}")
