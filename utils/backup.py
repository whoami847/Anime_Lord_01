# backup.py
import shutil
import os
from datetime import datetime

def backup_data():
    try:
        # Create a backup of the database
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_dir = f"backup_{timestamp}"
        os.makedirs(backup_dir, exist_ok=True)
        shutil.copy("anime_lord.db", backup_dir)
        return f"Backup created at {backup_dir}"
    except Exception as e:
        return f"Error during backup: {str(e)}"
      
