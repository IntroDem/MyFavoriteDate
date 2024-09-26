from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ImportantDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    details = db.Column(db.Text, nullable=True)

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey('important_date.id'), nullable=False)
    notification_time = db.Column(db.DateTime, nullable=False)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Integer, db.ForeignKey('important_date.id'), nullable=False)
    photo_path = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=True)