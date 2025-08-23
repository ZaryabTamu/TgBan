import os
import logging 
from pyrogram import Client
from config import Config 

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOG = logging.getLogger(__name__)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = str(os.environ.get("API_HASH", ""))
    TOKEN = str(os.environ.get("TOKEN", ""))
    SUDO = list(int(i) for i in os.environ.get("SUDO", "6346273488").split(" "))
    START_IMG = str(os.environ.get("START_IMG", ""))
    BOT_ID = int(os.environ.get("BOT_ID", ""))
    BOT_USERNAME = str(os.environ.get("BOT_USERNAME", ""))
    BOT_NAME = str(os.environ.get("BOT_NAME", ""))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
    DB_URL = str(os.environ.get("DATABASE_URL", ""))
else:
    from config import Config
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    TOKEN = Config.TOKEN
    SUDO = Config.SUDO
    START_IMG = Config.START_IMG
    BOT_ID = Config.BOT_ID
    BOT_USERNAME = Config.BOT_USERNAME
    BOT_NAME = Config.BOT_NAME
    LOG_CHANNEL = Config.LOG_CHANNEL
    DB_URL = Config.DB_URL

app = Client(
    "hasnainkk",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
    )

# Import modules
from hasnainkk.modules import start, admin, info, misc

LOG.info("Bot started successfully!")
