import json
import requests

baseUrl = "https://api.nexushub.co/wow-classic/v1/items/"

def importRecipes(profession, skillLevel):
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
        if info["Yellow"] <= skillLevel:
            recipes.pop(name)
    
    # Remove recipes from upcoming phases
    temp = recipes.copy()
    for name, info in temp.items():
        if not "Learn" in info:
            recipes.pop(name)
    
    # Return dictionary with all relevant recipes
    return recipes

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
        reagentPriceDict[reagent] = responseJson["stats"]["current"]["marketValue"]

    return reagentPriceDict