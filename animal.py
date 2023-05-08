from database import db
import json

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
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

    image_url = db.Column(db.String, nullable=True)

    def set_diet(self, data):
        self.diet = json.dumps(data)

    def get_diet(self):
        return json.loads(self.diet)
    
    def to_dict(self):
        animal_dict = {"id" : self.id,
            "name" : self.name,
            "age" : self.age,
            "gender" : self.gender,
            "species" : self.species,
            "price" : self.price,

            "weight" : self.weight,
            "height" : self.height,
            "health" : self.health,
            "color" : self.color,
            "purchase_date" : self.purchase_date,
            "sold_date" : self.sold_date,
            "supplier" : self.supplier,
            "purchase_price" : self.purchase_price,
            "diet" : self.get_diet(),
            "notes" : self.notes,
            "image_url" : self.image_url
        }
        return animal_dict