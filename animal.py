from database import db
import json

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    species = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)

    weight = db.Column(db.Float, nullable=False)
    height = db.Column(db.Float, nullable=False)
    health = db.Column(db.String, nullable=False)
    color = db.Column(db.String, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)
    sold_date = db.Column(db.Date, nullable=True)
    supplier = db.Column(db.String, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    diet = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)

    def set_diet(self, data):
        self.diet = json.dumps(data)

    def get_diet(self):
        return json.loads(self.diet)