"""
1. make sure you have sql alchemy installed with `pip install -U Flask-SQLAlchemy`
2. run `python .\create_tables.py`
3. run `python .\create_animal.py`
4. run "python app.py"
5. Running on http://127.0.0.1:5000
"""
from database import db
from pathlib import Path
from flask import Flask, jsonify, render_template, request
from animal import Animal
from dates import string_to_date
import json

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
app.instance_path = Path(".").resolve()
db.init_app(app)

@app.route("/")
def home():
    data = Animal.query.all()
    return render_template("index.html", animals=data)

@app.route("/", methods=["POST"])
def add_animal():
    data = request.form
    
    # Test to see the animal has all the required properties
    for key in ["name", 
                "age", 
                "gender", 
                "species", 
                "price", 
                "weight", 
                "height", 
                "health", 
                "color", 
                "purchase_date", 
                "sold_date", 
                "supplier", 
                "purchase_price", 
                "diet", 
                "notes"]:
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    highest_id = db.session.query(db.func.max(Animal.id)).scalar()
    if highest_id:
        new_id = highest_id + 1
    else:
        new_id = 1

    new_animal = Animal(id=new_id, 
                    name=data["name"],
                    age=data["age"], 
                    gender=data["gender"], 
                    species=data["species"],
                    price=data["price"], 
                    weight=data["weight"], 
                    height=data["height"], 
                    health=data["health"],
                    color=data["color"], 
                    purchase_date=string_to_date(data["purchase_date"]),
                    sold_date=string_to_date(data["sold_date"]),
                    supplier=data["supplier"],
                    purchase_price=data["purchase_price"],
                    diet=json.dumps(data["diet"]),
                    notes=data["notes"])
    
    db.session.add(new_animal)
    db.session.commit()
    return "Item added to the database"

@app.route("/animal/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    try:
        if not (db.session.get(Animal, animal_id)):
            raise ValueError(f"Animal id {animal_id} does not exist")
    except ValueError as excpt:
        return (
            f"Invalid values: {excpt}",
            404,
        )

    animal = db.session.get(Animal, animal_id)
    animal_json = animal.to_dict()
    return animal

@app.route("/animal/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    animal = db.session.get(Animal, animal_id)
    db.session.delete(animal)
    db.session.commit()
    return "Item deleted from the database"

@app.route("/animal/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    data = request.json
    
    # Test to see the animal has all the required properties
    for key in ["name", 
                "age", 
                "gender", 
                "species", 
                "price", 
                "weight", 
                "height", 
                "health", 
                "color", 
                "purchase_date", 
                "sold_date", 
                "supplier", 
                "purchase_price", 
                "diet", 
                "notes"]:
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400
        
    animal = db.session.get(Animal, animal_id)
    animal.name = data["name"]
    animal.age = data["age"]
    animal.gender = data["gender"] 
    animal.species = data["species"]
    animal.price = data["price"] 
    animal.weight = data["weight"] 
    animal.height = data["height"]
    animal.health = data["health"]
    animal.color = data["color"]
    animal.purchase_date = string_to_date(data["purchase_date"])
    animal.sold_date = string_to_date(data["sold_date"])
    animal.supplier = data["supplier"]
    animal.purchase_price = data["purchase_price"]
    animal.diet = json.dumps(data["diet"])
    animal.notes = data["notes"]

    db.session.commit()
    return "Item updated in the database"

if __name__ == "__main__":
    app.run(debug=True)