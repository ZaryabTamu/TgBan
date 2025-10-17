import os

class Config:
    # Bot configuration
    API_ID = int(os.environ.get("API_ID", 28615030))
    API_HASH = os.environ.get("API_HASH", "4cd09b1bcd45560ee35e8be593f13d83")
    TOKEN = os.environ.get("TOKEN", "8161770605:AAFOnX1Tn9OE9D3874qGsfUxmbPEqJ7fCbM")
    
    # Sudo users
    SUDO = [6125202012, 8171988347, 5907205317]  # Owner and dev users
    
    # Bot info
    START_IMG = os.environ.get("START_IMG", "https://files.catbox.moe/wz8qgd.jpg")
    BOT_ID = 7971809958  # Your bot ID
    BOT_USERNAME = "Kafka_SecurityBot"  # Your bot username
    BOT_NAME = "𝐊ᴀғᴋᴀ 𝐇ᴏɴᴋᴀɪ 𝐒ᴇᴄᴜʀɪᴛʏ"  # Your bot name
    
    # Log channel
    LOG_CHANNEL = -1002392274240 # Your log channel ID
    
    # Database
    DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://I-LOVE-PDF-BOT:I-LOVE-PDF-BOT@cluster0.c51o3a9.mongodb.net/?retryWrites=true&w=majority")


    