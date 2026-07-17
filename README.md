# WOM Discord

Automatically updates Wise Old Man players and posts a daily Discord report to a Discord channel using webhooks.

## Features

- Daily player updates
- Discord webhook reports
- Multiple players
- Cron support
- Easy configuration using `.env`

## Installation

```bash
git clone git@github.com:kunightly/wom-discord.git

cd wom-discord

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```ini
WOM_API_KEY=YOUR_API_KEY
DISCORD_WEBHOOK=YOUR_WEBHOOK
WOM_USER_AGENT=Knightly-WOM-Discord/1.0
```

Run:

```bash
python main.py
```
