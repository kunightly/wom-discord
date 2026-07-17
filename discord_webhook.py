import requests

from config import DISCORD_WEBHOOK


def send_embed(embed):

    payload = {
        "embeds": [embed]
    }

    r = requests.post(
        DISCORD_WEBHOOK,
        json=payload
    )

    r.raise_for_status()

    print("Discord message sent.")
