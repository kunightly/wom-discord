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


def request_with_retry(method, url, **kwargs):

    while True:

        response = requests.request(method, url, **kwargs)

        if response.status_code != 429:
            response.raise_for_status()
            return response

        retry_after = response.headers.get("Retry-After")

        try:
            wait = int(retry_after)
        except (TypeError, ValueError):
            wait = 30 * 60  # 30 minutes

        print(f"Rate limited (429). Waiting {wait} seconds before retrying...")
        time.sleep(wait)


def update_player(username):

    print(f"Updating {username}...")

    response = request_with_retry(
        "POST",
        f"{BASE_URL}/players/{username}",
        headers=HEADERS
    )

    return response.json()


def get_player(username):

    response = request_with_retry(
        "GET",
        f"{BASE_URL}/players/{username}",
        headers=HEADERS
    )

    return response.json()


def get_daily_gains(username):

    response = request_with_retry(
        "GET",
        f"{BASE_URL}/players/{username}/gained?period=day",
        headers=HEADERS
    )

    return response.json()


def update_all(players):

    for player in players:
        try:
            update_player(player)
        except Exception as e:
            print(f"Failed to update {player}: {e}")

    print(f"Waiting {UPDATE_WAIT} seconds...")

    time.sleep(UPDATE_WAIT)