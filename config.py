import os

API_HASH = os.environ.get("API_HASH")
APP_ID = int(os.environ.get("APP_ID"))
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
PLUGIN_ROOT = "plugins"
MONGO_URL = os.environ.get("MONGO_URL")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "YourBotUsername")
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False") == "True"
DEFAULT_CAPTION = os.environ.get("DEFAULT_CAPTION", "Uploaded via Mr Kingsura Bot")
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "0"))
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL")
LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
ADMINS = os.environ.get("ADMINS", "").split(",")