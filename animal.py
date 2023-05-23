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
    sold_date = db.Column(db.Date, nullable=True, default=None)
    supplier = db.Column(db.String, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    diet = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)

    image_url = db.Column(db.String, nullable=True)
    
    is_in_invoice = db.Column(db.Boolean, default=False)

    # def set_diet(self, data):
    #     self.diet = json.dumps(data)

    # def get_diet(self):
    #     return json.loads(self.diet)
    
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
            "diet" : self.diet,
            "notes" : self.notes,
            "image_url" : self.image_url,
            "is_in_invoice" : self.is_in_invoice
        }
        return animal_dict
    

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String, nullable=False)
    province = db.Column(db.String, nullable=False)
    postal_code = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    street = db.Column(db.String, nullable=False)

    animals = db.relationship('AnimalInvoice', back_populates='invoice')

    def to_dict(self):
        order_dict = {
            "id": self.id,
            "status": self.status,
            "date": self.date,
            "name": self.name,
            "city": self.city,
            "province": self.province,
            "postal_code": self.postal_code,
            "phone": self.phone,
            "street": self.street,
            "animals":[], 
            "price":0
        }
        for item in self.animals:
            order_dict["animals"].append({"animal_id":item.animal_id, "animal_name":item.animal.name, "animal_species":item.animal.species,"animal_price":item.animal.price})
            order_dict["price"] += item.animal.price
        return order_dict


class AnimalInvoice(db.Model):
    animal_id = db.Column(db.ForeignKey("animal.id"), primary_key=True)
    invoice_id = db.Column(db.ForeignKey("invoice.id"), primary_key=True)

    animal = db.relationship('Animal')
    invoice = db.relationship('Invoice', back_populates='animals')