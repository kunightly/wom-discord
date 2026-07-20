from dotenv import load_dotenv
import os

load_dotenv()

WOM_API_KEY = os.getenv("WOM_API_KEY")

DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK")

USER_AGENT = os.getenv(
    "WOM_USER_AGENT",
    "Knightly-WOM-Notify/1.0"
)

BASE_URL = "https://api.wiseoldman.net/v2"

PLAYERS = [
    "kn1ghtley",
    "ramleh"
]

UPDATE_WAIT = 30
