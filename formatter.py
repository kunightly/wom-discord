from datetime import datetime


def fmt(num):
    return f"{num:,}"


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
        description += f"**Total XP:** +{fmt(total_xp)}\n\n"

        levelups = []

        for name, skill in skills.items():

            if name == "overall":
                continue

            start = skill["level"]["start"]
            end = skill["level"]["end"]

            if end > start:
                levelups.append(f"• {name.title()} {start} → {end}")

        if levelups:
            description += "**⭐ Level Ups**\n"
            description += "\n".join(levelups)
            description += "\n\n"

        gained_skills = []

        for name, skill in skills.items():

            if name == "overall":
                continue

            xp = skill["experience"]["gained"]

            if xp > 0:
                gained_skills.append((xp, name))

        gained_skills.sort(reverse=True)

        if gained_skills:

            description += "**📈 Skill Gains**\n"

            for xp, skill in gained_skills[:8]:
                description += f"• {skill.title():15} +{fmt(xp)} XP\n"

            description += "\n"

        bosses_gained = []

        for name, boss in bosses.items():

            kc = boss["kills"]["gained"]

            if kc > 0:
                bosses_gained.append((kc, name))

        bosses_gained.sort(reverse=True)

        if bosses_gained:

            description += "**👹 Boss KC**\n"

            for kc, boss in bosses_gained:
                boss = boss.replace("_", " ").title()
                description += f"• {boss:30} +{kc}\n"

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