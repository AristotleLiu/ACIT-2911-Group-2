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
        notes = "Has a chipped tooth!",
        image_url = "https://pethelpful.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cg_xy_center%2Cq_auto:eco%2Cw_1200%2Cx_1281%2Cy_628/MTg5NzA4MjI3MTEyMzQ3NDAx/trac-vu-yzzn7zgjnqs-unsplash.jpg"
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
        notes = "Loves to play fetch!",
        image_url = "https://images.unsplash.com/photo-1558788353-f76d92427f16?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzN8fGRvZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Likes to sleep in sunbeams.",
        image_url = "https://images.unsplash.com/photo-1533738363-b7f9aef128ce?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Needs regular hoof care.",
        image_url = "https://images.unsplash.com/photo-1576289163370-0634b5d94d28?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=774&q=80"
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
        notes = "Loves to hop around and play.",
        image_url = "https://images.unsplash.com/photo-1591382386627-349b692688ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8cmFiYml0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to mimic human speech.",
        image_url = "https://images.unsplash.com/photo-1596044574113-bd6dc59e6337?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fFBhcnJvdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Likes to run on its wheel.",
        image_url = "https://images.unsplash.com/photo-1599154820236-ebe408351213?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fEhhbXN0ZXJ8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60"
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
        notes = "Enjoys being held and cuddled.",
        image_url = "https://images.unsplash.com/photo-1630173207885-c903abb963f6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1180&q=80"
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
        notes = "Needs a heat lamp to stay warm.",
        image_url = "https://images.unsplash.com/photo-1531386151447-fd76ad50012f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8c25ha2V8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to play with toys.",
        image_url = "https://images.unsplash.com/photo-1615087240969-eeff2fa558f2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8RmVycmV0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to play with toys.",
        image_url = "https://images.unsplash.com/photo-1605235923175-9930bcad51df?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Qm9iY2F0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to chew on cardboard boxes.",
        image_url = "https://images.unsplash.com/photo-1591382386627-349b692688ff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8UmFiYml0fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Requires a large enclosure with plenty of space to roam.",
        image_url = "https://images.unsplash.com/photo-1607490703747-0519d2e398a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDF8fGxpb258ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to play fetch.",
        image_url = "https://images.unsplash.com/photo-1546712508-dacd722e76e8?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fHBvbGFyJTIwYmVhcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Requires regular grooming and exercise.",
        image_url = "https://images.unsplash.com/photo-1576289163370-0634b5d94d28?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDF8fGhvcnNlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
        ),

        Animal(
        name = "Kiki",
        age = 1,
        gender = "female",
        species = "Dodo Bird",
        price = 25000,
        weight = 4,
        height = 0.3,
        health = "critical",
        color = "gray",
        purchase_date = string_to_date("2022-05-01"),
        sold_date = string_to_date("2022-07-15"),
        supplier = "petshelter@gmail.com",
        purchase_price = 200.0,
        diet = '{"type":"Omnivore", "foods":["Kibble", "Fish"]}',
        notes = "Likes to nap in cozy spots.",
        image_url = "https://images.unsplash.com/photo-1667286266878-e0c40979c220?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8RG9kbyUyMEJpcmR8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60"
        ),

        Animal(
        name = "Ziggy",
        age = 2,
        gender = "hermaphrodite",
        species = "Snail",
        price = 20,
        weight = 0.01,
        height = 0.01,
        health = "good",
        color = "brown",
        purchase_date = string_to_date("2023-01-01"),
        sold_date = string_to_date("2023-02-14"),
        supplier = "alice@snailfarmer.com",
        purchase_price = 10.0,
        diet = '{"type":"Herbivore", "foods":["Lettuce", "Carrots"]}',
        notes = "Likes to hide in its shell.",
        image_url = "https://images.unsplash.com/photo-1563662185892-fe39abf9ba9e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8U25haWx8ZW58MHx8MHx8&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to mimic human speech.",
        image_url = "https://images.unsplash.com/photo-1596044574113-bd6dc59e6337?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fFBhcnJvdHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Can change color to blend in with surroundings.",
        image_url = "https://images.unsplash.com/photo-1598904396634-9a630c4fd8c0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzR8fENoYW1lbGVvbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Has a loud, distinctive call.",
        image_url = "https://images.unsplash.com/photo-1595363530143-b913b4ea30dd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8VG91Y2FufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Extremely fast runner.",
        image_url = "https://images.unsplash.com/photo-1582425312148-de9955e68e45?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Q2hlZXRhaHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Extremely slow runner.",
        image_url = "https://images.unsplash.com/photo-1572713629470-3e9f5d4fdf4c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8VHVydGxlfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Can jump really high!",
        image_url = "https://images.unsplash.com/photo-1579380656108-f98e4df8ea62?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8ZnJvZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=800&q=60"
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
        notes = "Loves to swim and play with toys.",
        image_url = "https://i.natgeofe.com/k/60108d62-2d04-478e-bb79-3f3549ffd13e/walrus-tusks_4x3.jpg"
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
        notes = "Enjoys playing with Wally, the male Walrus.",
        image_url = "https://images.unsplash.com/photo-1627477150479-b7f109c3aaa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1548&q=80"
        ),

        Animal(
        name="Mila",
        age=3,
        gender="female",
        species="Tiger",
        price=12000,
        weight=180,
        height=1.1,
        health="excellent",
        color="orange and black",
        purchase_date=string_to_date("2022-09-10"),
        sold_date=string_to_date("2023-01-05"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=9000.0,
        diet='{"type":"Carnivore", "foods":["Meat", "Bone"]}',
        notes="Has beautiful stripes.",
        image_url="https://images.unsplash.com/photo-1615963244664-5b845b2025ee?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1064&q=80"
        ),

        Animal(
        name="Kiara",
        age=2,
        gender="female",
        species="Flamingo",
        price=800,
        weight=3,
        height=1.2,
        health="good",
        color="pink",
        purchase_date=string_to_date("2023-03-20"),
        sold_date=string_to_date("2023-05-10"),
        supplier="exoticbirds@aviary.com",
        purchase_price=600.0,
        diet='{"type":"Omnivore", "foods":["Shrimp", "Algae"]}',
        notes="Has long legs.",
        image_url="https://images.unsplash.com/photo-1539418561314-565804e349c0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
        ),

        Animal(
        name="Nala",
        age=4,
        gender="female",
        species="Lemur",
        price=6000,
        weight=2,
        height=0.6,
        health="excellent",
        color="gray and white",
        purchase_date=string_to_date("2022-07-15"),
        sold_date=string_to_date("2022-10-10"),
        supplier="wildsafaripark@wildlifeconservation.org",
        purchase_price=4500.0,
        diet='{"type":"Herbivore", "foods":["Fruits", "Leaves"]}',
        notes="Has a long tail.",
        image_url="https://images.unsplash.com/photo-1599639668421-eefd062fe657?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8TGVtdXJ8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Simba",
        age=4,
        gender="male",
        species="Lion",
        price=10000,
        weight=200,
        height=1.3,
        health="excellent",
        color="golden",
        purchase_date=string_to_date("2022-10-10"),
        sold_date=string_to_date("2023-03-01"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=8000.0,
        diet='{"type":"Carnivore", "foods":["Meat", "Bone"]}',
        notes="Has a majestic mane.",
        image_url="https://images.unsplash.com/photo-1552410260-0fd9b577afa6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8TGlvbnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Luna",
        age=3,
        gender="female",
        species="Cheetah",
        price=9000,
        weight=120,
        height=0.9,
        health="good",
        color="yellow and black",
        purchase_date=string_to_date("2022-12-05"),
        sold_date=string_to_date("2023-02-15"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=7000.0,
        diet='{"type":"Carnivore", "foods":["Meat", "Bone"]}',
        notes="Runs at high speeds.",
        image_url="https://images.unsplash.com/photo-1538100951519-36a3de1136c6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8Q2hlZXRhaHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Coco",
        age=2,
        gender="female",
        species="Orangutan",
        price=2500,
        weight=100,
        height=1.5,
        health="good",
        color="brown",
        purchase_date=string_to_date("2023-01-15"),
        sold_date=string_to_date("2023-03-20"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=2000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Nuts"]}',
        notes="Swings from trees.",
        image_url="https://images.unsplash.com/photo-1641697975041-b5f967d3a4b9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8b3Jhbmd1dGFuZ3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Ruby",
        age=2,
        gender="female",
        species="Parrot",
        price=200,
        weight=0.3,
        height=0.2,
        health="critical",
        color="red",
        purchase_date=string_to_date("2023-02-20"),
        sold_date=string_to_date("2023-04-10"),
        supplier="exoticbirds@aviary.com",
        purchase_price=400.0,
        diet='{"type":"Herbivore", "foods":["Seeds", "Fruits"]}',
        notes="Has vibrant feathers.",
        image_url="https://images.unsplash.com/photo-1592089416462-2b0cb7da8379?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8UGFycm90fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Kai",
        age=4,
        gender="male",
        species="Elephant",
        price=15000,
        weight=3000,
        height=2.5,
        health="excellent",
        color="gray",
        purchase_date=string_to_date("2022-11-10"),
        sold_date=string_to_date("2023-05-01"),
        supplier="wildsafaripark@wildlifeconservation.org",
        purchase_price=12000.0,
        diet='{"type":"Herbivore", "foods":["Leaves", "Grass"]}',
        notes="Has long tusks.",
        image_url="https://images.unsplash.com/photo-1619111712102-8273abfea0aa?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fGVsZXBoYW50fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Funnyman",
        age=3,
        gender="female",
        species="Zebra",
        price=4000,
        weight=350,
        height=1.2,
        health="good",
        color="black and white",
        purchase_date=string_to_date("2022-09-20"),
        sold_date=string_to_date("2022-12-10"),
        supplier="wildsafaripark@wildlifeconservation.org",
        purchase_price=3000.0,
        diet='{"type":"Herbivore", "foods":["Grass", "Leaves"]}',
        notes="Has stripes.",
        image_url="https://images.unsplash.com/photo-1574145967029-52f4cd6b7e76?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8WmVicmF8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Al",
        age=6,
        gender="male",
        species="Gorilla",
        price=12000,
        weight=250,
        height=1.5,
        health="fine",
        color="black",
        purchase_date=string_to_date("2022-08-15"),
        sold_date=string_to_date("2023-02-05"),
        supplier="wildsafaripark@wildlifeconservation.org",
        purchase_price=9000.0,
        diet='{"type":"Herbivore", "foods":["Fruits", "Vegetables"]}',
        notes="Has a muscular build.",
        image_url="https://images.unsplash.com/photo-1581252789066-5110779bda1b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8Z29yaWxsYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Spike",
        age=1,
        gender="male",
        species="Hedgehog",
        price=200,
        weight=0.3,
        height=0.1,
        health="good",
        color="brown",
        purchase_date=string_to_date("2023-03-10"),
        sold_date=string_to_date("2023-04-25"),
        supplier="exoticpets@petstore.com",
        purchase_price=150.0,
        diet='{"type":"Omnivore", "foods":["Insects", "Fruits", "Vegetables"]}',
        notes="Has prickly spines.",
        image_url="https://images.unsplash.com/photo-1605369179814-cfc635981c03?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8aGVkZ2Vob2d8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Ziggy",
        age=2,
        gender="female",
        species="Kangaroo",
        price=6000,
        weight=50,
        height=1.2,
        health="poor",
        color="brown",
        purchase_date=string_to_date("2022-10-05"),
        sold_date=string_to_date("2023-01-20"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=4500.0,
        diet='{"type":"Herbivore", "foods":["Grass", "Leaves"]}',
        notes="Has a pouch.",
        image_url="https://images.unsplash.com/photo-1626803111824-0ee594987d4b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=987&q=80"
        ),

        Animal(
        name="Nico",
        age=3,
        gender="male",
        species="Koala",
        price=5000,
        weight=12,
        height=0.6,
        health="fine",
        color="gray and white",
        purchase_date=string_to_date("2022-12-15"),
        sold_date=string_to_date("2023-03-01"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=4000.0,
        diet='{"type":"Herbivore", "foods":["Eucalyptus Leaves"]}',
        notes="Sleeps for long hours.",
        image_url="https://images.unsplash.com/photo-1579972383667-4894c883d674?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8S29hbGF8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Max",
        age=6,
        gender="male",
        species="Chimpanzee",
        price=8000,
        weight=60,
        height=0.9,
        health="good",
        color="brown",
        purchase_date=string_to_date("2022-09-10"),
        sold_date=string_to_date("2023-01-01"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=6000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Highly intelligent.",
        image_url="https://images.unsplash.com/photo-1596037332135-309f79d22d16?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1030&q=80"
        ),

        Animal(
        name="Lily",
        age=3,
        gender="female",
        species="Gibbon",
        price=5000,
        weight=8,
        height=0.6,
        health="good",
        color="black",
        purchase_date=string_to_date("2023-01-05"),
        sold_date=string_to_date("2023-03-20"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=4000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Leaves"]}',
        notes="Swings from branches.",
        image_url="https://images.unsplash.com/photo-1565899629718-4dae0e9566bd?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8R2liYm9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Charlie",
        age=4,
        gender="male",
        species="Orangutan",
        price=9000,
        weight=80,
        height=1.2,
        health="excellent",
        color="red",
        purchase_date=string_to_date("2022-11-15"),
        sold_date=string_to_date("2023-04-01"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=7000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Has long arms.",
        image_url="https://images.unsplash.com/photo-1583753341245-5175f6acfe38?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8T3Jhbmd1dGFufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Mia",
        age=2,
        gender="female",
        species="Baboon",
        price=3000,
        weight=30,
        height=0.7,
        health="good",
        color="gray",
        purchase_date=string_to_date("2023-02-20"),
        sold_date=string_to_date("2023-04-10"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=2000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Distinctive face features.",
        image_url="https://images.unsplash.com/photo-1605583956585-c749b5d92c9d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8QmFib29ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Leo",
        age=5,
        gender="male",
        species="Gorilla",
        price=10000,
        weight=180,
        height=1.5,
        health="excellent",
        color="black",
        purchase_date=string_to_date("2022-10-10"),
        sold_date=string_to_date("2023-03-01"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=8000.0,
        diet='{"type":"Herbivore", "foods":["Leaves", "Fruits"]}',
        notes="Large and powerful.",
        image_url="https://images.unsplash.com/photo-1541804536-78217d100fb7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8R29yaWxsYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Sophie",
        age=3,
        gender="female",
        species="Bonobo",
        price=7000,
        weight=45,
        height=0.9,
        health="good",
        color="black",
        purchase_date=string_to_date("2022-12-05"),
        sold_date=string_to_date("2023-02-15"),
        supplier="exoticwildlife@zoo.com",
        purchase_price=5000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Known for social behavior.",
        image_url="https://images.unsplash.com/photo-1598723588279-90d2cd2b2808?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8Qm9ub2JvfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Oscar",
        age=14,
        gender="male",
        species="Marmoset",
        price=1500,
        weight=0.4,
        height=0.2,
        health="good",
        color="white",
        purchase_date=string_to_date("2023-03-10"),
        sold_date=string_to_date("2023-04-25"),
        supplier="exoticpets@petstore.com",
        purchase_price=1000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Small and agile.",
        image_url="https://images.unsplash.com/photo-1675870832679-e5f1acee5265?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8TWFybW9zZXR8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Folk",
        age=2,
        gender="male",
        species="Tamarin",
        price=2000,
        weight=0.5,
        height=0.3,
        health="good",
        color="brown",
        purchase_date=string_to_date("2022-11-20"),
        sold_date=string_to_date("2023-01-15"),
        supplier="exoticpets@petstore.com",
        purchase_price=1500.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Has long tail hair.",
        image_url="https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTACV7Utt2IN_4tiz5ftNPdRFGTQ_UCIH8_Q7g_UlJnCqZtoDc29kTL5XCCWlbuvW-8X8hIFx0eJstEB6Y"
        ),

        Animal(
        name="Theodore",
        age=5,
        gender="female",
        species="Squirrel Monkey",
        price=2500,
        weight=0.6,
        height=0.3,
        health="good",
        color="brown",
        purchase_date=string_to_date("2022-10-15"),
        sold_date=string_to_date("2023-02-01"),
        supplier="exoticpets@petstore.com",
        purchase_price=2000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Active and agile.",
        image_url="https://images.unsplash.com/photo-1515444347446-4380c4d8a6ed?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8U3F1aXJyZWwlMjBNb25rZXl8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Vladimir",
        age=2,
        gender="male",
        species="Cebidae",
        price=5000,
        weight=15,
        height=0.8,
        health="good",
        color="black",
        purchase_date=string_to_date("2022-12-01"),
        sold_date=string_to_date("2023-03-10"),
        supplier="exoticpets@petstore.com",
        purchase_price=4000.0,
        diet='{"type":"Omnivore", "foods":["Fruits", "Insects"]}',
        notes="Long arms and fingers.",
        image_url="https://upload.wikimedia.org/wikipedia/commons/4/40/Capuchin_Costa_Rica.jpg"
        ),

        Animal(
        name="Charlie",
        age=6,
        gender="male",
        species="Shoebill Stork",
        price=5000,
        weight=6,
        height=1.3,
        health="good",
        color="gray",
        purchase_date=string_to_date("2022-09-20"),
        sold_date=string_to_date("2023-01-10"),
        supplier="exoticbirds@birdsanctuary.com",
        purchase_price=4000.0,
        diet='{"type":"Carnivore", "foods":["Fish", "Frogs"]}',
        notes="Has a distinctive bill.",
        image_url="https://images.unsplash.com/photo-1563188619-df4bb332ad8d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1011&q=80"
        ),

        Animal(
        name="Greta",
        age=4,
        gender="female",
        species="Shoebill Stork",
        price=6000,
        weight=5.5,
        height=1.2,
        health="good",
        color="gray",
        purchase_date=string_to_date("2022-12-15"),
        sold_date=string_to_date("2023-03-01"),
        supplier="exoticbirds@birdsanctuary.com",
        purchase_price=4500.0,
        diet='{"type":"Carnivore", "foods":["Fish", "Reptiles"]}',
        notes="Large and majestic bird.",
        image_url="https://images.unsplash.com/photo-1601617637993-f9f976d7b305?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8c2hvZWJpbGx8ZW58MHx8MHx8&auto=format&fit=crop&w=1200&q=60"
        ),

        Animal(
        name="Maximilian",
        age=5,
        gender="male",
        species="Dodo Bird",
        price=150000,
        weight=6.5,
        height=1.4,
        health="excellent",
        color="gray",
        purchase_date=string_to_date("2022-10-10"),
        sold_date=string_to_date("2023-02-01"),
        supplier="exoticbirds@birdsanctuary.com",
        purchase_price=45000.0,
        diet='{"type":"Carnivore", "foods":["Fish", "Amphibians"]}',
        notes="Impressive beak.",
        image_url="https://i.guim.co.uk/img/media/53d52ce049c9bcfd587495b77a1332d1ac28fb4d/162_0_2398_1440/master/2398.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=c58b0a3db379142d144a0e69cb14df3c"
        )
    ]

    for obj in animal_objs:
        db.session.add(obj)
        print("+", end='')
    print()
    db.session.commit()
