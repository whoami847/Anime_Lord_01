# bulk_share.py
from aiogram import types
from aiogram.types import ParseMode
from utils.autopost import AutoPost
# from emojis import get_emoji

async def handle_bulk_share(message: types.Message):
    try:
        # Some logic to handle bulk sharing
        await message.reply(f"{get_emoji('rocket')} Bulk file sharing initiated!", parse_mode=ParseMode.MARKDOWN_V2)
        # Post to channels, etc.
    except Exception as e:
        await message.reply(f"{get_emoji('warning')} Error: {str(e)}", parse_mode=ParseMode.MARKDOWN_V2)
      
