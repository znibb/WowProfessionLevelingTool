#!/usr/bin/env python3.7

recipes = {
	"": {
        "ID":       ,
        "Learn":    ,
        "Yellow":   ,
        "Green":    ,
        "Grey":     ,
        "Source":   "Trainer",
        "Reagents": {

        }
    },
    "": {
        "ID":       ,
        "Learn":    ,
        "Yellow":   ,
        "Green":    ,
        "Grey":     ,
        "Source":   "Trainer",
        "Reagents": {

        }
    }
}

import json
with open('tailoring.json', 'w') as jsonFile:
    json.dump(recipes, jsonFile)