from flask import render_template, flash, redirect, url_for, session
from app import app
from app.forms import UserInputForm
from datetime import datetime

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
    
    if not session.get("server") is None:
        form.server.data=session.get("server")
        form.profession.data=session.get("profession")
        form.startSkill.data=session.get("startSkill")
        form.targetSkill.data=session.get("targetSkill")
        session.pop("server", None)
        session.pop("profession", None)
        session.pop("startSkill", None)
        session.pop("targetSkill", None)
    

    if form.validate_on_submit():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        flash('{}: Calculated for {} - {} - {} - {}'.format(current_time,
            form.server.data, form.profession.data, form.startSkill.data, form.targetSkill.data))
        session["server"] = form.server.data
        session["profession"] = form.profession.data
        session["startSkill"] = form.startSkill.data
        session["targetSkill"] = form.targetSkill.data
        return redirect(url_for('index'))

    return render_template('index.html',
        title=title,
        author=author,
        form=form)