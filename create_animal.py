from app import app, db
from animal import Animal
from dates import string_to_date

with app.app_context():
    obj = Animal(
        id = 1,
        name = "Timothy",
        age = 1,
        gender = "Female",
        species = "Goat",
        price = 250,

        weight = 5,
        height = 1,
        health = "good",
        color = "white",
        purchase_date = string_to_date("2020-5-17"),
        sold_date = string_to_date("2020-5-17"),
        supplier = "tim@gmail.com",
        purchase_price = 50.0,
        diet = '{"type":"Herbivore", "foods":["Grass", "Hay"]}',
        notes = "Has a chipped tooth!"
    )
    print("Object made")

    db.session.add(obj)
    print("Object added")
    
    db.session.commit()
