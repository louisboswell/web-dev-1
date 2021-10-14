from flask_wtf import Form
from wtforms import DateField
from wtforms import TextField
from wtforms import BooleanField
from wtforms import DateTimeField

from wtforms.validators import DataRequired

class TextForm(Form):
    name = TextField('name', validators = [DataRequired()])
    module = TextField('module', validators = [DataRequired()])
    description = TextField('description', validators = [DataRequired()])

class BooleanForm(Form):
    completed = BooleanField('completed', validators = [DataRequired()])

class DateForm(Form):
    date = DateField('date', validators = [DataRequired()])