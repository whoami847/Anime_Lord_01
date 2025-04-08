# logs.py
from aiogram import types
from aiogram.types import ParseMode
from emojis import get_emoji

async def handle_logs(message: types.Message):
    try:
        # Retrieve and show logs
        await message.reply(f"{get_emoji('memo')} Here are the logs.", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        await message.reply(f"{get_emoji('warning')} Error: {str(e)}", parse_mode=ParseMode.MARKDOWN_V2)
      
