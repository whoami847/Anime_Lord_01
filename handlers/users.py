# users.py
from aiogram import types
from aiogram.types import ParseMode
from emojis import get_emoji

async def handle_user_list(message: types.Message):
    try:
        # Logic to show user list
        await message.reply(f"{get_emoji('calendar')} Here is the list of users.", parse_mode=ParseMode.MARKDOWN_V2)
    except Exception as e:
        await message.reply(f"{get_emoji('warning')} Error: {str(e)}", parse_mode=ParseMode.MARKDOWN_V2)
      
