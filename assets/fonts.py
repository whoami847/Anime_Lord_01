# fonts.py

fancy_font = {
    "A": "A", "B": "B", "C": "C", "D": "D", "E": "E",
    "F": "F", "G": "G", "H": "H", "I": "I", "J": "J",
    "K": "K", "L": "L", "M": "M", "N": "N", "O": "O",
    "P": "P", "Q": "Q", "R": "R", "S": "S", "T": "T",
    "U": "U", "V": "V", "W": "W", "X": "X", "Y": "Y", "Z": "Z",

    "a": "ᴀ", "b": "ʙ", "c": "ᴄ", "d": "ᴅ", "e": "ᴇ",
    "f": "ғ", "g": "ɢ", "h": "ʜ", "i": "ɪ", "j": "ᴊ",
    "k": "ᴋ", "l": "ʟ", "m": "ᴍ", "n": "ɴ", "o": "ᴏ",
    "p": "ᴘ", "q": "ǫ", "r": "ʀ", "s": "s", "t": "ᴛ",
    "u": "ᴜ", "v": "ᴠ", "w": "ᴡ", "x": "x", "y": "ʏ", "z": "ᴢ",

    "0": "𝟶", "1": "𝟷", "2": "𝟸", "3": "𝟹", "4": "𝟺",
    "5": "𝟻", "6": "𝟼", "7": "𝟽", "8": "𝟾", "9": "𝟿"
}

def to_fancy(text: str) -> str:
    """Convert normal text to Anime Lord fancy style."""
    return ''.join(fancy_font.get(char, char) for char in text)

# উদাহরণ:
if __name__ == "__main__":
    print(to_fancy("Anime Lord 123"))
    # Output: Aɴɪᴍᴇ ʟᴏʀᴅ 𝟷𝟸𝟹
