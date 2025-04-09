import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from database import save_bulk_files
from utils.files import get_file_details
from config import ADMINS

logger = logging.getLogger(__name__)

@Client.on_message(filters.private & filters.user(ADMINS) & filters.media)
async def handle_bulk_share(client: Client, message: Message):
    try:
        file_details = await get_file_details(message)
        await save_bulk_files(message.from_user.id, file_details)
        await message.reply_text("File saved for bulk sharing.")
    except Exception as e:
        logger.error(f"Error in bulk_share: {e}")
        await message.reply_text("Failed to save file for bulk sharing.")
