#!/usr/bin/env python3.7

recipes = {
    "Baked Salmon": {
        "ID":       13935,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Whitescale Salmon": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Barbecued Buzzard Wing": {
        "ID":       4457,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Buzzard Wing": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Beer Basted Boar Ribs": {
        "ID":       2888,
        "Learn":    25,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Crag Boar Rib": 1,
            "Rhapsody Malt": 1
        },
        "AmountCrafted": 1
    },
    "Big Bear Steak": {
        "ID":       3726,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "Reagents": {
            "Big Bear Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Blood Sausage": {
        "ID":       3220,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Bear Meat": 1,
            "Boar Intestines": 1,
            "Spider Ichor": 1
        },
        "AmountCrafted": 2
    },
    "Boiled Clams": {
        "ID":       5525,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Clam Meat": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1
    },
    "Brilliant Smallfish": {
        "ID":       6290,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Brilliant Smallfish": 1
        },
        "AmountCrafted": 1
    },
    "Bristle Whisker Catfish": {
        "ID":       4593,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Bristle Whiske Catfish": 1
        },
        "AmountCrafted": 1
    },
    "Carrion Surprise": {
        "ID":       12213,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Mystery Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Charred Wolf Meat": {
        "ID":       2679,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Stringy Wolf Meat": 1
        },
        "AmountCrafted": 1
    },
    "Clam Chowder": {
        "ID":       5526,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Clam Meat": 1,
            "Ice Cold Milk": 1,
            "Mild Spices": 1,
        },
        "AmountCrafted": 1
    },
    "Cooked Crab Claw": {
        "ID":       2682,
        "Learn":    85,
        "Yellow":   125,
        "Green":    145,
        "Grey":     165,
        "Source":   "Drop",
        "RecipeID": 2698,
        "Reagents": {
            "Crawler Claw": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Cooked Glossy Mightfish": {
        "ID":       13927,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Glossy Mightfish": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Coyote Steak": {
        "ID":       2684,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Coyote Meat": 1
        },
        "AmountCrafted": 1
    },
    "Crab Cake": {
        "ID":       2683,
        "Learn":    75,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
            "Crawler Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Crispy Bat Wing": {
        "ID":       12224,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "Reagents": {
            "Meaty Bat Wing": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Crispy Lizard Tail": {
        "ID":       5479,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "Reagents": {
            "Thunder Lizard Tail": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 2
    },
    "Crocolisk Gumbo": {
        "ID":       3664,
        "Learn":    120,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Tender Crocolisk Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Crocolisk Steak": {
        "ID":       3662,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Crocolisk Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Curiously Tasty Omelet": {
        "ID":       3665,
        "Learn":    130,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Vendor",
        "Reagents": {
            "Raptor Egg": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Dig Rat Stew": {
        "ID":       5478,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Quest",
        "Faction":  "Horde",
        "Reagents": {
            "Dig Rat": 1
        },
        "AmountCrafted": 2
    },
    "Dragonbreath Chili": {
        "ID":       12217,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Vendor",
        "Reagents": {
            "Mystery Meat": 1,
            "Small Flame Sac": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Dry Pork Ribs": {
        "ID":       2687,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
            "Boar Ribs": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Egg Nog": {
        "ID":       17198,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Seasonal",
        "RecipeID": 17201,
        "Reagents": {
            "Small Egg": 1,
            "Ice Cold Milk": 1,
            "Holiday Spirits": 1,
            "Holiday Spices": 1
        },
        "AmountCrafted": 1
    },
    "Filet of Redgill": {
        "ID":       13930,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Redgill": 1
        },
        "AmountCrafted": 1
    },
    "Fillet of Frenzy": {
        "ID":       5476,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Soft Frenzy Fish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 2
    },
    "Giant Clam Scorcho": {
        "ID":       6038,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Giant Clam Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Gingerbread Cookie": {
        "ID":       17197,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Seasonal",
        "RecipeID": 17200,
        "Reagents": {
            "Small Egg": 1,
            "Holiday Spices": 1
        },
        "AmountCrafted": 1
    },
    "Goblin Deviled Clams": {
        "ID":       5527,
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Trainer",
        "Reagents": {
            "Tangy Clam Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Goldthorn Tea": {
        "ID":       10841,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Goldthorn": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 4
    },
    "Gooey Spider Cake": {
        "ID":       3666,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Gooey Spider Leg": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Goretusk Liver Pie": {
        "ID":       724,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Goretusk Liver": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Grilled Squid": {
        "ID":       13928,
        "Learn":    240,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Winter Squid": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Heavy Crocolisk Stew": {
        "ID":       20074,
        "Learn":    150,
        "Yellow":   160,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "Reagents": {
            "Tender Crocolisk Meat": 2,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Heavy Kodo Stew": {
        "ID":       12215,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Vendor",
        "Reagents": {
            "Heavy Kodo Meat": 2,
            "Soothing Spices": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 2
    },
    "Herb Baked Egg": {
        "ID":       6888,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Small Egg": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Hot Lion Chops": {
        "ID":       3727,
        "Learn":    125,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Vendor",
        "Reagents": {
            "Lion Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Hot Smoked Bass": {
        "ID":       13929,
        "Learn":    240,
        "Yellow":   280,
        "Green":    300,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Summer Bass": 1,
            "Hot Spices": 2
        },
        "AmountCrafted": 1
    },
    "Hot Wolf Ribs": {
        "ID":       13851,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Red Wolf Meat": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Jungle Stew": {
        "ID":       12212,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Tiger Meat": 1,
            "Refreshing Spring Water": 1,
            "Shiny Red Apple": 2
        },
        "AmountCrafted": 2
    },
    "Kaldorei Spider Kabob": {
        "ID":       5472,
        "Learn":    10,
        "Yellow":   50,
        "Green":    70,
        "Grey":     90,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "Reagents": {
            "Small Spider Leg": 1
        },
        "AmountCrafted": 1
    },
    "Lean Venison": {
        "ID":       5480,
        "Learn":    110,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Vendor",
        "Reagents": {
            "Stag Meat": 1,
            "Mild Spices": 4
        },
        "AmountCrafted": 2
    },
    "Lean Wolf Steak": {
        "ID":       12209,
        "Learn":    125,
        "Yellow":   165,
        "Green":    185,
        "Grey":     205,
        "Source":   "Vendor",
        "Reagents": {
            "Lean Wolf Flank": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Lobster Stew": {
        "ID":       13933,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "Reagents": {
            "Darkclaw Lobster": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1
    },
    "Loch Frenzy Delight": {
        "ID":       6316,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Raw Loch Frenzy": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Longjaw Mud Snapper": {
        "ID":       4592,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Longjaw Mud Snapper": 1
        },
        "AmountCrafted": 1
    },
    "Mightfish Steak": {
        "ID":       13934,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Vendor",
        "Reagents": {
            "Large Raw Mightfish": 1,
            "Hot Spices": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Mithril Head Trout": {
        "ID":       8364,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Mithril Head Trout": 1
        },
        "AmountCrafted": 1
    },
    "Monster Omelet": {
        "ID":       12218,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Giant Egg": 1,
            "Soothing Spices": 2
        },
        "AmountCrafted": 1
    },
    "Murloc Fin Soup": {
        "ID":       3663,
        "Learn":    90,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Murloc Fin": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Mystery Stew": {
        "ID":       12214,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Mystery Meat": 1,
            "Skin of Dwarven Stout": 1
        },
        "AmountCrafted": 1
    },
    "Nightfin Soup": {
        "ID":       13931,
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     30,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Nightfin Snapper": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1
    },
    "Poached Sunscale Salmon": {
        "ID":       13932,
        "Learn":    250,
        "Yellow":   290,
        "Green":    310,
        "Grey":     330,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Sunscale Salmon": 1
        },
        "AmountCrafted": 1
    },
    "Rainbow Fin Albacore": {
        "ID":       5095,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Rainbow Fin Albacore": 1
        },
        "AmountCrafted": 1
    },
    "Redridge Goulash": {
        "ID":       1082,
        "Learn":    100,
        "Yellow":   135,
        "Green":    155,
        "Grey":     175,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Crisp Spider Meat": 1,
            "Tough Condor Meat": 1
        },
        "AmountCrafted": 1
    },
    "Roast Raptor": {
        "ID":       12210,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Raptor Flesh": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Roasted Boar Meat": {
        "ID":       2681,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Chunk of Boar Meat": 1
        },
        "AmountCrafted": 1
    },
    "Roasted Kodo Meat": {
        "ID":       5474,
        "Learn":    35,
        "Yellow":   75,
        "Green":    95,
        "Grey":     115,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "Reagents": {
            "Kodo Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 2
    },
    "Rockscale Cod": {
        "ID":       4594,
        "Learn":    175,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Rockscale Cod": 1
        },
        "AmountCrafted": 1
    },
    "Runn Tum Tuber Surprise": {
        "ID":       18254,
        "Learn":    275,
        "Yellow":   315,
        "Green":    335,
        "Grey":     355,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Runn Tum Tuber": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Sagefish Delight": {
        "ID":       21217,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Greater Sagefish": 1,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Savory Deviate Delight": {
        "ID":       6657,
        "Learn":    85,
        "Yellow":   125,
        "Green":    145,
        "Grey":     165,
        "Source":   "Drop",
        "RecipeID": 6661,
        "Reagents": {
            "Deviate Fish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Scorpid Surprise": {
        "ID":       5473,
        "Learn":    20,
        "Yellow":   60,
        "Green":    80,
        "Grey":     100,
        "Source":   "Vendor",
        "Faction":  "Horde",
        "Reagents": {
            "Scorpid Stinger": 1
        },
        "AmountCrafted": 1
    },
    "Seasoned Wolf Kabob": {
        "ID":       1017,
        "Learn":    100,
        "Yellow":   140,
        "Green":    160,
        "Grey":     180,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Lean Wolf Flank": 2,
            "Stormwind Seasoning Herbs": 1
        },
        "AmountCrafted": 3
    },
    "Slitherskin Mackerel": {
        "ID":       787,
        "Learn":    1,
        "Yellow":   45,
        "Green":    65,
        "Grey":     85,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Slitherskin Mackerel": 1
        },
        "AmountCrafted": 1
    },
    "Smoked Bear Meat": {
        "ID":       6890,
        "Learn":    40,
        "Yellow":   80,
        "Green":    100,
        "Grey":     120,
        "Source":   "Vendor",
        "Reagents": {
            "Bear Meat": 1
        },
        "AmountCrafted": 1
    },
    "Smoked Desert Dumplings": {
        "ID":       20452,
        "Learn":    285,
        "Yellow":   325,
        "Green":    345,
        "Grey":     365,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Sandworm Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Smoked Sagefish": {
        "ID":       21072,
        "Learn":    80,
        "Yellow":   120,
        "Green":    140,
        "Grey":     160,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Sagefish": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Soothing Turtle Bisque": {
        "ID":       3729,
        "Learn":    175,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Turtle Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Spiced Chili Crab": {
        "ID":       12216,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Tender Crab Meat": 1,
            "Hot Spices": 2
        },
        "AmountCrafted": 1
    },
    "Spiced Wolf Meat": {
        "ID":       2680,
        "Learn":    10,
        "Yellow":   50,
        "Green":    70,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Stringy Wolf Meat": 1,
            "Mild Spices": 1
        },
        "AmountCrafted": 1
    },
    "Spider Sausage": {
        "ID":       17222,
        "Learn":    200,
        "Yellow":   240,
        "Green":    260,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
            "White Spider Meat": 2
        },
        "AmountCrafted": 1
    },
    "Spotted Yellowtail": {
        "ID":       6887,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Raw Spotted Yellowtail": 1
        },
        "AmountCrafted": 1
    },
    "Strider Stew": {
        "ID":       5477,
        "Learn":    50,
        "Yellow":   90,
        "Green":    110,
        "Grey":     130,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Strider Meat": 1,
            "Shiny Red Apple": 1
        },
        "AmountCrafted": 2
    },
    "Succulent Pork Ribs": {
        "ID":       2685,
        "Learn":    110,
        "Yellow":   130,
        "Green":    150,
        "Grey":     170,
        "Source":   "Drop",
        "RecipeID": 2700,
        "Reagents": {
            "Boar Ribs": 2,
            "Hot Spices": 1
        },
        "AmountCrafted": 1
    },
    "Tasty Lion Steak": {
        "ID":       3728,
        "Learn":    150,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Quest",
        "Faction":  "Alliance",
        "Reagents": {
            "Lion Meat": 2,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Tender Wolf Steak": {
        "ID":       18045,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Tender Wolf Meat": 1,
            "Soothing Spices": 1
        },
        "AmountCrafted": 1
    },
    "Thistle Tea": {
        "ID":       7676,
        "Learn":    60,
        "Yellow":   100,
        "Green":    120,
        "Grey":     140,
        "Source":   "Vendor",
        "Reagents": {
            "Swiftthistle": 1,
            "Refreshing Spring Water": 1
        },
        "AmountCrafted": 1
    },
    "Undermine Clam Chowder": {
        "ID":       16766,
        "Learn":    225,
        "Yellow":   265,
        "Green":    285,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Zesty Clam Meat": 2,
            "Hot Spices": 1,
            "Ice Cold Milk": 1
        },
        "AmountCrafted": 2
    },
    "Westfall Stew": {
        "ID":       733,
        "Learn":    75,
        "Yellow":   115,
        "Green":    135,
        "Grey":     155,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Stringy Vulture Meat": 1,
            "Murloc Eye": 1,
            "Goretusk Snout": 1
        },
        "AmountCrafted": 1
    }
}

import json
with open('cooking.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)