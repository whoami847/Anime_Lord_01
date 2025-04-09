async def get_file_details(message):
    media = message.document or message.video or message.audio
    return {
        "file_id": media.file_id,
        "file_name": media.file_name,
        "file_size": media.file_size,
        "mime_type": media.mime_type
    }
