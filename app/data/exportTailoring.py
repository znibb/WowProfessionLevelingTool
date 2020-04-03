#!/usr/bin/env python3.7

recipes = {
	"Admirals Hat": {
        "ID":       10030,
        "Learn":    240,
        "Yellow":   255,
        "Green":    270,
        "Grey":     285,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Long Elegant Feather": 6,
            "Heavy Silken Thread": 2
        }
    },
    "Argent Boots": {
        "ID":       19056,
        "Learn":    290,
        "Yellow":   305,
        "Green":    320,
        "Grey":     335,
        "Source":   "Reputation",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Enchanted Leather": 4,
            "Golden Pearl": 2,
            "Guardian Stone": 2,
            "Ironweb Spider Silk": 2
        }
    },
    "Azure Shoulders": {
        "ID":       7060,
        "Learn":    190,
        "Yellow":   210,
        "Green":    225,
        "Grey":     240,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 6,
            "Naga Scale": 2,
            "Blue Dye": 2,
            "Silken Thread": 2
        }
    },
    "Azure Silk Belt": {
        "ID":       7052,
        "Learn":    175,
        "Yellow":   195,
        "Green":    210,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Elemental Water": 1,
            "Blue Dye": 2,
            "Fine Thread": 2,
            "Iron Buckle": 1
        }
    },
    "Azure Silk Cloak": {
        "ID":       7053,
        "Learn":    175,
        "Yellow":   195,
        "Green":    210,
        "Grey":     225,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Blue Dye": 2,
            "Fine Thread": 2
        }
    },
    "Azure Silk Gloves": {
        "ID":       4319,
        "Learn":    145,
        "Yellow":   165,
        "Green":    180,
        "Grey":     195,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Heavy Leather": 2,
            "Blue Dye": 2,
            "Fine Thread": 2
        }
    },
    "Azure Silk Hood": {
        "ID":       7048,
        "Learn":    145,
        "Yellow":   155,
        "Green":    160,
        "Grey":     165,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 2,
            "Blue Dye": 2,
            "Fine Thread": 1
        }
    },
    "Azure Silk Pants": {
        "ID":       7046,
        "Learn":    140,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Blue Dye": 2,
            "Fine Thread": 3
        }
    },
    "Azure Silk Vest": {
        "ID":       4324,
        "Learn":    150,
        "Yellow":   170,
        "Green":    185,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Blue Dye": 4
        }
    },
    "Barbaric Linen Vest": {
        "ID":       2578,
        "Learn":    70,
        "Yellow":   95,
        "Green":    112,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 4,
            "Light Leather": 1,
            "Fine Thread": 1
        }
    },
    "Black Mageweave Boots": {
        "ID":       10026,
        "Learn":    230,
        "Yellow":   245,
        "Green":    260,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Heavy Silken Thread": 2,
            "Thick Leather": 2
        }
    },
    "Black Mageweave Gloves": {
        "ID":       10003,
        "Learn":    215,
        "Yellow":   230,
        "Green":    245,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Black Mageweave Headband": {
        "ID":       10024,
        "Learn":    230,
        "Yellow":   245,
        "Green":    260,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Heavy Silken Thread": 2
        }
    },
    "Black Mageweave Leggings": {
        "ID":       9999,
        "Learn":    205,
        "Yellow":   220,
        "Green":    235,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Silken Thread": 3
        }
    },
    "Black Mageweave Robe": {
        "ID":       10001,
        "Learn":    210,
        "Yellow":   225,
        "Green":    240,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Heavy Silken Thread": 1
        }
    },
    "Black Mageweave Shoulders": {
        "ID":       10027,
        "Learn":    230,
        "Yellow":   245,
        "Green":    260,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Heavy Silken Thread": 2
        }
    },
    "Black Mageweave Vest": {
        "ID":       9998,
        "Learn":    205,
        "Yellow":   220,
        "Green":    235,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Silken Thread": 3
        }
    },
    "Black Silk Pack": {
        "ID":       5765,
        "Learn":    185,
        "Yellow":   205,
        "Green":    220,
        "Grey":     235,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Black Dye": 1,
            "Fine Thread": 4
        }
    },
    "Black Swashbucklers Shirt": {
        "ID":       4336,
        "Learn":    200,
        "Yellow":   210,
        "Green":    215,
        "Grey":     220,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Black Dye": 1,
            "Silken Thread": 1
        }
    },
    "Blue Linen Robe": {
        "ID":       6242,
        "Learn":    70,
        "Yellow":   95,
        "Green":    112,
        "Grey":     130,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Linen Cloth": 4,
            "Coarse Thread": 2,
            "Blue Dye": 2
        }
    },
    "Blue Linen Shirt": {
        "ID":       2577,
        "Learn":    40,
        "Yellow":   65,
        "Green":    82,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 1,
            "Blue Dye": 1
        }
    },
    "Blue Linen Vest": {
        "ID":       6240,
        "Learn":    55,
        "Yellow":   80,
        "Green":    97,
        "Grey":     115,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 1,
            "Blue Dye": 1
        }
    },
    "Blue Overalls": {
        "ID":       6263,
        "Learn":    100,
        "Yellow":   125,
        "Green":    142,
        "Grey":     160,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Fine Thread": 2,
            "Blue Dye": 2
        }
    },
    "Bolt of Linen Cloth": {
        "ID":       2996,
        "Learn":    1,
        "Yellow":   25,
        "Green":    37,
        "Grey":     50,
        "Source":   "Trainer",
        "Reagents": {
            "Linen Cloth": 2
        }
    },
    "Bolt of Mageweave": {
        "ID":       4339,
        "Learn":    175,
        "Yellow":   180,
        "Green":    182,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
            "Mageweave Cloth": 5
        }
    },
    "Bolt of Runecloth": {
        "ID":       14048,
        "Learn":    250,
        "Yellow":   255,
        "Green":    257,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Runecloth": 5
        }
    },
    "Bolt of Silk Cloth": {
        "ID":       4305,
        "Learn":    125,
        "Yellow":   135,
        "Green":    140,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
            "Silk Cloth": 4
        }
    },
    "Bolt of Woolen Cloth": {
        "ID":       2997,
        "Learn":    75,
        "Yellow":   90,
        "Green":    97,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
            "Wool Cloth": 3
        }
    },
    "Boots of the Enchanter": {
        "ID":       4325,
        "Learn":    175,
        "Yellow":   195,
        "Green":    210,
        "Grey":     225,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Silken Thread": 1,
            "Thick Spiders Silk": 2
        }
    },
    "Bright Yellow Shirt": {
        "ID":       4332,
        "Learn":    135,
        "Yellow":   145,
        "Green":    150,
        "Grey":     155,
        "Source":   "Vendor",
        "Faction":  "Alliance",
        "Reagents": {
            "Bolt of Silk Cloth": 1,
            "Yellow Dye": 1,
            "Fine Thread": 1
        }
    },
    "Brightcloth Cloak": {
        "ID":       14103,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Gold Bar": 2,
            "Rune Thread": 1
        }
    },
    "Brightcloth Gloves": {
        "ID":       14101,
        "Learn":    270,
        "Yellow":   285,
        "Green":    300,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Gold Bar": 2,
            "Rune Thread": 1
        }
    },
    "Brightcloth Pants": {
        "ID":       14104,
        "Learn":    290,
        "Yellow":   305,
        "Green":    320,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Gold Bar": 4,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Brightcloth Robe": {
        "ID":       14100,
        "Learn":    270,
        "Yellow":   285,
        "Green":    300,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Gold Bar": 2,
            "Rune Thread": 1
        }
    },
    "Brown Linen Pants": {
        "ID":       4343,
        "Learn":    30,
        "Yellow":   55,
        "Green":    72,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 1
        }
    },
    "Brown Linen Robe": {
        "ID":       6238,
        "Learn":    30,
        "Yellow":   55,
        "Green":    72,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 1
        }
    },
    "Brown Linen Shirt": {
        "ID":       4344,
        "Learn":    1,
        "Yellow":   35,
        "Green":    47,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 1,
            "Coarse Thread": 1
        }
    },
    "Brown Linen Vest": {
        "ID":       2568,
        "Learn":    10,
        "Yellow":   45,
        "Green":    57,
        "Grey":     70,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 1,
            "Coarse Thread": 1
        }
    },
    "Cenarion Herb Bag": {
        "ID":       22251,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Reputation",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Purple Lotus": 10,
            "Morrowgrain": 8,
            "Rune Thread": 2
        }
    },
    "Cintercloth Boots": {
        "ID":       10044,
        "Learn":    245,
        "Yellow":   260,
        "Green":    275,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 5,
            "Heart of Fire": 1,
            "Heavy Silken Thread": 3,
            "Thick Leather": 2
        }
    },
    "Cindercloth Cloak": {
        "ID":       14044,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Essence of Fire": 1,
            "Rune Thread": 1
        }
    },
    "Cindercloth Gloves": {
        "ID":       14043,
        "Learn":    270,
        "Yellow":   285,
        "Green":    300,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Heart of Fire": 3,
            "Rune Thread": 1
        }
    },
    "Cindercloth Pants": {
        "ID":       14045,
        "Learn":    280,
        "Yellow":   295,
        "Green":    310,
        "Grey":     325,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Essence of Fire": 1,
            "Rune Thread": 1
        }
    },
    "Cindercloth Robe": {
        "ID":       10042,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 5,
            "Heart of Fire": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Cindercloth Vest": {
        "ID":       14042,
        "Learn":    260,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Heart of Fire": 3,
            "Rune Thread": 1
        }
    },
    "Cloak of Fire": {
        "ID":       14134,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Essence of Fire": 4,
            "Heart of Fire": 4,
            "Elemental Fire": 4,
            "Rune Thread": 1
        }
    },
    "Colorful Kilt": {
        "ID":       10048,
        "Learn":    120,
        "Yellow":   145,
        "Green":    162,
        "Grey":     180,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 5,
            "Red Dye": 3,
            "Fine Thread": 1
        }
    },
    "Crimson Silk Belt": {
        "ID":       7055,
        "Learn":    175,
        "Yellow":   195,
        "Green":    210,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Iron Buckle": 1,
            "Red Dye": 2,
            "Silken Thread": 1
        }
    },
    "Crimson Silk Cloak": {
        "ID":       7056,
        "Learn":    180,
        "Yellow":   200,
        "Green":    215,
        "Grey":     230,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Red Dye": 2,
            "Fire Oil": 2,
            "Silken Thread": 1
        }
    },
    "Crimson Silk Gloves": {
        "ID":       7064,
        "Learn":    210,
        "Yellow":   225,
        "Green":    240,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 6,
            "Elemental Fire": 2,
            "Fire Oil": 2,
            "Thick Leather": 2,
            "Red Dye": 4,
            "Silken Thread": 2
        }
    },
    "Crimson Silk Pantaloons": {
        "ID":       7062,
        "Learn":    195,
        "Yellow":   215,
        "Green":    225,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Red Dye": 2,
            "Silken Thread": 2
        }
    },
    "Crimson Silk Robe": {
        "ID":       7063,
        "Learn":    205,
        "Yellow":   220,
        "Green":    235,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 8,
            "Elemental Fire": 4,
            "Mana Potion": 2,
            "Red Dye": 4,
            "Silken Thread": 1
        }
    },
    "Crimson Silk Shoulders": {
        "ID":       7059,
        "Learn":    190,
        "Yellow":   210,
        "Green":    225,
        "Grey":     240,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Fire Oil": 2,
            "Red Dye": 2,
            "Silken Thread": 2
        }
    },
    "Crimson Silk Vest": {
        "ID":       7058,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Red Dye": 2,
            "Fine Thread": 2
        }
    },
    "Dark Silk Shirt": {
        "ID":       4333,
        "Learn":    155,
        "Yellow":   165,
        "Green":    170,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 2,
            "Gray Dye": 2,
            "Fine Thread": 1
        }
    },
    "Double-stitched Woolen Shoulders": {
        "ID":       4314,
        "Learn":    110,
        "Yellow":   135,
        "Green":    152,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 3,
            "Fine Thread": 2
        }
    },
    "Dreamweave Circlet": {
        "ID":       10041,
        "Learn":    250,
        "Yellow":   265,
        "Green":    280,
        "Grey":     295,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 8,
            "Wildvine": 4,
            "Heart of the Wild": 2,
            "Heavy Silken Thread": 3,
            "Truesilver Bar": 1,
            "Jade": 1
        }
    },
    "Dreamweave Gloves": {
        "ID":       10019,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Wildvine": 4,
            "Heart of the Wild": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Dreamweave Vest": {
        "ID":       10021,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 6,
            "Wildvine": 6,
            "Heart of the Wild": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Earthen Silk Belt": {
        "ID":       7061,
        "Learn":    195,
        "Yellow":   215,
        "Green":    230,
        "Grey":     245,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Elemental Earth": 4,
            "Heavy Leather": 4,
            "Iron Buckle": 1,
            "Silken Thread": 2
        }
    },
    "Earthen Vest": {
        "ID":       7051,
        "Learn":    170,
        "Yellow":   190,
        "Green":    205,
        "Grey":     220,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Elemental Earth": 1,
            "Fine Thread": 2
        }
    },
    "Enchanted Mageweave Pouch": {
        "ID":       22246,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Vision Dust": 4,
            "Heavy Silken Thread": 2
        }
    },
    "Enchanted Runecloth Bag": {
        "ID":       22248,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Greater Eternal Essence": 2,
            "Rune Thread": 2
        }
    },
    "Enchanters Cowl": {
        "ID":       4322,
        "Learn":    165,
        "Yellow":   185,
        "Green":    200,
        "Grey":     215,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Fine Thread": 2,
            "Thick Spiders Silk": 2
        }
    },
    "Felcloth Bag": {
        "ID":       21341,
        "Learn":    285,
        "Yellow":   300,
        "Green":    315,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
            "Felcloth": 12,
            "Enchanted Leather": 6,
            "Dark Rune": 2,
            "Ironweb Spider Silk": 4
        }
    },
    "Felcloth Boots": {
        "ID":       14108,
        "Learn":    285,
        "Yellow":   300,
        "Green":    315,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Felcloth": 4,
            "Rugged Leather": 4,
            "Rune Thread": 1
        }
    },
    "Felcloth Hood": {
        "ID":       14111,
        "Learn":    290,
        "Yellow":   305,
        "Green":    320,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Felcloth": 4,
            "Rune Thread": 1
        }
    },
    "Felcloth Pants": {
        "ID":       14107,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Felcloth": 4,
            "Rune Thread": 1
        }
    },
    "Festival Dress": {
        "ID":       21154,
        "Learn":    250,
        "Yellow":   265,
        "Green":    280,
        "Grey":     295,
        "Source":   "Seasonal",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Firebloom": 2,
            "Red Dye": 2,
            "Rune Thread": 1
        }
    },
    "Festival Suit": {
        "ID":       21542,
        "Learn":    250,
        "Yellow":   265,
        "Green":    280,
        "Grey":     295,
        "Source":   "Seasonal",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Firebloom": 2,
            "Red Dye": 2,
            "Rune Thread": 1
        }
    },
    "Formal White Shirt": {
        "ID":       4334,
        "Learn":    170,
        "Yellow":   180,
        "Green":    185,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Bleach": 2,
            "Fine Thread": 1
        }
    },
    "Frostweave Gloves": {
        "ID":       13870,
        "Learn":    265,
        "Yellow":   280,
        "Green":    295,
        "Grey":     310,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 3,
            "Essence of Water": 1,
            "Rune Thread": 1
        }
    },
    "Frostweave Pants": {
        "ID":       13871,
        "Learn":    280,
        "Yellow":   295,
        "Green":    310,
        "Grey":     325,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Essence of Water": 1,
            "Rune Thread": 1
        }
    },
    "Frostweave Robe": {
        "ID":       13868,
        "Learn":    255,
        "Yellow":   270,
        "Green":    285,
        "Grey":     300,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Globe of Water": 2,
            "Rune Thread": 1
        }
    },
    "Frostweave Tunic": {
        "ID":       13869,
        "Learn":    255,
        "Yellow":   270,
        "Green":    285,
        "Grey":     300,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Globe of Water": 2,
            "Rune Thread": 1
        }
    },
    "Ghostweave Belt": {
        "ID":       14143,
        "Learn":    265,
        "Yellow":   280,
        "Green":    295,
        "Grey":     310,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 3,
            "Ghost Dye": 2,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Ghostweave Gloves": {
        "ID":       14142,
        "Learn":    270,
        "Yellow":   285,
        "Green":    300,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Ghost Dye": 2,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Ghostweave Pants": {
        "ID":       14144,
        "Learn":    290,
        "Yellow":   305,
        "Green":    320,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Ghost Dye": 4,
            "Rune Thread": 1
        }
    },
    "Ghostweave Vest": {
        "ID":       14141,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Ghost Dye": 4,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Gloves of Meditation": {
        "ID":       4318,
        "Learn":    130,
        "Yellow":   150,
        "Green":    165,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Fine Thread": 3,
            "Elixir of Wisdom": 1
        }
    },
    "Gray Woolen Robe": {
        "ID":       2585,
        "Learn":    105,
        "Yellow":   130,
        "Green":    147,
        "Grey":     165,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Fine Thread": 3,
            "Gray Dye": 1
        }
    },
    "Gray Woolen Shirt": {
        "ID":       2587,
        "Learn":    100,
        "Yellow":   110,
        "Green":    120,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 2,
            "Fine Thread": 1,
            "Gray Dye": 1
        }
    },
    "Greater Adepts Robe": {
        "ID":       6264,
        "Learn":    115,
        "Yellow":   140,
        "Green":    157,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Woolen Cloth": 5,
            "Fine Thread": 3,
            "Red Dye": 3
        }
    },
    "Green Holiday Shirt": {
        "ID":       17723,
        "Learn":    190,
        "Yellow":   200,
        "Green":    205,
        "Grey":     210,
        "Source":   "Seasonal",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Green Dye": 4,
            "Silken Thread": 1
        }
    },
    "Green Linen Bracers": {
        "ID":       4308,
        "Learn":    60,
        "Yellow":   85,
        "Green":    102,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 2,
            "Green Dye": 1
        }
    },
    "Green Linen Shirt": {
        "ID":       2579,
        "Learn":    70,
        "Yellow":   95,
        "Green":    112,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Fine Thread": 1,
            "Green Dye": 1
        }
    },
    "Green Silk Armor": {
        "ID":       7065,
        "Learn":    165,
        "Yellow":   185,
        "Green":    200,
        "Grey":     215,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Green Dye": 2,
            "Silken Thread": 1
        }
    },
    "Green Silk Pack": {
        "ID":       5764,
        "Learn":    175,
        "Yellow":   195,
        "Green":    210,
        "Grey":     225,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Heavy Leather": 3,
            "Fine Thread": 3,
            "Green Dye": 1
        }
    },
    "Green Silken Shoulders": {
        "ID":       7057,
        "Learn":    180,
        "Yellow":   200,
        "Green":    215,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 5,
            "Silken Thread": 2
        }
    },
    "Green Woolen Bag": {
        "ID":       4241,
        "Learn":    95,
        "Yellow":   120,
        "Green":    137,
        "Grey":     155,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Green Dye": 1,
            "Fine Thread": 1
        }
    },
    "Green Woolen Vest": {
        "ID":       2582,
        "Learn":    85,
        "Yellow":   110,
        "Green":    127,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 2,
            "Fine Thread": 2,
            "Green Dye": 1
        }
    },
    "Hands of Darkness": {
        "ID":       7047,
        "Learn":    145,
        "Yellow":   165,
        "Green":    180,
        "Grey":     195,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Heavy Leather": 2,
            "Shadow Protection Potion": 2,
            "Fine Thread": 2
        }
    },
    "Handstitched Linen Britches": {
        "ID":       4309,
        "Learn":    70,
        "Yellow":   95,
        "Green":    112,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 4,
            "Fine Thread": 2
        }
    },
    "Heavy Linen Gloves": {
        "ID":       4307,
        "Learn":    35,
        "Yellow":   60,
        "Green":    77,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 1
        }
    },
    "Heavy Woolen Cloak": {
        "ID":       4311,
        "Learn":    100,
        "Yellow":   125,
        "Green":    142,
        "Grey":     160,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 3,
            "Fine Thread": 2,
            "Small Lustrous Pearl": 2
        }
    },
    "Heavy Woolen Gloves": {
        "ID":       4310,
        "Learn":    85,
        "Yellow":   110,
        "Green":    127,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 3,
            "Fine Thread": 1
        }
    },
    "Heavy Woolen Pants": {
        "ID":       4316,
        "Learn":    110,
        "Yellow":   135,
        "Green":    152,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 5,
            "Fine Thread": 4
        }
    },
    "Icy Cloak": {
        "ID":       4327,
        "Learn":    200,
        "Yellow":   220,
        "Green":    235,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Silken Thread": 2,
            "Frost Oil": 1,
            "Thick Spiders Silk": 2
        }
    },
    "Lavender Mageweave Shirt": {
        "ID":       10054,
        "Learn":    230,
        "Yellow":   235,
        "Green":    240,
        "Grey":     245,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Purple Dye": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Lesser Wizards Robe": {
        "ID":       5766,
        "Learn":    135,
        "Yellow":   155,
        "Green":    170,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 2,
            "Fine Thread": 2,
            "Spiders Silk": 2
        }
    },
    "Linen Bag": {
        "ID":       4238,
        "Learn":    45,
        "Yellow":   70,
        "Green":    87,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 3
        }
    },
    "Linen Belt": {
        "ID":       7026,
        "Learn":    15,
        "Yellow":   50,
        "Green":    67,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 1,
            "Coarse Thread": 1
        }
    },
    "Linen Boots": {
        "ID":       2569,
        "Learn":    65,
        "Yellow":   90,
        "Green":    107,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 1,
            "Light Leather": 1
        }
    },
    "Linen Cloak": {
        "ID":       2570,
        "Learn":    1,
        "Yellow":   35,
        "Green":    47,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 1,
            "Coarse Thread": 1
        }
    },
    "Long Silken Cloak": {
        "ID":       4326,
        "Learn":    185,
        "Yellow":   205,
        "Green":    220,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Mana Potion": 1,
            "Silken Thread": 1
        }
    },
    "Mageweave Bag": {
        "ID":       10050,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Silken Thread": 2
        }
    },
    "Mooncloth": {
        "ID":       14342,
        "Learn":    250,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Felcloth": 2
        }
    },
    "Mooncloth Boots": {
        "ID":       15802,
        "Learn":    290,
        "Yellow":   295,
        "Green":    210,
        "Grey":     325,
        "Source":   "Quest",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Mooncloth": 4,
            "Black Pearl": 2,
            "Rune Thread": 1
        }
    },
    "Mooncloth Leggings": {
        "ID":       14137,
        "Learn":    290,
        "Yellow":   305,
        "Green":    320,
        "Grey":     335,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Mooncloth": 4,
            "Rune Thread": 1
        }
    },
    "Orange Mageweave Shirt": {
        "ID":       10056,
        "Learn":    215,
        "Yellow":   220,
        "Green":    225,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 1,
            "Orange Dye": 1,
            "Heavy Silken Thread": 1
        }
    },
    "Orange Martial Shirt": {
        "ID":       10052,
        "Learn":    220,
        "Yellow":   225,
        "Green":    230,
        "Grey":     235,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Orange Dye": 2,
            "Heavy Silken Thread": 1
        }
    },
    "Pearl-clasped Cloak": {
        "ID":       5542,
        "Learn":    90,
        "Yellow":   115,
        "Green":    132,
        "Grey":     150,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Woolen Cloth": 3,
            "Fine Thread": 2,
            "Small Lustrous Pearl": 1
        }
    },
    "Phoenix Gloves": {
        "ID":       4331,
        "Learn":    125,
        "Yellow":   150,
        "Green":    167,
        "Grey":     185,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Iridescent Pearl": 1,
            "Fine Thread": 4,
            "Bleach": 2
        }
    },
    "Phoenix Pants": {
        "ID":       4317,
        "Learn":    125,
        "Yellow":   150,
        "Green":    167,
        "Grey":     185,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 6,
            "Iridescent Pearl": 1,
            "Fine Thread": 3
        }
    },
    "Pink Mageweave Shirt": {
        "ID":       10055,
        "Learn":    235,
        "Yellow":   240,
        "Green":    245,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Pink Dye": 1,
            "Heavy Silken Thread": 1
        }
    },
    "Red Linen Bag": {
        "ID":       5762,
        "Learn":    70,
        "Yellow":   95,
        "Green":    112,
        "Grey":     130,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Linen Cloth": 4,
            "Fine Thread": 1,
            "Red Dye": 1
        }
    },
    "Red Linen Robe": {
        "ID":       2572,
        "Learn":    40,
        "Yellow":   65,
        "Green":    82,
        "Grey":     100,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 2,
            "Red Dye": 2
        }
    },
    "Red Linen Shirt": {
        "ID":       2575,
        "Learn":    40,
        "Yellow":   65,
        "Green":    82,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 1,
            "Red Dye": 1
        }
    },
    "Red Linen Vest": {
        "ID":       6239,
        "Learn":    55,
        "Yellow":   80,
        "Green":    97,
        "Grey":     115,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Linen Cloth": 3,
            "Coarse Thread": 1,
            "Red Dye": 1
        }
    },
    "Red Mageweave Bag": {
        "ID":       10051,
        "Learn":    235,
        "Yellow":   250,
        "Green":    265,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Red Dye": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Red Mageweave Gloves": {
        "ID":       10018,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Red Dye": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Red Mageweave Headband": {
        "ID":       10033,
        "Learn":    240,
        "Yellow":   255,
        "Green":    270,
        "Grey":     285,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Red Dye": 2,
            "Heavy Silken Thread": 2
        }
    },
    "Red Mageweave Pants": {
        "ID":       10009,
        "Learn":    215,
        "Yellow":   230,
        "Green":    245,
        "Grey":     260,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Red Dye": 2,
            "Heavy Silken Thread": 1
        }
    },
    "Red Mageweave Shoulders": {
        "ID":       10029,
        "Learn":    235,
        "Yellow":   250,
        "Green":    265,
        "Grey":     280,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Mageweave": 4,
            "Red Dye": 2,
            "Heavy Silken Thread": 3
        }
    },
    "Red Mageweave Vest": {
        "ID":       10007,
        "Learn":    215,
        "Yellow":   230,
        "Green":    245,
        "Grey":     260,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Red Dye": 2,
            "Heavy Silken Thread": 1
        }
    },
    "Red Swashbucklers Shirt": {
        "ID":       6796,
        "Learn":    175,
        "Yellow":   185,
        "Green":    190,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Red Dye": 2,
            "Silken Thread": 1
        }
    },
    "Red Woolen Bag": {
        "ID":       5763,
        "Learn":    115,
        "Yellow":   140,
        "Green":    157,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Red Dye": 1,
            "Fine Thread": 1
        }
    },
    "Red Woolen Boots": {
        "ID":       4313,
        "Learn":    95,
        "Yellow":   120,
        "Green":    137,
        "Grey":     155,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 4,
            "Light Leather": 2,
            "Fine Thread": 1,
            "Red Dye": 2
        }
    },
    "Reinforced Linen Cape": {
        "ID":       2580,
        "Learn":    60,
        "Yellow":   85,
        "Green":    102,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 3
        }
    },
    "Reinforced Woolen Shoulders": {
        "ID":       4315,
        "Learn":    120,
        "Yellow":   145,
        "Green":    162,
        "Grey":     180,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Woolen Cloth": 6,
            "Medium Leather": 2,
            "Fine Thread": 2
        }
    },
    "Rich Purple Silk Shirt": {
        "ID":       4335,
        "Learn":    185,
        "Yellow":   195,
        "Green":    200,
        "Grey":     205,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Purple Dye": 1,
            "Silken Thread": 1
        }
    },
    "Robe of Power": {
        "ID":       7054,
        "Learn":    190,
        "Yellow":   210,
        "Green":    225,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Elemental Earth": 2,
            "Elemental Water": 2,
            "Elemental Fire": 2,
            "Elemental Air": 2,
            "Silken Thread": 2
        }
    },
    "Robe of Winter Night": {
        "ID":       14136,
        "Learn":    285,
        "Yellow":   300,
        "Green":    315,
        "Grey":     300,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 10,
            "Felcloth": 12,
            "Essence of Undeath": 4,
            "Essence of Water": 4,
            "Rune Thread": 1
        }
    },
    "Robes of Arcana": {
        "ID":       5770,
        "Learn":    150,
        "Yellow":   170,
        "Green":    185,
        "Grey":     200,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Fine Thread": 2,
            "Spiders Silk": 2
        }
    },
    "Runecloth Bag": {
        "ID":       14046,
        "Learn":    260,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Rugged Leather": 2,
            "Rune Thread": 1
        }
    },
    "Runecloth Belt": {
        "ID":       13856,
        "Learn":    255,
        "Yellow":   270,
        "Green":    285,
        "Grey":     300,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Runecloth": 3,
            "Rune Thread": 1
        }
    },
    "Runecloth Boots": {
        "ID":       13864,
        "Learn":    280,
        "Yellow":   295,
        "Green":    310,
        "Grey":     325,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Ironweb Spider Silk": 2,
            "Rugged Leather": 4,
            "Rune Thread": 1
        }
    },
    "Runecloth Cloak": {
        "ID":       13860,
        "Learn":    265,
        "Yellow":   280,
        "Green":    295,
        "Grey":     310,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Runecloth Gloves": {
        "ID":       13863,
        "Learn":    275,
        "Yellow":   290,
        "Green":    305,
        "Grey":     320,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Rugged Leather": 4,
            "Rune Thread": 1
        }
    },
    "Runecloth Headband": {
        "ID":       13866,
        "Learn":    295,
        "Yellow":   310,
        "Green":    325,
        "Grey":     340,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 4,
            "Ironweb Spider Silk": 2,
            "Rune Thread": 1
        }
    },
    "Runecloth Pants": {
        "ID":       13865,
        "Learn":    285,
        "Yellow":   300,
        "Green":    315,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Ironweb Spider Silk": 2,
            "Rune Thread": 1
        }
    },
    "Runecloth Robe": {
        "ID":       13858,
        "Learn":    260,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Runecloth Tunic": {
        "ID":       13857,
        "Learn":    260,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Runecloth": 5,
            "Ironweb Spider Silk": 1,
            "Rune Thread": 1
        }
    },
    "Shadow Hood": {
        "ID":       4323,
        "Learn":    170,
        "Yellow":   190,
        "Green":    205,
        "Grey":     220,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Silken Thread": 1,
            "Shadow Oil": 1
        }
    },
    "Shadoweave Boots": {
        "ID":       10031,
        "Learn":    240,
        "Yellow":   255,
        "Green":    270,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 6,
            "Shadow Silk": 6,
            "Heavy Silken Thread": 3,
            "Thick Leather": 2
        }
    },
    "Shadoweave Gloves": {
        "ID":       10023,
        "Learn":    225,
        "Yellow":   240,
        "Green":    255,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 5,
            "Shadow Silk": 5,
            "Heavy Silken Thread": 2
        }
    },
    "Shadoweave Mask": {
        "ID":       10025,
        "Learn":    245,
        "Yellow":   260,
        "Green":    275,
        "Grey":     290,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
            "Bolt of Mageweave": 2,
            "Shadow Silk": 8,
            "Heavy Silken Thread": 2
        }
    },
    "Shadoweave Pants": {
        "ID":       10002,
        "Learn":    210,
        "Yellow":   225,
        "Green":    240,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Shadow Silk": 2,
            "Heavy Silken Thread": 1
        }
    },
    "Shadoweave Robe": {
        "ID":       10004,
        "Learn":    215,
        "Yellow":   230,
        "Green":    245,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Shadow Silk": 2,
            "Heavy Silken Thread": 1
        }
    },
    "Shadoweave Shoulders": {
        "ID":       10028,
        "Learn":    235,
        "Yellow":   250,
        "Green":    265,
        "Grey":     280,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 5,
            "Shadow Silk": 4,
            "Heavy Silken Thread": 2
        }
    },
    "Silk Headband": {
        "ID":       7050,
        "Learn":    160,
        "Yellow":   170,
        "Green":    175,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Fine Thread": 2
        }
    },
    "Simple Black Dress": {
        "ID":       10053,
        "Learn":    235,
        "Yellow":   240,
        "Green":    245,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Mageweave": 3,
            "Black Dye": 1,
            "Heavy Silken Thread": 1,
            "Bleach": 1
        }
    }
    ,
    "Simple Dress": {
        "ID":       6786,
        "Learn":    40,
        "Yellow":   65,
        "Green":    82,
        "Grey":     100,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Coarse Thread": 1,
            "Blue Dye": 1,
            "Bleach": 1
        }
    },
    "Simple Kilt": {
        "ID":       10047,
        "Learn":    75,
        "Yellow":   100,
        "Green":    117,
        "Grey":     135,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 4,
            "Fine Thread": 1
        }
    },
    "Simple Linen Boots": {
        "ID":       10046,
        "Learn":    20,
        "Yellow":   50,
        "Green":    67,
        "Grey":     85,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 2,
            "Light Leather": 1,
            "Coarse Thread": 1
        }
    },
    "Simple Linen Pants": {
        "ID":       10045,
        "Learn":    1,
        "Yellow":   35,
        "Green":    47,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 1,
            "Coarse Thread": 1
        }
    },
    "Small Silk Pack": {
        "ID":       4245,
        "Learn":    150,
        "Yellow":   170,
        "Green":    185,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Heavy Leather": 2,
            "Fine Thread": 3
        }
    },
    "Soft-soled Linen Boots": {
        "ID":       4312,
        "Learn":    80,
        "Yellow":   105,
        "Green":    122,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
            "Bolt of Linen Cloth": 5,
            "Light Leather": 2,
            "Fine Thread": 1
        }
    },
    "Soul Pouch": {
        "ID":       21340,
        "Learn":    260,
        "Yellow":   275,
        "Green":    290,
        "Grey":     305,
        "Source":   "Vendor",
        "Reagents": {
            "Bolt of Runecloth": 6,
            "Rugged Leather": 4,
            "Ichor of Undeath": 2,
            "Rune Thread": 1
        }
    },
    "Spider Belt": {
        "ID":       4328,
        "Learn":    180,
        "Yellow":   200,
        "Green":    215,
        "Grey":     230,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 4,
            "Thick Spiders Silk": 2,
            "Iron Buckle": 1
        }
    },
    "Spider Silk Slippers": {
        "ID":       4321,
        "Learn":    140,
        "Yellow":   160,
        "Green":    175,
        "Grey":     190,
        "Source":   "Drop",
        "Reagents": {
            "Bolt of Silk Cloth": 3,
            "Spiders Silk": 1,
            "Fine Thread": 2
        }
    }
}

import json
with open('tailoring.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)