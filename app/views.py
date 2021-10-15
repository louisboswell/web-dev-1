from flask import render_template, flash, request
from app import app, models, db
from .forms import AssessmentForm

# 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

@app.route('/')
def home():
    number = len(models.Assessment.query.filter_by(completed = False).all())
    return render_template("home.html", number = number)

@app.route('/all', methods = ['GET', 'POST'])
def all():
    database = models.Assessment.query.all()
    return render_template("banner_templates/all.html", database = database)

# Route used for setting an assessment to complete
@app.route('/complete', methods = ['GET', 'POST'])
def complete():

    print('COMPLETE BUTTON WORKING')
    print(request.form.getlist('name'))

    database = models.Assessment.query.all()
    return render_template("banner_templates/all.html", database = database)

# Route used for deleting an assessment
@app.route('/delete', methods = ['GET', 'POST'])
def delete():

    print('DELETE BUTTON WORKING')
    print(request.data)

    database = models.Assessment.query.all()
    return render_template("banner_templates/all.html", database = database)


@app.route('/completed')
def completed():
    database = models.Assessment.query.filter_by(completed = True).all()
    return render_template("banner_templates/completed.html", database = database)

@app.route('/uncompleted')
def uncompleted():
        database = models.Assessment.query.filter_by(completed = False).all()
        return render_template("banner_templates/uncompleted.html", database = database)

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
