from database import db
from datetime import datetime


class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String(200), unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    mimetype = db.Column(db.Text, nullable=False)