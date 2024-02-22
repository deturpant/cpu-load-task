from datetime import datetime

from app.store.database.models import db


class CPULoad(db.Model):
    __tablename__ = 'cpu_load'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    value = db.Column(db.Float, nullable=False)


class Log(db.Model):
    __tablename__ = 'log'

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    status = db.Column(db.String(), nullable=False)
