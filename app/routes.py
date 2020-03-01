from flask import render_template, flash, redirect, url_for
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

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UserInputForm()

    if form.validate_on_submit():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        flash('{}: Calculated for {} - {} - {} - {}'.format(current_time,
            form.server.data, form.profession.data, form.startSkill.data, form.targetSkill.data))
        return redirect(url_for('index'))

    return render_template('index.html',
        title=title,
        author=author,
        form=form)