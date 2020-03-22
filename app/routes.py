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

    # Main program logic
    recipes = importRecipes(form.profession.data, form.startSkill.data)
    reagentPrices = getReagentPrices(recipes, form.server.data, form.faction.data)
    recipePrices = calculateRecipePrices(recipes, reagentPrices)

    output = dict()
    for recipe, price in recipePrices.items():
        output[recipe] = prettyPrintPrice(price)

    return render_template('results.html',
        title=title,
        author=author,
        form=form,
        output=output)