from app import app, db
from animal import Animal
from dates import string_to_date

with app.app_context():
    animal_objs = [Animal(
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
        ),

        Animal(
        name = "Buddy",
        age = 3,
        gender = "Male",
        species = "Dog",
        price = 500,
        weight = 20,
        height = 2,
        health = "excellent",
        color = "brown",
        purchase_date = string_to_date("2022-01-01"),
        sold_date = string_to_date("2022-03-01"),
        supplier = "bobby@petstore.com",
        purchase_price = 350.0,
        diet = '{"type":"Omnivore", "foods":["Meat", "Vegetables"]}',
        notes = "Loves to play fetch!"
        ),

        Animal(
        name = "Whiskers",
        age = 2,
        gender = "Female",
        species = "Cat",
        price = 300,
        weight = 10,
        height = 1.5,
        health = "good",
        color = "gray",
        purchase_date = string_to_date("2022-02-14"),
        sold_date = string_to_date("2022-03-01"),
        supplier = "fred@craigslist.org",
        purchase_price = 200.0,
        diet = '{"type":"Carnivore", "foods":["Fish", "Meat"]}',
        notes = "Likes to sleep in sunbeams."
        ),

        Animal(
        name = "Hank",
        age = 5,
        gender = "Male",
        species = "Horse",
        price = 1500,
        weight = 800,
        height = 5,
        health = "fair",
        color = "brown",
        purchase_date = string_to_date("2021-07-10"),
        sold_date = string_to_date("2022-01-15"),
        supplier = "harry@horsebreeder.com",
        purchase_price = 1000.0,
        diet = '{"type":"Herbivore", "foods":["Hay", "Grass"]}',
        notes = "Needs regular hoof care."
        ),

        Animal(
        name = "Samantha",
        age = 4,
        gender = "Female",
        species = "Rabbit",
        price = 100,
        weight = 3,
        height = 0.5,
        health = "excellent",
        color = "white",
        purchase_date = string_to_date("2022-03-20"),
        sold_date = string_to_date("2023-03-20"),
        supplier = "ivan@localpetstore.com",
        purchase_price = 75.0,
        diet = '{"type":"Herbivore", "foods":["Carrots", "Lettuce"]}',
        notes = "Loves to hop around and play."
        ),

        Animal(
        name = "Max",
        age = 6,
        gender = "Male",
        species = "Parrot",
        price = 200,
        weight = 1,
        height = 0.5,
        health = "good",
        color = "green",
        purchase_date = string_to_date("2022-04-05"),
        sold_date = string_to_date("2022-05-05"),
        supplier = "tyler@exoticbirds.com",
        purchase_price = 150.0,
        diet = '{"type":"Omnivore", "foods":["Seeds", "Fruit"]}',
        notes = "Loves to mimic human speech."
        ),

        Animal(
        name = "Rocky",
        age = 2,
        gender = "Male",
        species = "Hamster",
        price = 50,
        weight = 0.2,
        height = 0.1,
        health = "fair",
        color = "brown",
        purchase_date = string_to_date("2021-11-11"),
        sold_date = string_to_date("2022-01-02"),
        supplier = "ivan@localpetstore.com",
        purchase_price = 30.0,
        diet = '{"type":"Omnivore", "foods":["Seeds", "Vegetables"]}',
        notes = "Likes to run on its wheel."
        ),

        Animal(
        name = "Leo",
        age = 1,
        gender = "Male",
        species = "Guinea Pig",
        price = 70,
        weight = 1,
        height = 0.2,
        health = "good",
        color = "black and white",
        purchase_date = string_to_date("2022-02-15"),
        sold_date = string_to_date("2022-04-01"),
        supplier = "ivan@localpetstore.com",
        purchase_price = 50.0,
        diet = '{"type":"Herbivore", "foods":["Hay", "Vegetables"]}',
        notes = "Enjoys being held and cuddled."
        ),

        Animal(
        name = "Milo",
        age = 4,
        gender = "Male",
        species = "Snake",
        price = 200,
        weight = 1,
        height = 0.2,
        health = "excellent",
        color = "yellow and black",
        purchase_date = string_to_date("2022-03-15"),
        sold_date = string_to_date("2022-05-01"),
        supplier = "justin@reptilebreeder.com",
        purchase_price = 150.0,
        diet = '{"type":"Carnivore", "foods":["Mice", "Rats"]}',
        notes = "Needs a heat lamp to stay warm."
        ),

        Animal(
        name = "Lola",
        age = 3,
        gender = "Female",
        species = "Ferret",
        price = 100,
        weight = 0.5,
        height = 0.2,
        health = "good",
        color = "brown",
        purchase_date = string_to_date("2022-04-20"),
        sold_date = string_to_date("2022-06-01"),
        supplier = "ivan@localpetstore.com",
        purchase_price = 80.0,
        diet = '{"type":"Carnivore", "foods":["Meat", "Eggs"]}',
        notes = "Loves to play with toys."
        ),
        
        Animal(
        name = "Viktor",
        age = 3,
        gender = "Female",
        species = "Bobcat",
        price = 100,
        weight = 0.5,
        height = 0.2,
        health = "poor",
        color = "brown",
        purchase_date = string_to_date("2022-04-20"),
        sold_date = string_to_date("2022-06-01"),
        supplier = "tyler@exoticbirds.com",
        purchase_price = 80.0,
        diet = '{"type":"Carnivore", "foods":["Meat", "Eggs"]}',
        notes = "Loves to play with toys."
        )
    ]

    for obj in animal_objs:
        db.session.add(obj)
        print("+", end='')
    print()
    db.session.commit()
