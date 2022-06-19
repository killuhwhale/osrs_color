from enum import Enum, unique


@unique
class Items(Enum):
    '''
        Map to Screenshot which are used as needle images to search in a space.
    '''

    AIR_RUNE = {"n": "AIR_RUNE", "conf": 0.80, "grayscale": False}
    EARTH_RUNE = {"n": "EARTH_RUNE", "conf": 0.80, "grayscale": False}
    WATER_RUNE = {"n": "WATER_RUNE", "conf": 0.80, "grayscale": False}
    FIRE_RUNE = {"n": "FIRE_RUNE", "conf": 0.80, "grayscale": False}
    LAW_RUNE = {"n": "LAW_RUNE", "conf": 0.80, "grayscale": False}
    COSMIC_RUNE = {"n": "COSMIC_RUNE", "conf": 0.80, "grayscale": False}
    BLOOD_RUNE = {"n": "BLOOD_RUNE", "conf": 0.80, "grayscale": False}
    NATURE_RUNE = {"n": "NATURE_RUNE", "conf": 0.80, "grayscale": False}
    DEATH_RUNE = {"n": "DEATH_RUNE", "conf": 0.80, "grayscale": False}
    BODY_RUNE = {"n": "BODY_RUNE", "conf": 0.80, "grayscale": False}
    CHAOS_RUNE = {"n": "CHAOS_RUNE", "conf": 0.80, "grayscale": False}
    ASTRAL_RUNE = {"n": "ASTRAL_RUNE", "conf": 0.80, "grayscale": False}
    SOUL_RUNE = {"n": "SOUL_RUNE", "conf": 0.80, "grayscale": False}
    WRATH_RUNE = {"n": "WRATH_RUNE", "conf": 0.80, "grayscale": False}
    DUST_RUNE = {"n": "DUST_RUNE", "conf": 0.80, "grayscale": False}
    MUD_RUNE = {"n": "MUD_RUNE", "conf": 0.80, "grayscale": False}
    SMOKE_RUNE = {"n": "SMOKE_RUNE", "conf": 0.80, "grayscale": False}
    STEAM_RUNE = {"n": "STEAM_RUNE", "conf": 0.80, "grayscale": False}
    LAVA_RUNE = {"n": "LAVA_RUNE", "conf": 0.80, "grayscale": False}
    MIND_RUNE = {"n": "MIND_RUNE", "conf": 0.80, "grayscale": False}

    RUNE_SKIM = {"n": "RUNE_SKIM", "conf": 0.80, "grayscale": False}
    STAFF_OF_AIR = {"n": "STAFF_OF_AIR", "conf": 0.80, "grayscale": False}
    STAFF_OF_FIRE = {"n": "STAFF_OF_FIRE", "conf": 0.80, "grayscale": False}
    SWORDFISH = {"n": "SWORDFISH", "conf": 0.80, "grayscale": False}

    RAW_SHRIMP = {"n": "RAW_SHRIMP", "conf": 0.80, "grayscale": False}
    LOGS = {"n": "LOGS", "conf": 0.80, "grayscale": False}
    TINDERBOX = {"n": "TINDERBOX", "conf": 0.80, "grayscale": False}

    BRONZE_BAR = {"n": "BRONZE_BAR", "conf": 0.80, "grayscale": False}
    BLURITE_BAR = {"n": "BLURITE_BAR", "conf": 0.80, "grayscale": False}
    IRON_BAR = {"n": "IRON_BAR", "conf": 0.80, "grayscale": False}
    SILVER_BAR = {"n": "SILVER_BAR", "conf": 0.80, "grayscale": False}
    ELEMENTAL_BAR = {"n": "ELEMENTAL_BAR", "conf": 0.80, "grayscale": False}
    STEEL_BAR = {"n": "STEEL_BAR", "conf": 0.80, "grayscale": False}
    GOLD_BAR = {"n": "GOLD_BAR", "conf": 0.80, "grayscale": False}
    LOVAKITE_BAR = {"n": "LOVAKITE_BAR", "conf": 0.80, "grayscale": False}
    MITHRIL_BAR = {"n": "MITHRIL_BAR", "conf": 0.80, "grayscale": False}
    ADAMANTITE_BAR = {"n": "ADAMANTITE_BAR", "conf": 0.80, "grayscale": False}
    RUNITE_BAR = {"n": "RUNITE_BAR", "conf": 0.80, "grayscale": False}

    SAPPHIRE = {"n": "SAPPHIRE", "conf": 0.80, "grayscale": False}
    EMERALD = {"n": "EMERALD", "conf": 0.80, "grayscale": False}
    RUBY = {"n": "RUBY", "conf": 0.80, "grayscale": False}
    DIAMOND = {"n": "DIAMOND", "conf": 0.80, "grayscale": False}
    OPAL = {"n": "OPAL", "conf": 0.80, "grayscale": False}
    RED_TOPAZ = {"n": "RED_TOPAZ", "conf": 0.80, "grayscale": False}
    DRAGONSTONE = {"n": "DRAGONSTONE", "conf": 0.80, "grayscale": False}
    ONYX = {"n": "ONYX", "conf": 0.80, "grayscale": False}
    ZENYTE = {"n": "ZENYTE", "conf": 0.80, "grayscale": False}

    SAPPHIRE_UNCUT = {"n": "SAPPHIRE_UNCUT", "conf": 0.80, "grayscale": False}
    EMERALD_UNCUT = {"n": "EMERALD_UNCUT", "conf": 0.80, "grayscale": False}
    RUBY_UNCUT = {"n": "RUBY_UNCUT", "conf": 0.80, "grayscale": False}
    DIAMOND_UNCUT = {"n": "DIAMOND_UNCUT", "conf": 0.80, "grayscale": False}
    OPAL_UNCUT = {"n": "OPAL_UNCUT", "conf": 0.80, "grayscale": False}
    RED_TOPAZ_UNCUT = {"n": "RED_TOPAZ_UNCUT",
                       "conf": 0.80, "grayscale": False}
    DRAGONSTONE_UNCUT = {"n": "DRAGONSTONE_UNCUT",
                         "conf": 0.80, "grayscale": False}
    ONYX_UNCUT = {"n": "ONYX_UNCUT", "conf": 0.80, "grayscale": False}
    ZENYTE_UNCUT = {"n": "ZENYTE_UNCUT", "conf": 0.80, "grayscale": False}

    BRACELET_SAPPHIRE = {"n": "BRACELET_SAPPHIRE",
                         "conf": 0.80, "grayscale": False}
    BRACELET_EMERALD = {"n": "BRACELET_EMERALD",
                        "conf": 0.80, "grayscale": False}
    BRACELET_RUBY = {"n": "BRACELET_RUBY", "conf": 0.80, "grayscale": False}
    BRACELET_DIAMOND = {"n": "BRACELET_DIAMOND",
                        "conf": 0.80, "grayscale": False}
    BRACELET_OPAL = {"n": "BRACELET_OPAL", "conf": 0.80, "grayscale": False}
    BRACELET_RED_TOPAZ = {"n": "BRACELET_RED_TOPAZ",
                          "conf": 0.80, "grayscale": False}
    BRACELET_DRAGONSTONE = {"n": "BRACELET_DRAGONSTONE",
                            "conf": 0.80, "grayscale": False}
    BRACELET_ONYX = {"n": "BRACELET_ONYX", "conf": 0.80, "grayscale": False}
    BRACELET_ZENYTE = {"n": "BRACELET_ZENYTE",
                       "conf": 0.80, "grayscale": False}

    def __str__(self):
        return self.name
