#!/usr/bin/env python3.7

recipes = {
    "Arcane Elixir": {
        "ID":       9155,
        "Learn":    235,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
            "Blindweed": 1,
            "Goldthorn": 1,
            "Crystal Vial": 1
        }
    },
    "Blackmouth Oil": {
        "ID":       6370,
        "Learn":    80,
        "Yellow":   80,
        "Green":    90,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Oily Blackmouth": 2,
            "Empty Vial": 1
        }
    },
    "Catseye Elixir": {
        "ID":       10592,
        "Learn":    200,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Goldthorn": 1,
            "Fadeleaf": 1,
            "Leaded Vial": 1
        }
    },
    "Discolored Healing Potion": {
        "ID":       4596,
        "Learn":    50,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Quest",
        "Faction":  "Horde",
        "Reagents": {
            "Discolored Worg Heart": 1,
            "Peacebloom": 1,
            "Empty Vial": 1
        }
    },
    "Dreamless Sleep Potion": {
        "ID":       12190,
        "Learn":    230,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Purple Lotus": 3,
            "Crystal Vial": 1
        }
    },
    "Elixir of Agility": {
        "ID":       8949,
        "Learn":    185,
        "Yellow":   205,
        "Green":    225,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
            "Stranglekelp": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Brute Force": {
        "ID":       13453,
        "Learn":    275,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Gromsblood": 2,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Elixir of Defence": {
        "ID":       3389,
        "Learn":    130,
        "Yellow":   155,
        "Green":    175,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Wild Steelbloom": 1,
            "Stranglekelp": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Demonslaying": {
        "ID":       9224,
        "Learn":    250,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Gromsblood": 1,
            "Ghost Mushroom": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of Detect Demon": {
        "ID":       9233,
        "Learn":    250,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Trainer",
        "Reagents": {
            "Gromsblood": 2,
            "Crystal Vial": 1
        }
    },
    "Elixir of Detect Lesser Invisibility": {
        "ID":       3828,
        "Learn":    195,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Drop",
        "Reagents": {
            "Khadgars Whisker": 1,
            "Fadeleaf": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Detect Undead": {
        "ID":       9154,
        "Learn":    230,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Arthas Tears": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of Dream Vision": {
        "ID":       9197,
        "Learn":    240,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Drop",
        "Reagents": {
            "Purple Lotus": 3,
            "Crystal Vial": 1
        }
    },
    "Elixir of Firepower": {
        "ID":       6373,
        "Learn":    140,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Fire Oil": 2,
            "Kingsblood": 1, 
            "Leaded Vial": 1
        }
    },
    "Elixir of Fortitude": {
        "ID":       3825,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
            "Wild Steelbloom": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Frost Power": {
        "ID":       17708,
        "Learn":    190,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Drop",
        "Reagents": {
            "Wintersbite": 2,
            "Khadgars Whisker": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Giant Growth": {
        "ID":       6662,
        "Learn":    90,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Drop",
        "Reagents": {
            "Deviate Fish": 1,
            "Earthroot": 1,
            "Empty Vial": 1
        }
    },
    "Elixir of Giants": {
        "ID":       9206,
        "Learn":    245,
        "Yellow":   260,
        "Green":    280,
        "Grey":     300,
        "Source":   "Drop",
        "Reagents": {
            "Sungrass": 1,
            "Gromsblood": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of Greater Agility": {
        "ID":       9187,
        "Learn":    240,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Trainer",
        "Reagents": {
            "Sungrass": 1,
            "Goldthorn": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of Greater Defense": {
        "ID":       8951,
        "Learn":    195,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Wild Steelbloom": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Greater Firepower": {
        "ID":       21546,
        "Learn-PHASE-5":    250,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Drop",
        "Reagents": {
            "Fire Oil": 3,
            "Firebloom": 3,
            "Crystal Vial": 1
        }
    },
    "Elixir of Greater Intellect": {
        "ID":       9179,
        "Learn":    235,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
            "Blindweed": 1,
            "Khadgars Whisker": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of Greater Water Breathing": {
        "ID":       18294,
        "Learn":    215,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Ichor of Undeath": 1,
            "Purple Lotus": 2,
            "Crystal Vial": 1
        }
    },
    "Elixir of Lesser Agility": {
        "ID":       3390,
        "Learn":    140,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Drop",
        "Reagents": {
            "Wild Steelbloom": 1,
            "Swiftthistle": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Lions Strength": {
        "ID":       2454,
        "Learn":    1,
        "Yellow":   55,
        "Green":    75,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
            "Earthroot": 1,
            "Silverleaf": 1,
            "Empty Vial": 1
        }
    },
    "Elixir of Minor Agility": {
        "ID":       2457,
        "Learn":    50,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Drop",
        "Reagents": {
            "Swiftthistle": 1,
            "Silverleaf": 1,
            "Empty Vial": 1
        }
    },
    "Elixir of Minor Defense": {
        "ID":       5997,
        "Learn":    1,
        "Yellow":   55,
        "Green":    75,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
            "Silverleaf": 2,
            "Empty Vial": 1
        }
    },
    "Elixir of Minor Fortitude": {
        "ID":       2458,
        "Learn":    50,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Earthroot": 2,
            "Peacebloom": 1,
            "Empty Vial": 1
        }
    },
    "Elixir of Ogres Strength": {
        "ID":       3391,
        "Learn":    150,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Drop",
        "Reagents": {
            "Earthroot": 1,
            "Kingsblood": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Poison Resistance": {
        "ID":       3386,
        "Learn":    120,
        "Yellow":   145,
        "Green":    165,
        "Grey":     185,
        "Source":   "Drop",
        "Reagents": {
            "Large Venom Sac": 1,
            "Bruiseweed": 1,
            "Leaded Vial": 1
        }
    },
    "Elixir of Shadow Power": {
        "ID":       9264,
        "Learn":    250,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Ghost Mushroom": 3,
            "Crystal Vial": 1
        }
    },
    "Elixir of Superior Defense": {
        "ID":       13445,
        "Learn":    265,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Stonescale Oil": 2,
            "Sungrass": 1,
            "Crystal Vial": 1
        }
    },
    "Elixir of the Mongoose": {
        "ID":       13452,
        "Learn":    280,
        "Yellow":   295,
        "Green":    315,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Mountain Silversage": 2,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Elixir of the Sages": {
        "ID":       13447,
        "Learn":    270,
        "Yellow":   285,
        "Green":    305,
        "Grey":     325,
        "Source":   "Drop",
        "Reagents": {
            "Dreamfoil": 1,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Elixir of Water Breathing": {
        "ID":       5996,
        "Learn":    90,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Stranglekelp": 1,
            "Blackmouth Oil": 2,
            "Empty Vial": 1
        }
    },
    "Elixir of Wisdom": {
        "ID":       3383,
        "Learn":    90,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Mageroyal": 1,
            "Briarthorn": 2,
            "Empty Vial": 1
        }
    },
    "Fire Oil": {
        "ID":       6371,
        "Learn":    130,
        "Yellow":   150,
        "Green":    160,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Firefin Snapper": 2,
            "Empty Vial": 1
        }
    },
    "Fire Protection Potion": {
        "ID":       6049,
        "Learn":    165,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
            "Small Flame Sac": 1,
            "Fire Oil": 1,
            "Leaded Vial": 1
        }
    },
    "Free Action Potion": {
        "ID":       5634,
        "Learn":    150,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Vendor",
        "Reagents": {
            "Blackmouth Oil": 2,
            "Stranglekelp": 1,
            "Leaded Vial": 1
        }
    },
    "Frost Oil": {
        "ID":       3829,
        "Learn":    200,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Vendor",
        "Reagents": {
            "Khadgars Whisker": 4,
            "Wintersbite": 2,
            "Leaded Vial": 1
        }
    },
    "Frost Protection Potion": {
        "ID":       6050,
        "Learn":    190,
        "Yellow":   205,
        "Green":    225,
        "Grey":     245,
        "Source":   "Vendor",
        "Reagents": {
            "Wintersbite": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Ghost Dye": {
        "ID":       9210,
        "Learn":    245,
        "Yellow":   260,
        "Green":    280,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
            "Ghost Mushroom": 2,
            "Purple Dye": 1,
            "Crystal Vial": 1
        }
    },
    "Gift of Arthas": {
        "ID":       9088,
        "Learn":    240,
        "Yellow":   255,
        "Green":    275,
        "Grey":     295,
        "Source":   "Drop",
        "Reagents": {
            "Arthas Tears": 1,
            "Blindweed": 1,
            "Crystal Vial": 1
        }
    },
    "Goblin Rocket Fuel": {
        "ID":       9061,
        "Learn":    210,
        "Yellow":   225,
        "Green":    245,
        "Grey":     265,
        "Source":   "Crafted",
        "Reagents": {
            "Firebloom": 1,
            "Volatile Rum": 1,
            "Leaded Vial": 1
        }
    },
    "Great Rage Potion": {
        "ID":       5633,
        "Learn":    175,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Vendor",
        "Reagents": {
            "Large Fang": 1,
            "Kingsblood": 1,
            "Leaded Vial": 1
        }
    },
    "Greater Arcane Elixir": {
        "ID":       13454,
        "Learn":    285,
        "Yellow":   300,
        "Green":    320,
        "Grey":     340,
        "Source":   "Drop",
        "Reagents": {
            "Dreamfoil": 3,
            "Mountain Silversage": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Arcane Protection Potion": {
        "ID":       13461,
        "Learn":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "Reagents": {
            "Dream Dust": 1,
            "Dreamfoil": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Dreamless Sleep Potion": {
        "ID":       20002,
        "Learn-PHASE-5":    275,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Vendor",
        "Reagents": {
            "Dreamfoil": 2,
            "Golden Sansam": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Fire Protection Potion": {
        "ID":       13457,
        "Learn":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "Reagents": {
            "Elemental Fire": 1,
            "Dreamfoil": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Frost Protection Potion": {
        "ID":       13456,
        "Learn":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "Reagents": {
            "Elemental Water": 1,
            "Dreamfoil": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Healing Potion": {
        "ID":       1710,
        "Learn":    155,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
            "Liferoot": 1,
            "Kingsblood": 1,
            "Leaded Vial": 1
        }
    },
    "Greater Mana Potion": {
        "ID":       6149,
        "Learn":    205,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Khadgars Whisker": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Greater Nature Protection Potion": {
        "ID":       13458,
        "Learn":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "Reagents": {
            "Elemental Earth": 1,
            "Dreamfoil": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Shadow Protection Potion": {
        "ID":       13459,
        "Learn":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Drop",
        "Reagents": {
            "Shadow Oil": 1,
            "Dreamfoil": 1,
            "Crystal Vial": 1
        }
    },
    "Greater Stoneshield Potion": {
        "ID":       13455,
        "Learn":    280,
        "Yellow":   295,
        "Green":    315,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Stonescale Oil": 3,
            "Thorium Ore": 1,
            "Crystal Vial": 1
        }
    },
    "Healing Potion": {
        "ID":       929,
        "Learn":    110,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
            "Bruiseweed": 1,
            "Briarthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Holy Protection Potion": {
        "ID":       6051,
        "Learn":    100,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Reagents": {
            "Bruiseweed": 1,
            "Swiftthistle": 1,
            "Empty Vial": 1
        }
    },
    "Invisibility Potion": {
        "ID":       9172,
        "Learn":    235,
        "Yellow":   250,
        "Green":    270,
        "Grey":     290,
        "Source":   "Drop",
        "Reagents": {
            "Ghost Mushroom": 1,
            "Sungrass": 1,
            "Crystal Vial": 1
        }
    },
    "Lesser Healing Potion": {
        "ID":       858,
        "Learn":    55,
        "Yellow":   85,
        "Green":    105,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
            "Minor Healing Potion": 1,
            "Briarthorn": 1
        }
    },
    "Lesser Invisibility Potion": {
        "ID":       3823,
        "Learn":    165,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
            "Fadeleaf": 1,
            "Wild Steelbloom": 1,
            "Leaded Vial": 1
        }
    },
    "Lesser Mana Potion": {
        "ID":       3385,
        "Learn":    120,
        "Yellow":   145,
        "Green":    165,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
            "Mageroyal": 1,
            "Stranglekelp": 1,
            "Empty Vial": 1
        }
    },
    "Lesser Stoneshield Potion": {
        "ID":       4623,
        "Learn":    215,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Mithril Ore": 1,
            "Goldthorn": 1,
            "Leaded Vial": 1
        }
    },
    "Limited Invulnerability Potion": {
        "ID":       3387,
        "Learn":    250,
        "Yellow":   275,
        "Green":    295,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
            "Blindweed": 2,
            "Ghost Mushroom": 1,
            "Crystal Vial": 1
        }
    },
    "Living Action Potion": {
        "ID":       20008,
        "Learn-PHASE-5":    285,
        "Yellow":   300,
        "Green":    320,
        "Grey":     340,
        "Source":   "Vendor",
        "Reagents": {
            "Icecap": 2,
            "Mountain Silversage": 2,
            "Heart of the Wild": 2,
            "Crystal Vial": 1
        }
    },
    "Mageblood Potion": {
        "ID":       20007,
        "Learn-PHASE-5":    275,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Vendor",
        "Reagents": {
            "Dreamfoil": 1,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Magic Resistance Potion": {
        "ID":       9036,
        "Learn":    210,
        "Yellow":   225,
        "Green":    245,
        "Grey":     265,
        "Source":   "Drop",
        "Reagents": {
            "Khadgars Whisker": 1,
            "Purple Lotus": 1,
            "Crystal Vial": 1
        }
    },
    "Major Healing Potion": {
        "ID":       13446,
        "Learn":    275,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Vendor",
        "Reagents": {
            "Golden Sansam": 2,
            "Mountain Silversage": 1,
            "Crystal Vial": 1
        }
    },
    "Major Mana Potion": {
        "ID":       13444,
        "Learn":    295,
        "Yellow":   310,
        "Green":    325,
        "Grey":     345,
        "Source":   "Vendor",
        "Reagents": {
            "Dreamfoil": 3,
            "Icecap": 2,
            "Crystal Vial": 1
        }
    },
    "Major Trolls Blood Potion": {
        "ID":       20004,
        "Learn-PHASE-5":    290,
        "Yellow":   305,
        "Green":    325,
        "Grey":     345,
        "Source":   "Vendor",
        "Reagents": {
            "Gromsblood": 1,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Mana Potion": {
        "ID":       3827,
        "Learn":    160,
        "Yellow":   180,
        "Green":    200,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
            "Stranglekelp": 1,
            "Kingsblood": 1,
            "Leaded Vial": 1
        }
    },
    "Mighty Rage Potion": {
        "ID":       13442,
        "Learn":    255,
        "Yellow":   270,
        "Green":    290,
        "Grey":     310,
        "Source":   "Drop",
        "Reagents": {
            "Gromsblood": 3,
            "Crystal Vial": 1
        }
    },
    "Mighty Trolls Blood Potion": {
        "ID":       3826,
        "Learn":    180,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Drop",
        "Reagents": {
            "Liferoot": 1,
            "Bruiseweed": 1,
            "Leaded Vial": 1
        }
    },
    "Minor Healing Potion": {
        "ID":       118,
        "Learn":    1,
        "Yellow":   55,
        "Green":    75,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
            "Peacebloom": 1,
            "Silverleaf": 1,
            "Empty Vial": 1
        }
    },
    "Minor Magic Resistance Potion": {
        "ID":       3384,
        "Learn":    110,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Drop",
        "Reagents": {
            "Mageroyal": 3,
            "Wild Steelbloom": 1,
            "Empty Vial": 1
        }
    },
    "Minor Mana Potion": {
        "ID":       2455,
        "Learn":    25,
        "Yellow":   65,
        "Green":    85,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
            "Mageroyal": 1,
            "Silverleaf": 1,
            "Empty Vial": 1
        }
    },
    "Minor Rejuvenation Potion": {
        "ID":       2456,
        "Learn":    25,
        "Yellow":   65,
        "Green":    85,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
            "Mageroyal": 2,
            "Peacebloom": 1,
            "Empty Vial": 1
        }
    },
    "Nature Protection Potion": {
        "ID":       6052,
        "Learn":    190,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
            "Liferoot": 1,
            "Stranglekelp": 1,
            "Leaded Vial": 1
        }
    },
    "Oil of Immolation": {
        "ID":       8956,
        "Learn":    205,
        "Yellow":   220,
        "Green":    240,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Firebloom": 1,
            "Goldthorn": 1,
            "Crystal Vial": 1
        }
    },
    "Purification Potion": {
        "ID":       13462,
        "Learn":    285,
        "Yellow":   300,
        "Green":    320,
        "Grey":     340,
        "Source":   "Drop",
        "Reagents": {
            "Icecap": 2,
            "Plaguebloom": 2,
            "Crystal Vial": 1
        }
    },
    "Rage Potion": {
        "ID":       5631,
        "Learn":    60,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Reagents": {
            "Sharp Claw": 1,
            "Briarthorn": 1,
            "Empty Vial": 1
        }
    },
    "Restorative Potion": {
        "ID":       9030,
        "Learn":    215,
        "Yellow":   225,
        "Green":    245,
        "Grey":     265,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Elemental Earth": 1,
            "Goldthorn": 1,
            "Crystal Vial": 1
        }
    },
    "Shadow Oil": {
        "ID":       3824,
        "Learn":    165,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Vendor",
        "Reagents": {
            "Fadeleaf": 4,
            "Grave Moss": 4,
            "Leaded Vial": 1
        }
    },
    "Shadow Protection Potion": {
        "ID":       6048,
        "Learn":    135,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Reagents": {
            "Grave Moss": 1,
            "Kingsblood": 1,
            "Leaded Vial": 1
        }
    },
    "Stonescale Oil": {
        "ID":       13423,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Stonescale Eel": 1,
            "Leaded Vial": 1
        }
    },
    "Strong Trolls Blood Potion": {
        "ID":       3388,
        "Learn":    125,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bruiseweed": 2,
            "Briarthorn": 2,
            "Leaded Vial": 1
        }
    },
    "Superior Healing Potion": {
        "ID":       3928,
        "Learn":    215,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Sungrass": 1,
            "Khadgars Whisker": 1,
            "Crystal Vial": 1
        }
    },
    "Superior Mana Potion": {
        "ID":       13443,
        "Learn":    260,
        "Yellow":   275,
        "Green":    295,
        "Grey":     315,
        "Source":   "Vendor",
        "Reagents": {
            "Sungrass": 2,
            "Blindweed": 2,
            "Crystal Vial": 1
        }
    },
    "Swiftness Potion": {
        "ID":       2459,
        "Learn":    60,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Drop",
        "Reagents": {
            "Swiftthistle": 1,
            "Briarthorn": 1,
            "Empty Vial": 1
        }
    },
    "Swim Speed Potion": {
        "ID":       6372,
        "Learn":    100,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Swiftthistle": 1,
            "Blackmouth Oil": 1,
            "Empty Vial": 1
        }
    },
    "Weak Trolls Blood Potion": {
        "ID":       3382,
        "Learn":    15,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Peacebloom": 1,
            "Earthroot": 2,
            "Empty Vial": 1
        }
    },
    "Wildvine Potion": {
        "ID":       9144,
        "Learn":    225,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Drop",
        "Reagents": {
            "Wildvine": 1,
            "Purple Lotus": 1,
            "Crystal Vial": 1
        }
    },
}

import json
with open('alchemy.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)