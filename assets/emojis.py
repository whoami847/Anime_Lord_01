# emojis.py
emoji_dict = {
    "check_mark": "✅",
    "cross_mark": "❌",
    "rocket": "🚀",
    "fire": "🔥",
    "star": "⭐",
    "thumbs_up": "👍",
    "thumbs_down": "👎",
    "heart": "❤️",
    "warning": "⚠️",
    "robot": "🤖",
    "calendar": "📅",
    "clock": "🕒",
    "memo": "📝",
}

def get_emoji(emoji_name: str) -> str:
    """Returns the corresponding emoji in MarkdownV2 format."""
    return emoji_dict.get(emoji_name, "")
