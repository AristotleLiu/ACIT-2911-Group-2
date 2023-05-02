"""
1. make sure you have sql alchemy installed with `pip install -U Flask-SQLAlchemy`
2. run `python .\database.py`
3. run `python .\create_tables.py`
4. run `python .\create_animal.py`
5. run "python app.py"
6. Running on http://127.0.0.1:5000
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
    data = Animal.query.all()[0]
    print(data)
    return jsonify(data.to_dict()), 200

@app.route("/animal", methods=["POST"])
def add_animal():
    data = request.json
    
    # Test to see the animal has all the required properties
    for key in ["id", 
                "name", 
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

    new_animal = Animal(id=data["id"], 
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
    return jsonify(new_animal.to_dict())

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
    return jsonify(animal_json)


if __name__ == "__main__":
    app.run(debug=True)