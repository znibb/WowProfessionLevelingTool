from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import UserInputForm
from datetime import datetime
from app.functions import *

VERSION="1.6.0"

author = {
    'username': 'Znibb',
    'server':   'Noggenfogger',
    'email':    "znibb@zkylark.se"}
title = {
    'short':    'WPLT',
    'long':     'WowProfessionLevelingTool v' + VERSION,
    'source':   'https://github.com/znibb/WowProfessionLevelingTool'}

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserInputForm()

    if form.validate_on_submit():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        flash('{}: Calculated for {} - {} - {} - {} - {}'.format(current_time,
            form.server.data, form.faction.data, form.profession.data, form.startSkill.data, form.targetSkill.data))
        session["server"] = form.server.data
        session["faction"] = form.faction.data
        session["profession"] = form.profession.data
        session["startSkill"] = form.startSkill.data
        session["targetSkill"] = form.targetSkill.data
        session["includeVendor"] = form.includeVendor.data
        session["includeVendorLimited"] = form.includeVendorLimited.data
        session["includeDrop"] = form.includeDrop.data
        session["includeQuest"] = form.includeQuest.data
        session["includeReputation"] = form.includeReputation.data
        session["includeSeasonal"] = form.includeSeasonal.data

        session["difficulty"] = form.difficulty.data

        session["blacksmithingSchool"] = form.blacksmithingSchool.data
        session["engineeringSchool"] = form.engineeringSchool.data
        session["leatherworkingSchool"] = form.leatherworkingSchool.data
        session["enchantingRods"] = form.enchantingRods.data

        return redirect(url_for('results'))

    return render_template('index.html',
        title=title,
        author=author,
        form=form)

@app.route('/results', methods=['GET', 'POST'])
def results():
    form = UserInputForm()

    if not session.get("server") is None:
        form.server.data=session.get("server")
        form.faction.data=session.get("faction")
        form.profession.data=session.get("profession")
        form.startSkill.data=session.get("startSkill")
        form.targetSkill.data=session.get("targetSkill")
        form.includeVendor.data=session.get("includeVendor")
        form.includeVendorLimited.data=session.get("includeVendorLimited")
        form.includeDrop.data=session.get("includeDrop")
        form.includeQuest.data=session.get("includeQuest")
        form.includeReputation.data=session.get("includeReputation")
        form.includeSeasonal.data=session.get("includeSeasonal")

        form.difficulty.data = session.get("difficulty")
        
        form.blacksmithingSchool.data=session.get("blacksmithingSchool")
        form.engineeringSchool.data=session.get("engineeringSchool")
        form.leatherworkingSchool.data=session.get("leatherworkingSchool")
        form.enchantingRods.data=session.get("enchantingRods")
        session.pop("server", None)
        session.pop("faction", None)
        session.pop("profession", None)
        session.pop("startSkill", None)
        session.pop("targetSkill", None)
        session.pop("includeVendor", None)
        session.pop("includeVendorLimited", None)
        session.pop("includeDrop", None)
        session.pop("includeQuest", None)
        session.pop("includeReputation", None)
        session.pop("includeSeasonal", None)

        session.pop("difficulty", None)

        session.pop("blacksmithingSchool", None)
        session.pop("engineeringSchool", None)
        session.pop("leatherworkingSchool", None)
        session.pop("enchantingRods", None)

    if form.validate_on_submit():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        flash('{}: Calculated for {} - {} - {} - {} - {}'.format(current_time,
            form.server.data, form.faction.data, form.profession.data, form.startSkill.data, form.targetSkill.data))
        session["server"] = form.server.data
        session["faction"] = form.faction.data
        session["profession"] = form.profession.data
        session["startSkill"] = form.startSkill.data
        session["targetSkill"] = form.targetSkill.data
        session["includeVendor"] = form.includeVendor.data
        session["includeVendorLimited"] = form.includeVendorLimited.data
        session["includeDrop"] = form.includeDrop.data
        session["includeQuest"] = form.includeQuest.data
        session["includeReputation"] = form.includeReputation.data
        session["includeSeasonal"] = form.includeSeasonal.data

        session["difficulty"] = form.difficulty.data
        
        session["blacksmithingSchool"] = form.blacksmithingSchool.data
        session["engineeringSchool"] = form.engineeringSchool.data
        session["leatherworkingSchool"] = form.leatherworkingSchool.data
        session["enchantingRods"] = form.enchantingRods.data

        return redirect(url_for('results'))

    ##########################
    ### Main program logic ###
    ##########################

    # Collect required data
    recipeSources = {"Vendor": form.includeVendor.data,
                    "VendorLimited": form.includeVendorLimited.data,
                    "Drop": form.includeDrop.data,
                    "Quest": form.includeQuest.data,
                    "Reputation": form.includeReputation.data,
                    "Seasonal": form.includeSeasonal.data}

    school = ""
    if form.profession.data == "Blacksmithing":
        school = form.blacksmithingSchool.data
    elif form.profession.data == "Engineering":
        school = form.engineeringSchool.data
    elif form.profession.data == "Leatherworking":
        school = form.leatherworkingSchool.data
    else:
        school = "None"

    allRecipes = importRecipes(form.profession.data, form.targetSkill.data, recipeSources, form.faction.data, school)
    reagentPrices = getReagentPrices(allRecipes, form.server.data, form.faction.data)
    recipePrices = calculateRecipePrices(allRecipes, reagentPrices)
    currentSkill = form.startSkill.data
    targetSkill = form.targetSkill.data
    enchantingRodsOverride = form.enchantingRods.data and form.profession.data == "Enchanting"

    # Initialize outputs
    craftList = dict()
    reagentsToBuy = dict()
    recipesFromAH = dict()
    recipesFromVendor = dict()
    recipesFromVendorLimited = dict()
    recipesFromQuest = dict()
    recipesFromReputation = dict()
    recipesFromSeasonal = dict()

    # Create prunable copy
    recipes = allRecipes.copy()

    # Remove recipes that doesn't have a determinable price, i.e. one or more reagents hasn't been seen on the AH
    temp = recipes.copy()
    for recipe in temp.keys():
        if recipe not in recipePrices:
            recipes.pop(recipe)

    while(True):
        # Break the loop if we're at the target skill
        if currentSkill == targetSkill:
            break

        # Remove recipes that we've out-levelled
        temp = recipes.copy()
        for name, info in temp.items():
            if info["Grey"] <= currentSkill:
                recipes.pop(name)
            elif (form.difficulty.data == "Yellow") and (currentSkill >= info["Green"]):
                recipes.pop(name)
            elif (form.difficulty.data == "Orange") and (currentSkill >= info["Yellow"]):
                recipes.pop(name)

        # Determine next craft
        (bestCraft, multiplier) = getCheapestSkillingRecipe(recipes, recipePrices, currentSkill, enchantingRodsOverride)
        
        # Break loop if no skillable craft is available
        if bestCraft == '':
            break

        # Update craft list
        # Check if this is the first entry
        if not bool(craftList):
            craftList[1] = {"Start": currentSkill, "End": 1, "Count": multiplier, "Recipe": bestCraft, "Cost": prettyPrintPrice(recipePrices[bestCraft])}
        else:
            # Get index of the last entry
            lastIndex = list(craftList.keys())[-1]
            # If this craft is the same as the last one
            if craftList[lastIndex]["Recipe"] == bestCraft:
                # Increment the count
                craftList[lastIndex]["End"] += 1
                craftList[lastIndex]["Count"] = craftList[lastIndex]["Count"] + multiplier
            # If it's a new one
            else:
                # Create a new entry
                craftList[lastIndex]["Count"] = craftList[lastIndex]["Count"]
                craftList[lastIndex+1] = {"Start": currentSkill, "End": 1,"Count": multiplier, "Recipe": bestCraft, "Cost": prettyPrintPrice(recipePrices[bestCraft])}

        # Add reagents for the chosen recipe to the purchase list
        for reagent, amount in recipes[bestCraft]["Reagents"].items():
            if reagent in reagentsToBuy:
                reagentsToBuy[reagent]["Amount"] = reagentsToBuy[reagent]["Amount"] + (amount * multiplier)
            else:
                reagentsToBuy[reagent] = dict()
                reagentsToBuy[reagent]["Amount"] = (amount * multiplier)
                reagentsToBuy[reagent]["PPU"] = reagentPrices[reagent]["Price"]

        # Add recipe to appropriate shopping list
        if recipes[bestCraft]["Source"] == "Vendor":
            recipesFromVendor[bestCraft] = recipes[bestCraft]["RecipeID"]
        elif recipes[bestCraft]["Source"] == "VendorLimited":
            recipesFromVendorLimited[bestCraft] = recipes[bestCraft]["RecipeID"]
        elif recipes[bestCraft]["Source"] == "Drop":
            if bestCraft not in recipesFromAH.keys():
                recipesFromAH[bestCraft] = dict()
                recipesFromAH[bestCraft]["ID"] = recipes[bestCraft]["RecipeID"]
                recipesFromAH[bestCraft]["Price"] = 0
        elif recipes[bestCraft]["Source"] == "Quest":
            recipesFromQuest[bestCraft] = recipes[bestCraft]["RecipeID"]
        elif recipes[bestCraft]["Source"] == "Reputation":
            recipesFromReputation[bestCraft] = recipes[bestCraft]["RecipeID"]
        elif recipes[bestCraft]["Source"] == "Seasonal":
            recipesFromSeasonal[bestCraft] = recipes[bestCraft]["RecipeID"]
        else:
            pass

        # Increment skill
        currentSkill += 1
    
    # Clean up partial Counts
    for craft in craftList:
        craftList[craft]["Count"] = math.ceil(craftList[craft]["Count"])

    # Check if any reagents on the shopping list will be crafted
    temp = reagentsToBuy.copy()
    for reagent in temp.keys():
        val = searchCraftList(craftList, reagent)

        # If the reagent has been crafted previously
        if len(val) > 0:
            index = val[0]

            if "AmountCrafted" in allRecipes[craftList[index]["Recipe"]]:
                amountPerCraft = allRecipes[craftList[index]["Recipe"]]["AmountCrafted"]
            else:
                amountPerCraft = 1

            amountCrafted = craftList[index]["Count"]*amountPerCraft
            amountNeeded = reagentsToBuy[reagent]["Amount"]

            if amountCrafted >= amountNeeded:
                reagentsToBuy.pop(reagent)
            else:
                reagentsToBuy[reagent]["Amount"] = amountNeeded - amountCrafted

    # If we're able to craft a reagent, check if that's cheaper than purchasing the 'reagent' from the AH
    temp = reagentsToBuy.copy()
    for reagent, data in temp.items():
        # If we are able to craft a 'reagent'
        if reagent in recipePrices:
            # If crafting cost is lower than purchasing price
            if recipePrices[reagent] < reagentsToBuy[reagent]["PPU"]:
                # Add "sub-reagents" to shopping list
                for subReagent, amount in allRecipes[reagent]["Reagents"].items():
                    if subReagent in reagentsToBuy.keys():
                        reagentsToBuy[subReagent]["Amount"] += amount*data["Amount"]
                    else:
                        reagentsToBuy[subReagent] = dict()
                        reagentsToBuy[subReagent]["Amount"] = amount*data["Amount"]
                        reagentsToBuy[subReagent]["PPU"] = reagentPrices[reagent]["Price"]

                # Remove the reagent itself from the shopping list
                reagentsToBuy.pop(reagent)

    # Calculate cost for each reagent purchase
    for reagent in reagentsToBuy:
        reagentsToBuy[reagent]["Amount"] = math.ceil(reagentsToBuy[reagent]["Amount"])
        reagentsToBuy[reagent]["Total"] = prettyPrintPrice(math.ceil(reagentsToBuy[reagent]["Amount"]) * reagentPrices[reagent]["Price"])

    # Pretty print PPU for reagents
    for reagent in reagentsToBuy:
        reagentsToBuy[reagent]["PPU"] = prettyPrintPrice(reagentsToBuy[reagent]["PPU"])

    # Calculate total reagent purchasing cost
    reagentCost = prettyPrintPrice(calculateReagentCost(reagentsToBuy, reagentPrices))

    # Calculate cost for each recipe purchase and aggregate total recipe cost
    recipeCost = 0
    for name in recipesFromAH.keys():
        price = getRecipePrice(recipesFromAH[name]["ID"], form.server.data, form.faction.data)
        recipeCost += price
        recipesFromAH[name]["Price"] = prettyPrintPrice(price)
    recipeCost = prettyPrintPrice(recipeCost)

    # Calculate money recouperated from selling all crafted items to vendor
    moneyFromVendoring = prettyPrintPrice(calculateSellToVendor(craftList, form.profession.data, form.server.data, form.faction.data))

    # Calculate total cost
    costs = [reagentCost,
             recipeCost,
            "-" + moneyFromVendoring]
    totalCost = sumPretty(costs)

    # Pass along itemID dictionary to be able to fetch tooltips
    with open("app/data/itemID.json", 'r') as f:
            itemID = json.load(f)

    return render_template('results.html',
        title=title,
        author=author,
        form=form,
        craftList=craftList,
        reagents=reagentsToBuy,
        reagentCost=reagentCost,
        recipesFromAH=recipesFromAH,
        recipeCost=recipeCost,
        recipesFromVendor=recipesFromVendor,
        recipesFromVendorLimited=recipesFromVendorLimited,
        recipesFromQuest=recipesFromQuest,
        recipesFromReputation=recipesFromReputation,
        recipesFromSeasonal=recipesFromSeasonal,
        moneyFromVendoring=moneyFromVendoring,
        totalCost=totalCost,
        itemID=itemID,
        allRecipes=allRecipes,
        targetReached = currentSkill == targetSkill)
