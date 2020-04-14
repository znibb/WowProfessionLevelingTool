#!/usr/bin/env python3.7

recipes = {
    "Accurate Scope": {
        "ID":       3979,
        "Learn":    180,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 1,
			"Jade": 1,
			"Citrine": 1
        }
    },
	"Advanced Target Dummy": {
        "ID":       3965,
        "Learn":    185,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Strut": 1,
			"Bronze Framework": 1,
			"Gyrochronatom": 1,
			"Heavy Leather": 4
        }
    },
	"Alarm-O-Bot": {
        "ID":       23096,
        "Learn":    265,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Drop",
		"School": "Gnomish",
        "Reagents": {
			"Thorium Bar": 4,
			"Thorium Widget": 2,
			"Rugged Leather": 4,
			"Star Ruby": 1,
			"Fused Wiring": 1
        }
    },
	"Aquadynamic Fish Attractor": {
        "ID":       9271,
        "Learn":    150,
        "Yellow":   150,
        "Green":    160,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Nightcrawlers": 1,
			"Coarse Blasting Powder": 1
        }
    },
	"Arclight Spanner": {
        "ID":       7430,
        "Learn":    50,
        "Yellow":   70,
        "Green":    80,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 6
        }
    },
	"Big Bronze Bomb": {
        "ID":       3950,
        "Learn":    140,
        "Yellow":   140,
        "Green":    165,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 2,
			"Bronze Bar": 3,
			"Silver Contact": 1
        }
    },
	"Big Iron Bomb": {
        "ID":       3967,
        "Learn":    190,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 3,
			"Heavy Blasting Powder": 3,
			"Silver Contact": 1
        }
    },
	"Blue Firework": {
        "ID":       23067,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Blue Rocker Cluster": {
        "ID":       26423,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Bright-Eye Googles": {
        "ID":       12587,
        "Learn":    175,
        "Yellow":   195,
        "Green":    205,
        "Grey":     215,
        "Source":   "Drop",
        "Reagents": {
			"Heavy Leather": 6,
			"Citrine": 2
        }
    },
	"Bronze Framework": {
        "ID":       3953,
        "Learn":    145,
        "Yellow":   145,
        "Green":    170,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Medium Leather": 1,
			"Wool Cloth": 1
        }
    },
	"Bronze Tube": {
        "ID":       3938,
        "Learn":    105,
        "Yellow":   105,
        "Green":    130,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Weak Flux": 1
        }
    },
	"Catseye Ultra Googles": {
        "ID":       12607,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "Reagents": {
			"Thick Leather": 4,
			"Aquamarine": 2,
			"Catseye Elixir": 1
        }
    },
	"Coarse Blasting Powder": {
        "ID":       3929,
        "Learn":    75,
        "Yellow":   85,
        "Green":    90,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Stone": 1
        }
    },
	"Coarse Dynamite": {
        "ID":       3931,
        "Learn":    75,
        "Yellow":   90,
        "Green":    97,
        "Grey":     105,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 3,
			"Linen Cloth": 1
        }
    },
	"Compact Harvest Reaper Kit": {
        "ID":       3963,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Strut": 2,
			"Bronze Framework": 1,
			"Gyrochronatom": 2,
			"Heavy Leather": 4
        }
    },
	"Copper Modulator": {
        "ID":       3926,
        "Learn":    65,
        "Yellow":   95,
        "Green":    110,
        "Grey":     125,
        "Source":   "Trainer",
        "Reagents": {
			"Handful of Copper Bolts": 2,
			"Copper Bar": 1,
			"Linen Cloth": 2
        }
    },
	"Copper Tube": {
        "ID":       3924,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 2,
			"Weak Flux": 1
        }
    },
	"Crafted Heavy Shot": {
        "ID":       3930,
        "Learn":    75,
        "Yellow":   85,
        "Green":    90,
        "Grey":     95,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Copper Bar": 1
        }
    },
	"Crafted Light Shot": {
        "ID":       3920,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Blasting Powder": 1,
			"Copper Bar": 1
        }
    },
	"Crafted Solid Shot": {
        "ID":       3947,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Bronze Bar": 1
        }
    },
	"Craftmans Monocle": {
        "ID":       3966,
        "Learn":    185,
        "Yellow":   205,
        "Green":    215,
        "Grey":     225,
        "Source":   "Drop",
        "Reagents": {
			"Heavy Leather": 6,
			"Citrine": 2
        }
    },
	"Crude Scope": {
        "ID":       3977,
        "Learn":    60,
        "Yellow":   90,
        "Green":    105,
        "Grey":     120,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 1,
			"Malachite": 1,
			"Handful of Copper Bolts": 1
        }
    },
	"Dark Iron Bomb": {
        "ID":       19799,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "Reagents": {
			"Thorium Widget": 2,
			"Dark Iron Bar": 1,
			"Dense Blasting Powder": 3,
			"Runecloth": 3
        }
    },
	"Dark Iron Rifle": {
        "ID":       19796,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Drop",
        "Reagents": {
			"Thorium Tube": 2,
			"Dark Iron Bar": 6,
			"Deadly Scope": 2,
			"Blue Sapphire": 2,
			"Large Opal": 2,
			"Rugged Leather": 4
        }
    },
	"Deadly Blunderbuss": {
        "ID":       3936,
        "Learn":    105,
        "Yellow":   130,
        "Green":    142,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 2,
			"Handful of Copper Bolts": 4,
			"Wooden Stock": 1,
			"Medium Leather": 2
        }
    },
	"Deadly Scope": {
        "ID":       12597,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Tube": 1,
			"Aquamarine": 2,
			"Thick Leather": 2
        }
    },
	"Deepdive Helmet": {
        "ID":       12617,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Bar": 8,
			"Mithril Casing": 1,
			"Truesilver Bar": 1,
			"Tigerseye": 4,
			"Malachite": 4
        }
    },
	"Delicate Arcanite Converter": {
        "ID":       19815,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Vendor",
        "Reagents": {
			"Arcanite Bar": 1,
			"Ironweb Spider Silk": 1
        }
    },
	"Dense Blasting Powder": {
        "ID":       19788,
        "Learn":    250,
        "Yellow":   250,
        "Green":    255,
        "Grey":     260,
        "Source":   "Trainer",
        "Reagents": {
			"Dense Stone": 2
        }
    },
	"Dense Dynamite": {
        "ID":       23070,
        "Learn":    250,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Dense Blasting Powder": 2,
			"Runecloth": 3
        }
    },
	"Dimensoinal Ripper - Everlook": {
        "ID":       23486,
        "Learn":    260,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 10,
			"Truesilver Transformer": 1,
			"Heart of Fire": 4,
			"Star Ruby": 2,
			"The Big One": 1
        }
    },
	"Discombobulator Ray": {
        "ID":       3959,
        "Learn":    160,
        "Yellow":   180,
        "Green":    190,
        "Grey":     200,
        "Source":   "Drop",
        "Reagents": {
			"Whirring Bronze Gizmo": 3,
			"Silk Cloth": 2,
			"Jade": 1,
			"Bronze Tube": 1
        }
    },
	"Explosive Sheep": {
        "ID":       3955,
        "Learn":    150,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Framework": 1,
			"Whirring Bronze Gizmo": 1,
			"Heavy Blasting Powder": 2,
			"Wool Cloth": 2
        }
    },
	"EZ-Thro Dynamite": {
        "ID":       8339,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Drop",
        "Reagents": {
			"Coarse Blasting Powder": 4,
			"Wool Cloth": 1
        }
    },
	"EZ-Thro Dynamite II": {
        "ID":       23069,
        "Learn":    200,
        "Yellow":   200,
        "Green":    210,
        "Grey":     220,
        "Source":   "Vendor",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Mageweave Cloth": 2
        }
    },
	"Fire Googles": {
        "ID":       12594,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Green Tinted Googles": 1,
			"Citrine": 2,
			"Elemental Fire": 2,
			"Heavy Leather": 4
        }
    },
	"Firework Cluster Launcher": {
        "ID":       26443,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Seasonal",
        "Reagents": {
			"Inlaid Mithril Cylinder": 4,
			"Goblin Rocket Fuel": 4,
			"Truesilver Transformer": 2,
			"Mithril Casing": 1
        }
    },
	"Firework Launcher": {
        "ID":       26442,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Seasonal",
        "Reagents": {
			"Inlaid Mithril Cylinder": 1,
			"Goblin Rocket Fuel": 1,
			"Unstable Trigger": 1,
			"Mithril Casing": 1
        }
    },
	"Flame Deflector": {
        "ID":       3944,
        "Learn":    125,
        "Yellow":   125,
        "Green":    150,
        "Grey":     175,
        "Source":   "Drop",
        "Reagents": {
			"Whirring Bronze Gizmo": 1,
			"Small Flame Sac": 1 
        }
    },
	"Flash Bomb": {
        "ID":       8243,
        "Learn":    185,
        "Yellow":   185,
        "Green":    205,
        "Grey":     225,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Blue Pearl": 1,
			"Heavy Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Flying Tiger Googles": {
        "ID":       3937,
        "Learn":    100,
        "Yellow":   130,
        "Green":    145,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Light Leather": 6,
			"Tigerseye": 2
        }
    },
	"Gnomish Battle Chicken": {
        "ID":       12906,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Casing": 1,
			"Truesilver Bar": 6,
			"Mithril Bar": 6,
			"Inlaid Mithril Cylinder": 2,
			"Gold Power Core": 1,
			"Jade": 1
        }
    },
	"Gnomish Cloaking Device": {
        "ID":       3971,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Vendor",
        "Reagents": {
			"Gyrochronatom": 4,
			"Jade": 2,
			"Lesser Moonstone": 2,
			"Citrine": 2,
			"Fused Wiring": 1
        }
    },
	"Gnomish Death Ray": {
        "ID":       12759,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 2,
			"Unstable Trigger": 1,
			"Essence of Undeath": 1,
			"Ichor of Undeath": 4,
			"Inlaid Mithril Cylinder": 1
        }
    },
	"Gnomish Goggles": {
        "ID":       12897,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Fire Goggles": 1,
			"Mithril Tube": 1,
			"Gold Power Core": 2,
			"Flask of Mojo": 2,
			"Heavy Leather": 2
        }
    },
	"Gnomish Harm Prevention Belt": {
        "ID":       12903,
        "Learn":    215,
        "Yellow":   235,
        "Green":    245,
        "Grey":     255,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Dusky Belt": 1,
			"Mithril Bar": 4,
			"Truesilver Bar": 2,
			"Unstable Trigger": 1,
			"Aquamarine": 2
        }
    },
	"Gnomish Mind Control Cap": {
        "ID":       12907,
        "Learn":    235,
        "Yellow":   255,
        "Green":    265,
        "Grey":     275,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Bar": 10,
			"Truesilver Bar": 4,
			"Gold Power Core": 1,
			"Star Ruby": 2,
			"Mageweave Cloth": 4
        }
    },
	"Gnomish Net-o-Matic Projector": {
        "ID":       12902,
        "Learn":    210,
        "Yellow":   230,
        "Green":    240,
        "Grey":     250,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 1,
			"Shadow Silk": 2,
			"Thick Spiders Silk": 4,
			"Solid Blasting Powder": 2,
			"Mithril Bar": 4
        }
    },
	"Gnomish Rocket Boots": {
        "ID":       12905,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Black Mageweave Boots": 1,
			"Mithril Tube": 2,
			"Heavy Leather": 4,
			"Solid Blasting Powder": 8,
			"Gyrochronatom": 4
        }
    },
	"Gnomish Shrink Ray": {
        "ID":       12899,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Tube": 1,
			"Unstable Trigger": 1,
			"Mithril Bar": 4,
			"Flask of Mojo": 4,
			"Jade": 2
        }
    },
	"Gnomish Universal Remote": {
        "ID":       9269,
        "Learn":    125,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Bar": 6,
			"Whirring Bronze Gizmo": 1,
			"Flask of Oil": 2,
			"Tigerseye": 1,
			"Malachite": 1
        }
    },
	"Goblin Bomb Dispenser": {
        "ID":       12755,
        "Learn":    230,
        "Yellow":   230,
        "Green":    250,
        "Grey":     270,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Casing": 2,
			"Solid Blasting Powder": 4,
			"Truesilver Bar": 6,
			"Unstable Trigger": 1,
			"Accurate Scope": 2
        }
    },
	"Goblin Construction Helmet": {
        "ID":       12718,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 8,
			"Citrine": 1,
			"Elemental Fire": 4
        }
    },
	"Goblin Dragon Gun": {
        "ID":       12908,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Tube": 2,
			"Goblin Rocket Fuel": 4,
			"Mithril Bar": 6,
			"Truesilver Bar": 6,
			"Unstable Trigger": 1
        }
    },
	"Goblin Jumper Cables": {
        "ID":       9273,
        "Learn":    165,
        "Yellow":   165,
        "Green":    180,
        "Grey":     200,
        "Source":   "Vendor",
        "Reagents": {
			"Iron Bar": 6,
			"Whirring Bronze Gizmo": 2,
			"Flask of Oil": 2,
			"Silk Cloth": 2,
			"Shadowgem": 2,
			"Fused Wiring": 1
        }
    },
	"Goblin Jumper Cables XL": {
        "ID":       23078,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "Reagents": {
			"Thorium Widget": 2,
			"Truesilver Transformer": 2,
			"Fused Wiring": 2,
			"Ironweb Spider Silk": 2,
			"Star Ruby": 2
        }
    },
	"Goblin Land Mine": {
        "ID":       3968,
        "Learn":    195,
        "Yellow":   215,
        "Green":    225,
        "Grey":     235,
        "Source":   "Drop",
        "Reagents": {
			"Heavy Blasting Powder": 3,
			"Iron Bar": 2,
			"Gyrochronatom": 1
        }
    },
	"Goblin Mining Helmet": {
        "ID":       12717,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Bar": 8,
			"Citrine": 1,
			"Elemental Earth": 4
        }
    },
	"Goblin Mortar": {
        "ID":       12716,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Golbin",
        "Reagents": {
			"Mithril Tube": 2,
			"Mithril Bar": 4,
			"Solid Blasting Powder": 5,
			"Gold Power Core": 1,
			"Elemental Fire": 1
        }
    },
	"Goblin Rocket Boots": {
        "ID":       8895,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Black Mageweave Boots": 1,
			"Mithril Tube": 2,
			"Heavy Leather": 4,
			"Goblin Rocket Fuel": 2,
			"Unstable Trigger": 1
        }
    },
	"Goblin Rocket Fuel Recipe": {
        "ID":       12715,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Blank Parchment": 1,
			"Engineers Ink": 1
        }
    },
	"Goblin Rocket Helmet": {
        "ID":       12758,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Goblin Construction Helmet": 1,
			"Goblin Rocket Fuel": 4,
			"Mithril Bar": 4,
			"Unstable Trigger": 1
        }
    },
	"Goblin Sapper Charge": {
        "ID":       12760,
        "Learn":    205,
        "Yellow":   205,
        "Green":    225,
        "Grey":     245,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 3,
			"Unstable Trigger": 1
        }
    },
	"Gold Power Core": {
        "ID":       12584,
        "Learn":    150,
        "Yellow":   150,
        "Green":    170,
        "Grey":     190,
        "Source":   "Trainer",
        "Reagents": {
			"Gold Bar": 1
        }
    },
	"Green Firework": {
        "ID":       23068,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Green Lens": {
        "ID":       12622,
        "Learn":    245,
        "Yellow":   265,
        "Green":    275,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 8,
			"Jade": 3,
			"Aquamarine": 3,
			"Heart of the Wild": 2,
			"Wildvine": 2
        }
    },
	"Green Rocket Cluster": {
        "ID":       26424,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Green Tinted Goggles": {
        "ID":       3956,
        "Learn":    150,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Trainer",
        "Reagents": {
			"Medium Leather": 4,
			"Moss Agate": 2,
			"Flying Tiger Goggles": 1
        }
    },
	"Gyrochronatom": {
        "ID":       3961,
        "Learn":    170,
        "Yellow":   170,
        "Green":    190,
        "Grey":     210,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 1,
			"Gold Power Core": 1
        }
    },
	"Gyrofreeze Ice Reflector": {
        "ID":       23077,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 6,
			"Truesilver Transformer": 2,
			"Blue Sapphire": 2,
			"Essence of Fire": 4,
			"Frost Oil": 2,
			"Icecap": 4
        }
    },
	"Gyromatic Micro-Adjustor": {
        "ID":       12590,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Steel Bar": 4
        }
    },
	"Handful of Copper Bolts": {
        "ID":       3922,
        "Learn":    30,
        "Yellow":   45,
        "Green":    52,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 1
        }
    },
	"Heavy Blasting Powder": {
        "ID":       3945,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Stone": 1
        }
    },
	"Heavy Dynamite": {
        "ID":       3946,
        "Learn":    125,
        "Yellow":   125,
        "Green":    135,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Heavy Blasting Powder": 2,
			"Wool Cloth": 1
        }
    },
	"Hi-Explosive Bomb": {
        "ID":       12619,
        "Learn":    235,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 2,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 2
        }
    },
	"Hi-Impact Mithril Slugs": {
        "ID":       12596,
        "Learn":    210,
        "Yellow":   210,
        "Green":    230,
        "Grey":     250,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Hyper-Radiant Flame Reflector": {
        "ID":       23081,
        "Learn":    290,
        "Yellow":   210,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
			"Dark Iron Bar": 4,
			"Truesilver Transformer": 3,
			"Essence of Water": 6,
			"Star Ruby": 4,
			"Azerothian Diamond": 2
        }
    },
	"Ice Deflector": {
        "ID":       3957,
        "Learn":    155,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Vendor",
		"Reagents": {
			"Whirring Bronze Gizmo": 1,
			"Frost Oil": 1
        }
    },
	"Inlaid Mithril Cylinder Plans": {
        "ID":       12895,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Blank Parchment": 1,
			"Engineers Ink": 1
        }
    },
	"Iron Grenade": {
        "ID":       3962,
        "Learn":    175,
        "Yellow":   175,
        "Green":    195,
        "Grey":     215,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 1,
			"Heavy Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Iron Strut": {
        "ID":       3958,
        "Learn":    160,
        "Yellow":   160,
        "Green":    170,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Iron Bar": 2
        }
    },
	"Large Blue Rocket": {
        "ID":       26420,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Blue Rocket Cluster": {
        "ID":       26426,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Copper Bomb": {
        "ID":       3937,
        "Learn":    105,
        "Yellow":   105,
        "Green":    130,
        "Grey":     155,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 3,
			"Coarse Blasting Powder": 4,
			"Silver Contact": 1
        }
    },
	"Large Green Rocket": {
        "ID":       26421,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Green Rocket Cluster": {
        "ID":       26427,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Red Rocket": {
        "ID":       26422,
        "Learn":    175,
        "Yellow":   175,
        "Green":    187,
        "Grey":     200,
        "Source":   "Seasonal",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Large Red Rocket Cluster": {
        "ID":       26428,
        "Learn":    275,
        "Yellow":   275,
        "Green":    280,
        "Grey":     285,
        "Source":   "Seasonal",
        "Reagents": {
			"Dense Blasting Powder": 1,
			"Rugged Leather": 1
        }
    },
	"Large Seaforium Charge": {
        "ID":       3972,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Drop",
        "Reagents": {
			"Solid Blasting Powder": 2,
			"Heavy Leather": 2,
			"Refreshing Spring Water": 1
        }
    },
	"Lifelike Mechanical Toad": {
        "ID":       19793,
        "Learn":    265,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Drop",
        "Reagents": {
			"Living Essence": 1,
			"Thorium Widget": 4,
			"Gold Power Core": 1,
			"Rugged Leather": 1
        }
    },
	"Lil Smoky": {
        "ID":       15633,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Quest",
        "Faction":  "Any",
		"School":	"Gnomish",
        "Reagents": {
			"Core of Earth": 1,
			"Gyrochronatom": 2,
			"Fused Wiring": 1,
			"Mithril Bar": 2,
			"Truesilver Bar": 1
        }
    },
	"Lovingly Crafted Boomstick": {
        "ID":       3939,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 2,
			"Handful of Copper Bolts": 2,
			"Heavy Stock": 1,
			"Moss Agate": 3
        }
    },
	"Major Recombobulator": {
        "ID":       23079,
        "Learn":    275,
        "Yellow":   285,
        "Green":    290,
        "Grey":     295,
        "Source":   "Drop",
        "Reagents": {
			"Thorium Tube": 2,
			"Truesilver Transformer": 1,
			"Runecloth": 2
        }
    },
	"Master Engineers Goggles": {
        "ID":       19825,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
			"Fire Goggles": 1,
			"Huge Emerald": 2,
			"Enchanted Leather": 4
        }
    },
	"Masterwork Target Dummy": {
        "ID":       19814,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Tube": 1,
			"Thorium Widget": 2,
			"Truesilver Bar": 1,
			"Rugged Leather": 2,
			"Runecloth": 4
        }
    },
	"Mechanical Dragonling": {
        "ID":       3969,
        "Learn":    200,
        "Yellow":   220,
        "Green":    230,
        "Grey":     240,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Framework": 1,
			"Iron Strut": 4,
			"Gyrochronatom": 4,
			"Citrine": 2,
			"Fused Wiring": 1
        }
    },
	"Mechanical Repair Kit": {
        "ID":       15255,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Mechanical Squirrel": {
        "ID":       3928,
        "Learn":    75,
        "Yellow":   105,
        "Green":    120,
        "Grey":     135,
        "Source":   "Drop",
        "Reagents": {
			"Copper Modulator": 1,
			"Handful of Copper Bolts": 1,
			"Copper Bar": 1,
			"Malachite": 2
        }
    },
	"Minor Recombobulator": {
        "ID":       3952,
        "Learn":    140,
        "Yellow":   165,
        "Green":    177,
        "Grey":     190,
        "Source":   "Vendor",
        "Reagents": {
			"Bronze Tube": 1,
			"Whirring Bronze Gizmo": 2,
			"Medium Leather": 2,
			"Moss Agate": 1
        }
    },
	"Mithril Blunderbuss": {
        "ID":       12595,
        "Learn":    205,
        "Yellow":   225,
        "Green":    235,
        "Grey":     245,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Tube": 1,
			"Unstable Trigger": 1,
			"Heavy Stock": 1,
			"Mithril Bar": 4,
			"Elemental Fire": 2
        }
    },
	"Mithril Casing": {
        "ID":       12599,
        "Learn":    215,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 3
        }
    },
	"Mithril Frag Bomb": {
        "ID":       12603,
        "Learn":    215,
        "Yellow":   215,
        "Green":    235,
        "Grey":     255,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 1,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Mithril Gyro-Shot": {
        "ID":       12621,
        "Learn":    245,
        "Yellow":   245,
        "Green":    265,
        "Grey":     285,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 2,
			"Solid Blasting Powder": 2
        }
    },
	"Mithril Heavy-bore Rifle": {
        "ID":       12614,
        "Learn":    220,
        "Yellow":   240,
        "Green":    250,
        "Grey":     260,
        "Source":   "Drop",
        "Reagents": {
			"Mithril Tube": 2,
			"Unstable Trigger": 1,
			"Heavy Stock": 1,
			"Mithril Bar": 6,
			"Citrine": 2
        }
    },
	"Mithril Mechanical Dragonling": {
        "ID":       12624,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Vendor",
        "Reagents": {
			"Mithril Bar": 14,
			"Heart of Fire": 4,
			"Truesilver Bar": 4,
			"Inlaid Mithril Cylinder": 2,
			"Goblin Rocket Fuel": 2,
			"Star Ruby": 2
        }
    },
	"Mithril Tube": {
        "ID":       12589,
        "Learn":    195,
        "Yellow":   195,
        "Green":    215,
        "Grey":     235,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 3
        }
    },
	"Moonsight Rifle": {
        "ID":       3954,
        "Learn":    145,
        "Yellow":   170,
        "Green":    182,
        "Grey":     195,
        "Source":   "Drop",
        "Reagents": {
			"Bronze Tube": 3,
			"Whirring Bronze Gizmo": 3,
			"Heavy Stock": 1,
			"Lesser Moonstone": 2
        }
    },
	"Ornate Spyglass": {
        "ID":       6458,
        "Learn":    135,
        "Yellow":   160,
        "Green":    172,
        "Grey":     185,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 2,
			"Whirring Bronze Gizmo": 2,
			"Copper Modulator": 1,
			"Moss Agate": 1
        }
    },
	"Parachute Cloak": {
        "ID":       12616,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Drop",
        "Reagents": {
			"Bolt of Mageweave": 4,
			"Shadow Silk": 2,
			"Unstable Trigger": 1,
			"Solid Blasting Powder": 4
        }
    },
	"Pet Bombling": {
        "ID":       15628,
        "Learn":    205,
        "Yellow":   205,
        "Green":    205,
        "Grey":     205,
        "Source":   "Quest",
        "Faction":  "Any",
		"School":	"Goblin",
        "Reagents": {
			"Big Iron Bomb": 1,
			"Heart of Fire": 1,
			"Fused Wiring": 1,
			"Mithril Bar": 6
        }
    },
	"Portable Bronze Mortar": {
        "ID":       3960,
        "Learn":    165,
        "Yellow":   185,
        "Green":    195,
        "Grey":     205,
        "Source":   "Drop",
        "Reagents": {
			"Bronze Tube": 4,
			"Iron Strut": 1,
			"Heavy Blasting Powder": 4,
			"Medium Leather": 4
        }
    },
	"Powerful Seaforium Charge": {
        "ID":       23080,
        "Learn":    275,
        "Yellow":   275,
        "Green":    285,
        "Grey":     295,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 2,
			"Dense Blasting Powder": 3,
			"Rugged Leather": 2,
			"Refreshing Spring Water": 1
        }
    },
	"Practice Lock": {
        "ID":       8334,
        "Learn":    100,
        "Yellow":   115,
        "Green":    122,
        "Grey":     130,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 1,
			"Handful of Copper Bolts": 2,
			"Weak Flux": 1
        }
    },
	"Red Firework": {
        "ID":       23066,
        "Learn":    150,
        "Yellow":   150,
        "Green":    162,
        "Grey":     175,
        "Source":   "Vendor",
        "Reagents": {
			"Heavy Blasting Powder": 1,
			"Heavy Leather": 1
        }
    },
	"Red Rocket Cluster": {
        "ID":       26425,
        "Learn":    225,
        "Yellow":   225,
        "Green":    237,
        "Grey":     250,
        "Source":   "Seasonal",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Thick Leather": 1
        }
    },
	"Rose Colored Goggles": {
        "ID":       12618,
        "Learn":    230,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Trainer",
        "Reagents": {
			"Thick Leather": 6,
			"Star Ruby": 2
        }
    },
	"Rough Blasting Powder": {
        "ID":       3918,
        "Learn":    1,
        "Yellow":   20,
        "Green":    30,
        "Grey":     40,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Stone": 1
        }
    },
	"Rough Boomstick": {
        "ID":       3925,
        "Learn":    50,
        "Yellow":   80,
        "Green":    95,
        "Grey":     110,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Tube": 1,
			"Handful of Copper Bolts": 1,
			"Wooden Stock": 1
        }
    },
	"Rough Copper Bomb": {
        "ID":       3923,
        "Learn":    30,
        "Yellow":   60,
        "Green":    75,
        "Grey":     90,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Bar": 1,
			"Handful of Copper Bolts": 1,
			"Rough Blasting Powder": 2,
			"Linen Cloth": 1
        }
    },
	"Rough Dynamite": {
        "ID":       3919,
        "Learn":    1,
        "Yellow":   30,
        "Green":    45,
        "Grey":     60,
        "Source":   "Trainer",
        "Reagents": {
			"Rough Blasting Powder": 2,
			"Linen Cloth": 1
        }
    },
	"Salt Shaker": {
        "ID":       19567,
        "Learn":    250,
        "Yellow":   270,
        "Green":    280,
        "Grey":     290,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Bar": 6,
			"Gold Power Core": 1,
			"Unstable Trigger": 4
        }
    },
	"Shadow Goggles": {
        "ID":       3940,
        "Learn":    120,
        "Yellow":   145,
        "Green":    157,
        "Grey":     170,
        "Source":   "Drop",
        "Reagents": {
			"Medium Leather": 4,
			"Shadowgem": 2
        }
    },
	"Silver Contact": {
        "ID":       3973,
        "Learn":    90,
        "Yellow":   110,
        "Green":    125,
        "Grey":     140,
        "Source":   "Trainer",
        "Reagents": {
			"Silver Bar": 1
        }
    },
	"Silver-plated Shotgun": {
        "ID":       3949,
        "Learn":    130,
        "Yellow":   155,
        "Green":    167,
        "Grey":     180,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 2,
			"Whirring Bronze Gizmo": 2,
			"Heavy Stock": 1,
			"Silver Bar": 3
        }
    },
	"Small Blue Rocket": {
        "ID":       26416,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Bronze Bomb": {
        "ID":       3941,
        "Learn":    120,
        "Yellow":   120,
        "Green":    145,
        "Grey":     170,
        "Source":   "Trainer",
        "Reagents": {
			"Coarse Blasting Powder": 4,
			"Bronze Bar": 2,
			"Silver Contact": 1,
			"Wool Cloth": 1
        }
    },
	"Small Green Rocket": {
        "ID":       26417,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Red Rocket": {
        "ID":       26418,
        "Learn":    125,
        "Yellow":   125,
        "Green":    137,
        "Grey":     150,
        "Source":   "Seasonal",
        "Reagents": {
			"Coarse Blasting Powder": 1,
			"Medium Leather": 1
        }
    },
	"Small Seaforium Charge": {
        "ID":       3933,
        "Learn":    100,
        "Yellow":   130,
        "Green":    145,
        "Grey":     160,
        "Source":   "Drop",
        "Reagents": {
			"Coarse Blasting Powder": 2,
			"Copper Modulator": 1,
			"Light Leather": 1,
			"Refreshing Spring Water": 1
        }
    },
	"Snake Burst Firework": {
        "ID":       23507,
        "Learn":    250,
        "Yellow":   250,
        "Green":    260,
        "Grey":     270,
        "Source":   "Vendor",
        "Reagents": {
			"Dense Blasting Powder": 2,
			"Runecloth": 2,
			"Deeprock Salt": 1
        }
    },
	"Sniper Scope": {
        "ID":       12620,
        "Learn":    240,
        "Yellow":   260,
        "Green":    270,
        "Grey":     280,
        "Source":   "Drop",
        "Reagents": {
			"Mithril Tube": 1,
			"Star Ruby": 1,
			"Truesilver Bar": 2
        }
    },
	"Snowmaster 9000": {
        "ID":       21940,
        "Learn":    190,
        "Yellow":   190,
        "Green":    210,
        "Grey":     230,
        "Source":   "Seasonal",
        "Reagents": {
			"Mithril Bar": 8,
			"Gyrochronatom": 4,
			"Snowball": 4,
			"Frost Oil": 1
        }
    },
	"Solid Blasting Powder": {
        "ID":       12585,
        "Learn":    175,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Solid Stone": 2
        }
    },
	"Solid Dynamite": {
        "ID":       12586,
        "Learn":    175,
        "Yellow":   175,
        "Green":    185,
        "Grey":     195,
        "Source":   "Trainer",
        "Reagents": {
			"Solid Blasting Powder": 1,
			"Silk Cloth": 1
        }
    },
	"Spellpower Goggles Xtreme": {
        "ID":       12615,
        "Learn":    225,
        "Yellow":   245,
        "Green":    255,
        "Grey":     265,
        "Source":   "Drop",
        "Reagents": {
			"Thick Leather": 4,
			"Star Ruby": 2
        }
    },
	"Spellpower Goggles Xtreme Plus": {
        "ID":       19794,
        "Learn":    270,
        "Yellow":   290,
        "Green":    300,
        "Grey":     310,
        "Source":   "Drop",
        "Reagents": {
			"Spellpower Goggles Xtreme": 1,
			"Star Ruby": 4,
			"Enchanted Leather": 2,
			"Runecloth": 8
        }
    },
	"Standard Scope": {
        "ID":       3978,
        "Learn":    120,
        "Yellow":   135,
        "Green":    147,
        "Grey":     160,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Tube": 1,
			"Moss Agate": 1
        }
    },
	"Steam Tonk Controller": {
        "ID":       28327,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Thorium Widget": 2,
			"Mithril Casing": 1,
			"Gold Power Core": 1
        }
    },
	"Target Dummy": {
        "ID":       3932,
        "Learn":    85,
        "Yellow":   115,
        "Green":    130,
        "Grey":     145,
        "Source":   "Trainer",
        "Reagents": {
			"Copper Modulator": 1,
			"Handful of Copper Bolts": 2,
			"Bronze Bar": 1,
			"Wool Cloth": 1
        }
    },
	"The Big One": {
        "ID":       12754,
        "Learn":    235,
        "Yellow":   235,
        "Green":    255,
        "Grey":     275,
        "Source":   "Trainer",
		"School":	"Goblin",
        "Reagents": {
			"Mithril Casing": 1,
			"Goblin Rocket Fuel": 1,
			"Solid Dynamite": 6,
			"Unstable Trigger": 1
        }
    },
	"Thorium Grenade": {
        "ID":       19790,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Widget": 1,
			"Thorium Bar": 3,
			"Dense Blasting Powder": 3,
			"Runecloth": 3
        }
    },
	"Thorium Rifle": {
        "ID":       19792,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Drop",
        "Reagents": {
			"Mithril Tube": 2,
			"Mithril Casing": 2,
			"Thorium Widget": 2,
			"Thorium Bar": 4,
			"Deadly Scope": 1
        }
    },
	"Thorium Shells": {
        "ID":       19800,
        "Learn":    285,
        "Yellow":   305,
        "Green":    315,
        "Grey":     325,
        "Source":   "Drop",
        "Reagents": {
			"Thorium Bar": 2,
			"Dense Blasting Powder": 1
        }
    },
	"Thorium Tube": {
        "ID":       19795,
        "Learn":    275,
        "Yellow":   295,
        "Green":    305,
        "Grey":     315,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Bar": 6
        }
    },
	"Thorium Widget": {
        "ID":       19791,
        "Learn":    260,
        "Yellow":   280,
        "Green":    290,
        "Grey":     300,
        "Source":   "Vendor",
        "Reagents": {
			"Thorium Bar": 3,
			"Runecloth": 1
        }
    },
	"Tranquil Mechanical Yeti": {
        "ID":       26011,
        "Learn":    250,
        "Yellow":   320,
        "Green":    330,
        "Grey":     340,
        "Source":   "Quest",
        "Faction":  "Any",
        "Reagents": {
			"Cured Rugged Hide": 1,
			"Thorium Widget": 4,
			"Globe of Water": 2,
			"Truesilver Transformer": 2,
			"Gold Power Core": 1
        }
    },
	"Truesilver Transformer": {
        "ID":       23071,
        "Learn":    260,
        "Yellow":   270,
        "Green":    275,
        "Grey":     280,
        "Source":   "Vendor",
        "Reagents": {
			"Truesilver Bar": 2,
			"Elemental Earth": 2,
			"Elemental Air": 1
        }
    },
	"Ultrasafe Transporter - Gadgetzan": {
        "ID":       23489,
        "Learn":    260,
        "Yellow":   285,
        "Green":    295,
        "Grey":     305,
        "Source":   "Trainer",
		"School":	"Gnomish",
        "Reagents": {
			"Mithril Bar": 12,
			"Truesilver Transformer": 2,
			"Core of Earth": 4,
			"Globe of Water": 2,
			"Aquamarine": 4,
			"Inlaid Mithril Cylinder": 1
        }
    },
	"Unstable Trigger": {
        "ID":       12591,
        "Learn":    200,
        "Yellow":   200,
        "Green":    220,
        "Grey":     240,
        "Source":   "Trainer",
        "Reagents": {
			"Mithril Bar": 1,
			"Mageweave Cloth": 1,
			"Solid Blasting Powder": 1
        }
    },
	"Voice Amplification Modulator": {
        "ID":       19819,
        "Learn":    290,
        "Yellow":   310,
        "Green":    320,
        "Grey":     330,
        "Source":   "Drop",
        "Reagents": {
			"Delicate Arcanite Converter": 2,
			"Gold Power Core": 1,
			"Thorium Widget": 1,
			"Large Opal": 1
        }
    },
	"Whirring Bronze Gizmo": {
        "ID":       3942,
        "Learn":    125,
        "Yellow":   125,
        "Green":    150,
        "Grey":     175,
        "Source":   "Trainer",
        "Reagents": {
			"Bronze Bar": 2,
			"Wool Cloth": 1
        }
    },
	"World Enlarger": {
        "ID":       23129,
        "Learn":    260,
        "Yellow":   260,
        "Green":    265,
        "Grey":     270,
        "Source":   "Drop",
        "Reagents": {
			"Mithril Casing": 1,
			"Thorium Widget": 2,
			"Gold Power Core": 1,
			"Unstable Trigger": 1,
			"Citrine": 1
        }
    }
}

import json
with open('engineering.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)