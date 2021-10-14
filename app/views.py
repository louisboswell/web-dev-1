from flask import render_template, flash
from app import app, models, db
from .forms import AssessmentForm

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/all')
def all():
    database = models.Assessment.query.all()
    return render_template("banner_templates/all.html")

@app.route('/completed')
def completed():
    return render_template("banner_templates/completed.html")

@app.route('/uncompleted')
def uncompleted():
    return render_template("banner_templates/uncompleted.html")

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AssessmentForm()


    # Check if form is validated correctly
    if form.validate_on_submit():
        flash('Successfully received form data.')

        # Submit data to the db
        temp = models.Assessment(
            name = form.name.data,
            module = form.module.data,
            description = form.description.data,
            date = form.date.data,
            completed = form.completed.data
        )
        
        db.session.add(temp)
        db.session.commit()

    else:
        for key in form.errors:
            flash("%s field is required." % (key))

    return render_template("banner_templates/add.html", 
    title = 'Add an assessment', form = form)


# Each individual route refers to a new page 
# i.e. www.google.com/XXXX
