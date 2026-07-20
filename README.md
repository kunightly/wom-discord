# WOM Notify

Automatically updates Wise Old Man players and posts a daily activity report to Discord using webhooks.

The bot checks Wise Old Man for the daily activity of tracked players (currently `kn1ghtley` and `ramleh`) via the API. If at least one player has activity, it sends a formatted Discord report. It also sends a Telegram notification via Hermes every day indicating whether activity was detected.

## Features

- Daily Wise Old Man player updates
- Formatted Discord webhook reports
- Telegram daily reset notifications
- Automatically skips Discord reports when no tracked players have activity
- Supports multiple tracked players
- Cron-friendly
- Easy configuration using `.env`

## Installation

```bash
git clone git@github.com:kunightly/wom-notify.git

cd wom-notify

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```ini
WOM_API_KEY=YOUR_API_KEY
DISCORD_WEBHOOK=YOUR_WEBHOOK
WOM_USER_AGENT=Knightly-WOM-Notify/1.0
```

Run manually:

```bash
python3 main.py
```

## Notifications

### Discord
- Sends a detailed daily report when one or more tracked players have activity.
- Does not send a report if all tracked players have no activity.

### Telegram
Always sends a daily reset notification.

Examples:

```
⏰ OSRS Daily Reset - 0 GMT. No activity to report.
```

```
⏰ OSRS Daily Reset - 0 GMT. Activity from Ramleh.
```

```
⏰ OSRS Daily Reset - 0 GMT. Activity from Kn1ghtley.
```

```
⏰ OSRS Daily Reset - 0 GMT. Activity from Ramleh and Kn1ghtley.
```
