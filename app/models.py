from app import db
from sqlalchemy.dialects.postgresql import ARRAY

class answ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    buy = db.Column(db.Text)