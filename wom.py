import requests
import time

from config import (
    WOM_API_KEY,
    USER_AGENT,
    BASE_URL,
    UPDATE_WAIT
)

HEADERS = {
    "x-api-key": WOM_API_KEY,
    "User-Agent": USER_AGENT
}


def update_player(username):

    print(f"Updating {username}...")

    response = requests.post(
        f"{BASE_URL}/players/{username}",
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()


def get_player(username):

    response = requests.get(
        f"{BASE_URL}/players/{username}",
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()


def get_daily_gains(username):

    response = requests.get(
        f"{BASE_URL}/players/{username}/gained?period=day",
        headers=HEADERS
    )

    response.raise_for_status()

    return response.json()


def update_all(players):

    for player in players:
        update_player(player)

    print(f"Waiting {UPDATE_WAIT} seconds...")

    time.sleep(UPDATE_WAIT)
