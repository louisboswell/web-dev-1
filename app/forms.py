from flask_wtf import Form
from wtforms import DateField
from wtforms import TextField
from wtforms import BooleanField
from wtforms import DateTimeField
from wtforms import TextAreaField

from wtforms.validators import DataRequired
import wtforms.validators as validators

class AssessmentForm(Form):
    name = TextField('name', validators = [DataRequired()])
    module = TextField('module', validators = [DataRequired()])
    description = TextAreaField('description', validators = [DataRequired()])
    completed = BooleanField('completed', validators = [DataRequired()])
    date = DateTimeField('date', validators = [DataRequired()])


class BooleanForm(Form):
    completed = BooleanField('completed', validators = [DataRequired()])

class DateForm(Form):
    date = DateTimeField('date', validators = [DataRequired()])