from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import UserInputForm
from datetime import datetime
from app.functions import *

author = {
    'username': 'Znibb',
    'server':   'Noggenfogger',
    'discord':  "https://discordapp.com/channels/@me/192987995006173184"}
title = {
    'short':    'WPLT',
    'long':     'WowProfessionLevelingTool',
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
        session["blacksmithingSchool"] = form.blacksmithingSchool.data
        session["engineeringSchool"] = form.engineeringSchool.data

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
        form.blacksmithingSchool.data=session.get("blacksmithingSchool")
        form.engineeringSchool.data=session.get("engineeringSchool")
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
        session.pop("blacksmithingSchool", None)
        session.pop("engineeringSchool", None)
    
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
        session["blacksmithingSchool"] = form.blacksmithingSchool.data
        session["engineeringSchool"] = form.engineeringSchool.data

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
    else:
        school = "None"

    recipes = importRecipes(form.profession.data, form.startSkill.data, form.targetSkill.data, recipeSources, form.faction.data, school)
    reagentPrices = getReagentPrices(recipes, form.server.data, form.faction.data)
    recipePrices = calculateRecipePrices(recipes, reagentPrices)
    currentSkill = form.startSkill.data
    targetSkill = form.targetSkill.data

    # Initialize outputs
    craftList = dict()
    reagentsToBuy = dict()
    recipesToBuy = dict()
    oldestDataUsedObj = datetime.now()

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
            if info["Yellow"] <= currentSkill:
                recipes.pop(name)

        # Determine next craft
        bestCraft = getCheapestSkillingRecipe(recipes, recipePrices, currentSkill)

        # Break loop if no skillable craft is available
        if bestCraft == '':
            break

        # Update craft list
        # Check if this is the first entry
        if not bool(craftList):
            craftList[1] = {"Start": currentSkill, "Count": 1, "Recipe": bestCraft, "Cost": prettyPrintPrice(recipePrices[bestCraft])}
        else:
            # Get index of the last entry
            lastIndex = list(craftList.keys())[-1]
            # If this craft is the same as the last one
            if craftList[lastIndex]["Recipe"] == bestCraft:
                # Increment the count
                craftList[lastIndex]["Count"] += 1
            # If it's a new one
            else:
                # Create a new entry
                craftList[lastIndex+1] = {"Start": currentSkill, "Count": 1, "Recipe": bestCraft, "Cost": prettyPrintPrice(recipePrices[bestCraft])}

        # Add reagents for the chosen recipe to the purchase list
        for reagent, amount in recipes[bestCraft]["Reagents"].items():
            if reagent in reagentsToBuy:
                reagentsToBuy[reagent]["Amount"] += amount
            else:
                reagentsToBuy[reagent] = dict()
                reagentsToBuy[reagent]["Amount"] = amount
                reagentsToBuy[reagent]["PPU"] = prettyPrintPrice(reagentPrices[reagent]["Price"])

        # Add recipe to shopping list if it's source is 'drop'
        if recipes[bestCraft]["Source"] == "Drop":
            if bestCraft not in recipesToBuy.keys():
                recipesToBuy[bestCraft] = dict()
                recipesToBuy[bestCraft]["ID"] = recipes[bestCraft]["RecipeID"]
                recipesToBuy[bestCraft]["Price"] = 0

        # Increment skill
        currentSkill += 1
    
    # Calculate cost for each reagent purchased
    for reagent in reagentsToBuy:
        reagentsToBuy[reagent]["Total"] = prettyPrintPrice(reagentsToBuy[reagent]["Amount"] * reagentPrices[reagent]["Price"])
        if reagentPrices[reagent]["LastSeen"] < oldestDataUsedObj:
            oldestDataUsedObj = reagentPrices[reagent]["LastSeen"]

    oldestDataUsed = oldestDataUsedObj.strftime("%Y-%m-%d %X")

    # Calculate total reagent purchasing cost
    reagentCost = prettyPrintPrice(calculateReagentCost(reagentsToBuy, reagentPrices))

    # Calculate cost for each recipe purchase and aggregate total recipe cost
    recipeCost = 0
    for name in recipesToBuy.keys():
        price = getRecipePrice(recipesToBuy[name]["ID"], form.server.data, form.faction.data)
        recipeCost += price
        recipesToBuy[name]["Price"] = prettyPrintPrice(price)
    recipeCost = prettyPrintPrice(recipeCost)

    # Calculate total cost
    costs = [reagentCost,
             recipeCost]
    totalCost = sumPretty(costs)

    return render_template('results.html',
        title=title,
        author=author,
        form=form,
        craftList=craftList,
        oldestDataUsed=oldestDataUsed,
        reagents=reagentsToBuy,
        reagentCost=reagentCost,
        recipesToBuy=recipesToBuy,
        recipeCost=recipeCost,
        totalCost=totalCost)