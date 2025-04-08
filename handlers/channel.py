# channel.py
from aiogram import types
from aiogram.types import ParseMode
from utils.autopost import AutoPost
from emojis import get_emoji

async def handle_channel_subscription(message: types.Message):
    try:
        # Logic for forced channel subscription
        await message.reply(f"{get_emoji('thumbs_up')} You have been subscribed to the channel.", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        await message.reply(f"{get_emoji('warning')} Error: {str(e)}", parse_mode=ParseMode.MARKDOWN_V2)
      
