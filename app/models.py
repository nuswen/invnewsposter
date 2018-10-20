from app import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buy = db.Column(db.Text)