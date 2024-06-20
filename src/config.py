import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PROXY = {
    "scheme": os.getenv("PROXY_SCHEME"),
    "hostname": os.getenv("PROXY_HOSTNAME"),
    "port": int(os.getenv("PROXY_PORT")),
}
SERVER_API_URL = os.getenv("SERVER_API_URL")
