import asyncio

# Dummy in-memory store
users_db = set()
bulk_files_db = {}

async def save_bulk_files(user_id, file_details):
    if user_id not in bulk_files_db:
        bulk_files_db[user_id] = []
    bulk_files_db[user_id].append(file_details)
    users_db.add(user_id)

async def get_user_count():
    return len(users_db)
