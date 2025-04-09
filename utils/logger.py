import os

LOG_FILE = "bot_logs.txt"

def read_logs():
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            f.write("Bot started.\n")
    return LOG_FILE
