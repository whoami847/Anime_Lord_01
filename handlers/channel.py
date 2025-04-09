from pyrogram import Client, filters
from pyrogram.types import Message
from config import CHANNELS, ADMINS

@Client.on_message(filters.command("channel") & filters.user(ADMINS))
async def list_channels(client: Client, message: Message):
    channels_list = "\n".join([f"{idx+1}. {channel}" for idx, channel in enumerate(CHANNELS)])
    await message.reply_text(f"Your managed channels:\n\n{channels_list}")
