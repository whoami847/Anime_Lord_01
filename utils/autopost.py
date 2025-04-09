from aiogram import types
import emojis  # Correcting the import

class AutoPost:
    def __init__(self, bot):
        self.bot = bot

    async def post_to_channel(self, message: types.Message, channel_id: str):
        try:
            # Here you can use emojis.encode() to add emojis
            text_with_emojis = emojis.encode(message.text)
            await self.bot.send_message(channel_id, text_with_emojis)
            return True
        except Exception as e:
            return False
