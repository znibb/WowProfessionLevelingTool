import json
import math
import requests

baseUrl = "https://api.nexushub.co/wow-classic/v1/items/"

def calculateRecipePrices(recipes, prices):
    recipePriceDict = dict()

    for name, info in recipes.items():
        price = 0
        for reagent, amount in info["Reagents"].items():
            price += amount*prices[reagent]
        recipePriceDict[name] = price
    
    return recipePriceDict

def calculateTotalCost(reagents, prices):
    totalCost = 0
    for reagent, info in reagents.items():
        totalCost += info["Amount"]*prices[reagent]

    return totalCost

def getCheapestSkillingRecipe(recipes, recipePrices, currentSkill):
    cost = 999999 # arbitrary large number
    candidate = ''

    for name, info in recipes.items():
        if info["Learn"] <= currentSkill:
            if recipePrices[name] < cost:
                candidate = name
                cost = recipePrices[name]

    return candidate
    
def getReagentPrices(recipes, server, faction):
    # Import translation table for item name to ID
    with open("app/data/itemID.json", 'r') as f:
            itemID = json.load(f)

    # Make a set of all potential reagents
    reagents = set()
    for name, info in recipes.items():
        for reagent, amount in info["Reagents"].items():
            reagents.add(reagent)
    
    # Iterate over the reagent set and create a dictionary containing reagent-price pairs
    reagentPriceDict = dict()
    serverUrl = baseUrl + server[3:].lower() + '-' + faction.lower() + '/'
    for reagent in reagents:
        requestUrl = serverUrl + str(itemID[reagent])
        response = requests.get(requestUrl)
        responseJson = response.json()
        if responseJson["vendorPrice"] == None:
            reagentPriceDict[reagent] = responseJson["stats"]["current"]["marketValue"]
        else:
            reagentPriceDict[reagent] = responseJson["vendorPrice"]

    return reagentPriceDict

def importRecipes(profession, startSkill, targetSkill):
    # Import apropriate list of recipes
    '''
    if profession is "Alchemy":
        with open("data/alchemy.json", 'r') as f:
            recipes = json.load(f)
    else:
        return
    '''
    with open("app/data/alchemy.json", 'r') as f:
        recipes = json.load(f)

    # Remove recipes that we've already out-levelled
    temp = recipes.copy()
    for name, info in temp.items():
        if info["Yellow"] <= startSkill:
            recipes.pop(name)
    
    # Remove recipes from upcoming phases
    temp = recipes.copy()
    for name, info in temp.items():
        if not "Learn" in info:
            recipes.pop(name)

    # Remove recipes that are learned past our target skill
    temp = recipes.copy()
    for name, info in temp.items():
        if info["Learn"] >= targetSkill:
            recipes.pop(name)

    
    
    # Return dictionary with all relevant recipes
    return recipes

def prettyPrintPrice(price):
    gold = math.floor(price/10000)
    silver = math.floor(price%10000/100)
    copper = price%100

    result = ''
    if not gold:
        if not silver:
            result = "{}c".format(copper)
        else:
            result = "{}s{:02}c".format(silver, copper)
    else:
        result = "{}g{:02}s{:02}c".format(gold, silver, copper)
    
    return result
