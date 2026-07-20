from config import PLAYERS
from wom import update_all, get_daily_gains
from formatter import build_embed, has_activity
from discord_webhook import send_embed


def main():

    print("Updating players...")

    update_all(PLAYERS)

    results = {}

    for player in PLAYERS:

        print(f"Fetching gains for {player}")

        results[player] = get_daily_gains(player)

    # Don't send anything if nobody had activity.
    if not any(has_activity(data) for data in results.values()):
        print("No activity for any tracked player. Skipping Discord notification.")
        return

    embed = build_embed(results)

    print("Sending Discord message...")

    send_embed(embed)

    print("Done.")


if __name__ == "__main__":
    main()