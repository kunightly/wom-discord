from datetime import datetime

from emojis import skill_emoji, boss_emoji

COMBAT_SKILLS = ["prayer", "attack", "strength", "defence", "hitpoints", "ranged", "magic"]


def fmt(num):
    return f"{num:,}"


def fmt_xp(num):
    """Compact XP formatting: 50101 -> '50.1k', 2_400_000 -> '2.4m', 320 -> '320'."""

    if num >= 1_000_000:
        return f"{num / 1_000_000:.1f}m"

    if num >= 1000:
        return f"{num / 1000:.1f}k"

    return str(num)


def format_skill_line(name, xp, start, end):

    emoji = skill_emoji(name)
    xp_str = fmt_xp(xp)

    if end > start:
        return f"• {emoji} {name.title()} {start} → {end} +{xp_str}"

    return f"• {emoji} {name.title()} +{xp_str}"


def build_embed(results):

    description = ""

    daily_winner = None
    highest_xp = -1

    for player, data in results.items():

        skills = data["data"]["skills"]
        bosses = data["data"]["bosses"]

        total_xp = skills["overall"]["experience"]["gained"]

        if total_xp > highest_xp:
            highest_xp = total_xp
            daily_winner = player

        description += f"## ⚔ {player.title()}\n\n"
        description += f"**{skill_emoji('overall')} Total EXP:** +{fmt_xp(total_xp)}\n\n"

        # Collect every skill with xp gained this period, keyed by name
        skill_entries = {}

        for name, skill in skills.items():

            if name == "overall":
                continue

            xp = skill["experience"]["gained"]

            if xp > 0:
                skill_entries[name] = {
                    "xp": xp,
                    "start": skill["level"]["start"],
                    "end": skill["level"]["end"]
                }

        # Pull out combat skills first, in the fixed order
        combat_lines = []

        for name in COMBAT_SKILLS:
            if name in skill_entries:
                entry = skill_entries.pop(name)
                combat_lines.append(format_skill_line(name, entry["xp"], entry["start"], entry["end"]))

        # Remaining skills, sorted by xp gained (highest first), capped at 8
        other_entries = sorted(
            skill_entries.items(),
            key=lambda item: item[1]["xp"],
            reverse=True
        )[:8]

        other_lines = [
            format_skill_line(name, entry["xp"], entry["start"], entry["end"])
            for name, entry in other_entries
        ]

        if combat_lines or other_lines:

            description += "**Experience Gains**\n"

            if combat_lines:
                description += "\n".join(combat_lines) + "\n"

            if combat_lines and other_lines:
                description += "\n"

            if other_lines:
                description += "\n".join(other_lines) + "\n"

            description += "\n"

        bosses_gained = []

        for name, boss in bosses.items():

            kc = boss["kills"]["gained"]

            if kc > 0:
                bosses_gained.append((kc, name))

        bosses_gained.sort(reverse=True)

        if bosses_gained:

            description += f"**Slain Bosses**\n"

            for kc, boss in bosses_gained:
                emoji = boss_emoji(boss)
                boss_name = boss.replace("_", " ").title()
                description += f"  {emoji} {boss_name} {kc}\n"

            description += "\n"

        description += "──────────────────────\n\n"

    embed = {
        "title": "📊 Wise Old Man Daily Report",
        "description": description,
        "color": 3447003,
        "footer": {
            "text": f"Daily MVP: {daily_winner} ({fmt(highest_xp)} XP)"
        },
        "timestamp": datetime.utcnow().isoformat()
    }

    return embed


def has_activity(data):

    skills = data["data"]["skills"]
    bosses = data["data"]["bosses"]
    activities = data["data"]["activities"]

    # Total XP gained
    if skills["overall"]["experience"]["gained"] > 0:
        return True

    # Any level up
    for skill in skills.values():
        if skill["level"]["end"] > skill["level"]["start"]:
            return True

    # Any boss KC gained
    for boss in bosses.values():
        if boss["kills"]["gained"] > 0:
            return True

    # Any activity score gained
    for activity in activities.values():
        if activity["score"]["gained"] > 0:
            return True

    return False
