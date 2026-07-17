from config import PLAYERS
from wom import update_all, get_daily_gains
from formatter import build_embed
from discord_webhook import send_embed


def main():

    print("Updating players...")

    update_all(PLAYERS)

    results = {}

    for player in PLAYERS:

        print(f"Fetching gains for {player}")

        results[player] = get_daily_gains(player)

    embed = build_embed(results)

    print("Sending Discord message...")

    send_embed(embed)

    print("Done.")


if __name__ == "__main__":
    main()
