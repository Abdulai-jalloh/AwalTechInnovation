from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from sqlalchemy.dialects.sqlite import JSON
#Land Information
db = SQLAlchemy()
class Land(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  location = db.Column(db.String(150), nullable=False)
  price = db.Column(db.Numeric(10, 2), nullable=False)
  description = db.Column(db.Text)
  mainImage = db.Column(db.String(255))
  gallery = db.Column(db.PickleType)
  features = db.Column(db.PickleType)
  status = db.Column(db.String(50), default='Available')

    # Owner Personal Information
  name = db.Column(db.String(100))
  email = db.Column(db.String(100))
  phone = db.Column(db.String(50))

  date_Added = db.Column(db.DateTime, default=datetime.utcnow)

  latitude = db.Column(db.Numeric(9, 6))
  longitude = db.Column(db.Numeric(9, 6))
  visible = db.Column(db.Boolean, default=True)

  sales = db.relationship('Sale', backref='land', cascade="all, delete", lazy=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    land_id = db.Column(db.Integer, db.ForeignKey('land.id'), nullable=False)
    buyerName = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    sale_date = db.Column(db.Date)
    documents = db.Column(db.String(200))

 