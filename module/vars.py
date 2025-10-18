import os

API_ID    = os.environ.get("API_ID", "27297131")
API_HASH  = os.environ.get("API_HASH", "9fdd19cc4433056a425c9a042ffe8ba0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8486255280:AAER-h8Guf4-QKe0d1ssZjDVJ4U4eGyAFXI
") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
