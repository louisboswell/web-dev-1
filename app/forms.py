from flask_wtf import Form
from wtforms import TextField
from wtforms import BooleanField
from wtforms import DateTimeField
from wtforms import TextAreaField
from wtforms.fields.html5 import DateField

from datetime import datetime

from wtforms.validators import DataRequired

class AssessmentForm(Form):
    name = TextField('Name', validators = [DataRequired()])
    module = TextField('Module', validators = [DataRequired()])
    description = TextAreaField('Description')
    completed = BooleanField('Completed')
    date = DateField('date', validators = [DataRequired()], default = datetime.now())