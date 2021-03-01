from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField, BooleanField, SelectMultipleField, RadioField
from wtforms.validators import InputRequired, NumberRange
import requests

professions = [
    'Alchemy',
    'Blacksmithing',
    'Cooking',
    'Enchanting',
    'Engineering',
    'Leatherworking',
    'Tailoring']

# Fetch server list
response = requests.get("https://api.nexushub.co/wow-classic/v1/servers/full/")
responseJson = response.json()

servers = dict()
for line in responseJson:
    servers[line["slug"]] = line["name"]

class UserInputForm(FlaskForm):
    server = SelectField(u'Server',
        default='noggenfogger',
        choices=[(slug, name) for slug, name in servers.items()])
    faction = SelectField(u'Faction',
        default='horde',
        choices=[('alliance', 'Alliance'), ('horde', "Horde")])
    profession = SelectField(u'Profession',
        choices=[(profession, profession) for profession in professions])
    startSkill = IntegerField(u'Starting skill',
        default=1,
        validators=[InputRequired(),
                    NumberRange(min=1, max=299)])
    targetSkill = IntegerField(u'Target skill',
        default=300,
        validators=[InputRequired(),
                    NumberRange(min=2, max=300)])
    calculate = SubmitField('Calculate')
    includeVendor = BooleanField(u'Vendor', default="checked")
    includeVendorLimited = BooleanField(u'VendorLimited', default="checked")
    includeDrop = BooleanField(u'Drop')
    includeQuest = BooleanField(u'Quest')
    includeReputation = BooleanField(u'Reputation')
    includeSeasonal = BooleanField(u'Seasonal')

    difficulty = RadioField(u'Difficulty:',
        choices=[("Green", "Green"), 
            ("Yellow", "Yellow"), 
            ("Orange", "Orange")],
        default="Orange")

    blacksmithingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Armorsmithing", "Armorsmithing"),
                ("Weaponsmithing", "Weaponsmithing")],
        default="None")
    engineeringSchool = RadioField(u'School:',
        choices=[("None", "None"),
                ("Gnomish", "Gnomish"),
                ("Goblin", "Goblin")],
        default="None")
    leatherworkingSchool = RadioField(u'School:',
        choices=[("None", "None"),
                 ("Dragonscale", "Dragonscale"),
                 ("Elemental", "Elemental"),
                 ("Tribal", "Tribal")],
        default="None")
    enchantingRods = BooleanField(u'Include enchanting rods', default="checked")