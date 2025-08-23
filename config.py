import os

class Config:
    # Bot configuration
    API_ID = int(os.environ.get("API_ID", 12345678))
    API_HASH = os.environ.get("API_HASH", "abcdefghij1234567890")
    TOKEN = os.environ.get("TOKEN", "1234567890:ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    
    # Sudo users
    SUDO = [6346273488, 8171988347, 5907205317]  # Owner and dev users
    
    # Bot info
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/example.jpg")
    BOT_ID = 1234567890  # Your bot ID
    BOT_USERNAME = "Bot_RoxBot"  # Your bot username
    BOT_NAME = "Yumeko"  # Your bot name
    
    # Log channel
    LOG_CHANNEL = -1001234567890  # Your log channel ID
    
    # Database
    DB_URL = os.environ.get("DATABASE_URL", "postgresql://username:password@localhost:5432/database")
