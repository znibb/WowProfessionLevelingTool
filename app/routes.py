from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import UserInputForm
from datetime import datetime
from app.functions import *

author = {
    'username': 'znibb',
    'server':   'Noggenfogger'
}
title = {
    'short':    'skillCalc',
    'long':     'WowProfessionLevelingTool'
}

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
        session.pop("server", None)
        session.pop("faction", None)
        session.pop("profession", None)
        session.pop("startSkill", None)
        session.pop("targetSkill", None)
    
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

        return redirect(url_for('results'))

    ##########################
    ### Main program logic ###
    ##########################

    # Collect required data
    recipes = importRecipes(form.profession.data, form.startSkill.data, form.targetSkill.data)
    reagentPrices = getReagentPrices(recipes, form.server.data, form.faction.data)
    recipePrices = calculateRecipePrices(recipes, reagentPrices)
    currentSkill = form.startSkill.data
    targetSkill = form.targetSkill.data

    # Initialize outputs
    craftList = dict()
    reagentsToBuy = dict()

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
                reagentsToBuy[reagent]["PPU"] = prettyPrintPrice(reagentPrices[reagent])
        
        # Increment skill
        currentSkill += 1
    
    totalCost = prettyPrintPrice(calculateTotalCost(reagentsToBuy, reagentPrices))

    return render_template('results.html',
        title=title,
        author=author,
        form=form,
        craftList=craftList,
        reagents=reagentsToBuy,
        totalCost=totalCost)