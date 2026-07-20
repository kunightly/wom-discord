from config import PLAYERS
from wom import update_all, get_daily_gains
from formatter import build_embed, has_activity
from discord_webhook import send_embed
from telegram import send_gmt_message


def main():

    print("Updating players...")

    update_all(PLAYERS)

    results = {}

    for player in PLAYERS:

        print(f"Fetching gains for {player}")

        results[player] = get_daily_gains(player)

    active_players = [
        player for player, data in results.items()
        if has_activity(data)
    ]

    if not active_players:

        print("No activity for any tracked player. Skipping Discord notification.")

        telegram_message = "⏰ OSRS Daily Reset - 0 GMT. No activity to report."

        print("Sending Telegram reset notification...")
        send_gmt_message(telegram_message)

        print("Done.")
        return

    embed = build_embed(results)

    print("Sending Discord message...")
    send_embed(embed)

    if len(active_players) == 1:
        telegram_message = f"⏰ OSRS Daily Reset - 0 GMT. Activity from {active_players[0]}."
    else:
        telegram_message = (
            f"⏰ OSRS Daily Reset - 0 GMT. "
            f"Activity from {' and '.join(active_players)}."
        )

    print("Sending Telegram reset notification...")
    send_gmt_message(telegram_message)

    print("Done.")


if __name__ == "__main__":
    main()