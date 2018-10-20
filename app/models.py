from app import db

class answ(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Lastpos = db.Column(db.Integer)
    Buy = db.Column(db.Text)
    Buych = db.Column(db.Text)
    Sell = db.Column(db.Text)
    Sellch = db.Column(db.Text)
    Stop = db.Column(db.Text)
    Lasttime = db.Column(db.Integer)