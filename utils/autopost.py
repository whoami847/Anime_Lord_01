# autopost.py
from aiogram import types
from emojis import get_emoji

class AutoPost:
    def __init__(self, bot):
        self.bot = bot
    
    async def post_to_channel(self, message: types.Message, channel_id: str):
        try:
            await self.bot.send_message(channel_id, message.text)
            return True
        except Exception as e:
            return False
          
