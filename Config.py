import os
from dotenv import load_dotenv
load_dotenv()

# Load environment variables
API_ID = int(os.environ.get("API_ID", "0"))
if API_ID == 0:
    raise ValueError("API_ID is missing or invalid.")

API_HASH = os.environ.get("API_HASH")
if not API_HASH:
    raise ValueError("API_HASH is missing.")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing.")

DATABASE_URL = os.environ.get("DATABASE_URL", "")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")

MUST_JOIN = os.environ.get("MUST_JOIN", "")
if MUST_JOIN.startswith("@"):
    MUST_JOIN = MUST_JOIN[1:]

# Optional: Debug mode
DEBUG = bool(os.environ.get("DEBUG", False))
