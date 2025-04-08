# automation.py
from aiogram import types
from aiogram.types import ParseMode
from utils.autopost import AutoPost
from emojis import get_emoji

async def handle_auto_posting(message: types.Message):
    try:
        # Logic to handle auto-posting configuration
        await message.reply(f"{get_emoji('star')} Auto-posting is now configured!", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        await message.reply(f"{get_emoji('warning')} Error: {str(e)}", parse_mode=ParseMode.MARKDOWN_V2)
      
