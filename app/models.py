from app import db

class answ(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Buy = db.Column(db.Text)