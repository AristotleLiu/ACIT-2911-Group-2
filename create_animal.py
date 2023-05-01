from app import app, db
from animal import Animal
import datetime



with app.app_context():
    obj = Animal(
        id = 1,             # int
        name = "Timothy",   # str
        age = 1,            # int
        gender = "Female",  # int
        species = "Goat",   # str
        price = 250,        # int

        weight = 5,         # int
        height = 1,         # int
        health = "good"     # str
        color = "white"     # str
        purchase_date = datetime.datetime(2020, 5, 17)
        sold_date = datetime.datetime(2020, 5, 17)
        supplier = "tim@gmail.com"
        purchase_price = 50,
        diet = {"type":"Herbivore", "foods":["Grass", "Hay"]}
        notes = "Has a chipped tooth!"
    )
    db.session.add(obj)
    db.session.commit()
