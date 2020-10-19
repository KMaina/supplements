import datetime
from .. import db

class Blog(db.Model):
    """ BLog Model for storing blog related details """
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    body = db.Column(db.String(5000), unique=True, nullable=False)
    published_on = db.Column(db.DateTime, nullable=False)
