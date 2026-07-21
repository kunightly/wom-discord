# Maps Wise Old Man skill/boss keys -> Discord custom emoji tags.
# Format is <:name:id> - the "name" part can be anything readable,
# Discord renders based on the numeric id.

SKILL_EMOJIS = {
    "overall":       "<:overall:720446212356177951>",
    "sailing":       "<:sailing:1437131470698446990>",
    "magic":         "<:magic:706462611243532330>",
    "ranged":        "<:ranged:706462611222429796>",
    "hitpoints":     "<:hitpoints:706462611050332258>",
    "slayer":        "<:slayer:706462611222298654>",
    "agility":       "<:agility:706462611121897483>",
    "construction":  "<:construction:706462610853330986>",
    "defence":       "<:defence:706462611000000589>",
    "farming":       "<:farming:706462611364904980>",
    "strength":      "<:strength:706462610916114483>",
    "woodcutting":   "<:woodcutting:706462611205783562>",
    "fishing":       "<:fishing:706462611415236618>",
    "attack":        "<:attack:706462610840879146>",
    "hunter":        "<:hunter:706462611218366534>",
    "thieving":      "<:thieving:706462611214172240>",
    "mining":        "<:mining:706462611134349413>",
    "prayer":        "<:prayer:706462610949931049>",
    "crafting":      "<:crafting:706462610920308761>",
    "firemaking":    "<:firemaking:706462611209977907>",
    "fletching":     "<:fletching:706462611075629138>",
    "smithing":      "<:smithing:706462610945736706>",
    "cooking":       "<:cooking:706462611075629128>",
    "runecrafting":  "<:runecrafting:706462611327287347>",
    "herblore":      "<:herblore:706462611012583456>",
}

BOSS_EMOJIS = {
    "mimic":              "<:mimic:730169728357761145>",
    "alchemical_hydra":   "<:alchemical_hydra:729839921207967765>",
    "kraken":             "<:kraken:729840084798406767>",
    "araxxor":            "<:araxxor:1278337345069781082>",
    "cerberus":           "<:cerberus:729839921401167954>",
}

MISC_EMOJIS = {
    "clue_scroll":        "<:clue_scroll:729844134004785204>",
    "collection_log":     "<:collection_log:1334481313801179236>",
}


def skill_emoji(name):
    """Returns the emoji tag for a skill, or empty string if we don't have one."""
    return SKILL_EMOJIS.get(name, "")


def boss_emoji(name):
    """Returns the emoji tag for a boss, or empty string if we don't have one."""
    return BOSS_EMOJIS.get(name, "")