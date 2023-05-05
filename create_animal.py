from app import app, db
from animal import Animal
from dates import string_to_date

with app.app_context():
    animal_objs = [Animal(
        id = 1,
        name = "Timothy",
        age = 1,
        gender = "female",
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
        gender = "male",
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
        gender = "female",
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
        gender = "male",
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
        gender = "female",
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
        gender = "male",
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
        gender = "male",
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
        gender = "male",
        species = "Guinea Pig",
        price = 70,
        weight = 1,
        height = 0.2,
        health = "poor",
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
        gender = "male",
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
        gender = "female",
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
        gender = "female",
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
        ),

        Animal(
        name = "Fluffy",
        age = 2,
        gender = "female",
        species = "Rabbit",
        price = 100,
        weight = 2.5,
        height = 0.3,
        health = "good",
        color = "white",
        purchase_date = string_to_date("2022-01-10"),
        sold_date = string_to_date("2022-04-05"),
        supplier = "johndoe@localpetstore.com",
        purchase_price = 75.0,
        diet = '{"type":"Herbivore", "foods":["Pellets", "Vegetables"]}',
        notes = "Loves to chew on cardboard boxes."
        ),

        Animal(
        name = "Simba",
        age = 3,
        gender = "male",
        species = "Lion",
        price = 5000,
        weight = 200,
        height = 1.2,
        health = "excellent",
        color = "golden",
        purchase_date = string_to_date("2022-02-20"),
        sold_date = string_to_date("2022-06-10"),
        supplier = "safariadventures@gmail.com",
        purchase_price = 4000.0,
        diet = '{"type":"Carnivore", "foods":["Meat", "Bone"]}',
        notes = "Requires a large enclosure with plenty of space to roam."
        ),

        Animal(
        name = "Coco",
        age = 1,
        gender = "female",
        species = "Polar Bear",
        price = 10000,
        weight = 900,
        height = 2.5,
        health = "good",
        color = "brown",
        purchase_date = string_to_date("2022-03-01"),
        sold_date = string_to_date("2022-05-25"),
        supplier = "ivan@localpetstore.com",
        purchase_price = 2500.0,
        diet = '{"type":"Omnivore", "foods":["Kibble", "Meat", "Fish"]}',
        notes = "Loves to play fetch."
        ),

        Animal(
        name = "Zeus",
        age = 5,
        gender = "male",
        species = "Horse",
        price = 8000,
        weight = 600,
        height = 1.8,
        health = "excellent",
        color = "black",
        purchase_date = string_to_date("2022-04-15"),
        sold_date = string_to_date("2022-06-30"),
        supplier = "smithfarms@hotmail.com",
        purchase_price = 6000.0,
        diet = '{"type":"Herbivore", "foods":["Hay", "Grass"]}',
        notes = "Requires regular grooming and exercise."
        ),

        Animal(
        name = "Kiki",
        age = 1,
        gender = "female",
        species = "Dodo Bird",
        price = 25000,
        weight = 4,
        height = 0.3,
        health = "good",
        color = "gray",
        purchase_date = string_to_date("2022-05-01"),
        sold_date = string_to_date("2022-07-15"),
        supplier = "petshelter@gmail.com",
        purchase_price = 200.0,
        diet = '{"type":"Omnivore", "foods":["Kibble", "Fish"]}',
        notes = "Likes to nap in cozy spots."
        ),

        Animal(
        name = "Ziggy",
        age = 2,
        gender = "hermaphrodite",
        species = "Snail",
        price = 20,
        weight = 0.01,
        height = 0.001,
        health = "good",
        color = "brown",
        purchase_date = string_to_date("2023-01-01"),
        sold_date = string_to_date("2023-02-14"),
        supplier = "alice@snailfarmer.com",
        purchase_price = 10.0,
        diet = '{"type":"Herbivore", "foods":["Lettuce", "Carrots"]}',
        notes = "Likes to hide in its shell."
        ),

        Animal(
        name = "Kiki",
        age = 2,
        gender = "female",
        species = "Parrot",
        price = 500,
        weight = 0.5,
        height = 0.3,
        health = "good",
        color = "red and green",
        purchase_date = string_to_date("2022-01-10"),
        sold_date = string_to_date("2022-02-14"),
        supplier = "exoticpets@zoo.com",
        purchase_price = 300.0,
        diet = '{"type":"Omnivore", "foods":["Seeds", "Fruit", "Insects"]}',
        notes = "Loves to mimic human speech."
        ),

        Animal(
        name = "Ziggy",
        age = 5,
        gender = "male",
        species = "Chameleon",
        price = 350,
        weight = 0.1,
        height = 0.2,
        health = "excellent",
        color = "green and blue",
        purchase_date = string_to_date("2022-02-23"),
        sold_date = string_to_date("2022-04-15"),
        supplier = "junglecreatures@gmail.com",
        purchase_price = 250.0,
        diet = '{"type":"Insectivore", "foods":["Crickets", "Mealworms"]}',
        notes = "Can change color to blend in with surroundings."
        ),

        Animal(
        name = "Gus",
        age = 3,
        gender = "male",
        species = "Toucan",
        price = 800,
        weight = 0.5,
        height = 0.4,
        health = "good",
        color = "black, white, and yellow",
        purchase_date = string_to_date("2022-04-10"),
        sold_date = string_to_date("2022-05-15"),
        supplier = "rainforestaviary@birdlovers.com",
        purchase_price = 500.0,
        diet = '{"type":"Frugivore", "foods":["Fruit"]}',
        notes = "Has a loud, distinctive call."
        ),

        Animal(
        name = "Simba",
        age = 1,
        gender = "male",
        species = "Cheetah",
        price = 1500,
        weight = 50,
        height = 0.9,
        health = "excellent",
        color = "golden",
        purchase_date = string_to_date("2022-03-01"),
        sold_date = string_to_date("2022-04-30"),
        supplier = "africanwildlife@conservation.org",
        purchase_price = 1000.0,
        diet = '{"type":"Carnivore", "foods":["Meat"]}',
        notes = "Extremely fast runner."
        ),

        Animal(
        name = "Zara",
        age = 2,
        gender = "female",
        species = "Turtle",
        price = 20,
        weight = 5,
        height = 0.3,
        health = "critical",
        color = "brown",
        purchase_date = string_to_date("2022-05-01"),
        sold_date = string_to_date("2022-06-10"),
        supplier = "exoticpetshop@aquatics.com",
        purchase_price = 100.0,
        diet = '{"type":"Herbivore", "foods":["Vegetables", "Fruit"]}',
        notes = "Extremely slow runner."
        ),

        Animal(
        name = "Kiki",
        age = 5,
        gender = "hermaphrodite",
        species = "Frog",
        price = 50,
        weight = 0.5,
        height = 0.05,
        health = "excellent",
        color = "green",
        purchase_date = string_to_date("2022-11-15"),
        sold_date = string_to_date("2023-03-01"),
        supplier = "bob@frogbreeder.com",
        purchase_price = 30.0,
        diet = '{"type":"Carnivore", "foods":["Insects", "Worms"]}',
        notes = "Can jump really high!"
        ),

        Animal(
        name = "Wally",
        age = 7,
        gender = "male",
        species = "Walrus",
        price = 10000,
        weight = 1200,
        height = 1.5,
        health = "good",
        color = "brown",
        purchase_date = string_to_date("2023-02-01"),
        sold_date = string_to_date("2023-05-01"),
        supplier = "walrusworld@marinepark.com",
        purchase_price = 8000.0,
        diet = '{"type":"Carnivore", "foods":["Fish", "Squid"]}',
        notes = "Loves to swim and play with toys."
        ),

        Animal(
        name = "Wilma",
        age = 5,
        gender = "female",
        species = "Walrus",
        price = 9000,
        weight = 1100,
        height = 1.4,
        health = "fair",
        color = "gray",
        purchase_date = string_to_date("2022-11-15"),
        sold_date = string_to_date("2023-04-01"),
        supplier = "walrusworld@marinepark.com",
        purchase_price = 7500.0,
        diet = '{"type":"Carnivore", "foods":["Fish", "Squid"]}',
        notes = "Enjoys playing with Wally, the male Walrus."
        ),
    ]

    for obj in animal_objs:
        db.session.add(obj)
        print("+", end='')
    print()
    db.session.commit()
