from flask import render_template
from app import app 
from .forms import TextForm

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/all')
def all():
    return render_template("banner_templates/all.html")

@app.route('/completed')
def completed():
    return render_template("banner_templates/completed.html")

@app.route('/uncompleted')
def uncompleted():
    return render_template("banner_templates/uncompleted.html")

@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = TextForm()
    return render_template("banner_templates/add.html", 
    title = 'Add an assessment', form = form)


# Each individual route refers to a new page 
# i.e. www.google.com/XXXX
