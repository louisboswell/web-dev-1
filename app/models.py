from app import db

class Assessment(db.Model):
    name = db.Column(db.String(20), primary_key = True)
    module = db.Column(db.String(20), index = True)
    date = db.Column(db.DateTime)
    description = db.Column(db.String(500), index = True)
    completed = db.Column(db.Boolean)