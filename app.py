"""
1. make sure you have sql alchemy installed with `pip install -U Flask-SQLAlchemy`
2. run `python .\create_tables.py`
3. run `python .\create_animal.py`
4. run `python .\create_invoice.py`
5. run "python app.py"
6. Running on http://127.0.0.1:5000
"""
from database import db
from pathlib import Path
from flask import Flask, jsonify, render_template, request, redirect
from models import Animal, Invoice, AnimalInvoice
from dates import string_to_date
import platform

if platform.system() != "Windows":
    """
    Check platform compatibility for the 'crypt' module. This module allows non-Windows users to
    run this program.

    Note: This code is specifically written to handle platforms other than Windows, as the 'crypt' module
    may not be available or supported on all platforms.
    """
    try:
        import crypt
    except ImportError:
        raise ImportError(
            "The crypt module is not available or not supported on this platform"
        )

# Create an instance of the Flask application
app = Flask(__name__)
# Configure the SQLAlchemy database URI
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///store.db"
# Set the instance path to the current directory using Path
app.instance_path = Path(".").resolve()
# Initialize the Flask application with the database
db.init_app(app)


@app.route("/")
def home():
    """
    Renders the home page with a list of all animals.

    Returns:
        str: Rendered HTML template with animal data.
    """
    data = Animal.query.all()
    return render_template("index.html", animals=[item.to_dict() for item in data])


@app.route("/invoice")
def invoice_home():
    """
    Renders the invoice page with a list of all invoices.

    Returns:
        str: Rendered HTML template with invoice data.
    """
    data = Invoice.query.all()
    return render_template("invoice.html", invoices=[item.to_dict() for item in data])


@app.route("/", methods=["POST"])
def add_animal():
    """
    Adds a new animal to the database using data from a submitted form.

    Returns:
        Redirect: Redirects to the homepage after successfully adding the animal to the database.
    """
    data = request.form

    # Test to see the animal has all the required properties
    for key in [
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
        "supplier",
        "purchase_price",
        "diet",
        "notes",
        "image_url",
    ]:
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    # Get the highest ID in the Animal table and increment it to generate a new ID for the new animal
    # If the database is empty, the new ID will be one
    highest_id = db.session.query(db.func.max(Animal.id)).scalar()
    if highest_id:
        new_id = highest_id + 1
    else:
        new_id = 1

    # Create a new Animal object with the provided data
    new_animal = Animal(
        id=new_id,
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
        supplier=data["supplier"],
        purchase_price=data["purchase_price"],
        diet=data["diet"],
        notes=data["notes"],
        image_url=data["image_url"],
    )

    # Add the new animal to the session and commit the changes to the database
    db.session.add(new_animal)
    db.session.commit()

    # Redirect to the homepage after successfully adding the animal
    return redirect("http://127.0.0.1:5000/")


@app.route("/invoice", methods=["POST"])
def add_invoice():
    """
    Adds a new invoice to the database using data from a submitted form.

    Returns:
        Redirect: Redirects to the invoice page after successfully adding the invoice to the database.
    """
    data = request.form

    # Test to see the invoice has all the required properties
    for key in [
        "status",
        "date",
        "name",
        "city",
        "province",
        "street",
        "postal_code",
        "phone",
        "animals_id",
    ]:
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    # Create a new Invoice object with the provided data
    new_invoice = Invoice(
        status=data["status"],
        date=string_to_date(data["date"]),
        name=data["name"],
        city=data["city"],
        province=data["province"],
        postal_code=data["postal_code"],
        phone=data["phone"],
        street=data["street"],
    )

    # Add the new animal to the session and commit the changes to the database
    db.session.add(new_invoice)
    db.session.commit()

    # Creates an association between animals in the invoice and the invoice
    for ani_id in data["animals_id"].split():
        animal = db.session.get(Animal, ani_id)
        association = AnimalInvoice(animal=animal, invoice=new_invoice)
        animal.is_in_invoice = True
        animal.sold_date = new_invoice.date
        db.session.add(association)

    # Redirect to the invoice page after successfully adding the invoice
    db.session.commit()
    return redirect("http://127.0.0.1:5000/invoice")


@app.route("/summary", methods=["post"])
def sum():
    """
    Redirects to the summary page.

    Returns:
        Redirect: Redirects to the summary page.
    """
    return redirect("http://127.0.0.1:5000/summary")


@app.route("/animal/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    """
    Retrieves an animal from the database based on the given animal ID.

    Args:
        animal_id (int): The ID of the animal.

    Returns:
        JSON: JSON representation of the animal's data.
        If the animal ID does not exist, returns an error message with a status code of 404.
    """
    try:
        if not (db.session.get(Animal, animal_id)):
            raise ValueError(f"Animal id {animal_id} does not exist")
    except ValueError as excpt:
        return (
            f"Invalid values: {excpt}",
            404,
        )

    animal = db.session.get(Animal, animal_id)
    return jsonify(animal.to_dict())


@app.route("/invoice/<int:invoice_id>", methods=["GET"])
def get_invoice(invoice_id):
    """
    Retrieves an invoice from the database based on the given invoice ID.

    Args:
        invoice_id (int): The ID of the invoice.

    Returns:
        JSON: JSON representation of the invoice's data.
        If the invoice ID does not exist, returns an error message with a status code of 404.
    """
    try:
        if not (db.session.get(Invoice, invoice_id)):
            raise ValueError(f"Invoice id {invoice_id} does not exist")
    except ValueError as excpt:
        return (
            f"Invalid values: {excpt}",
            404,
        )

    invoice = db.session.get(Invoice, invoice_id)
    return jsonify(invoice.to_dict())


@app.route("/animal/<int:animal_id>", methods=["DELETE"])
def delete_animal(animal_id):
    """
    Deletes an animal from the database based on the given animal ID.

    Args:
        animal_id (int): The ID of the animal.

    Returns:
        str: Success message indicating the item has been deleted from the database.
    """
    animal = db.session.get(Animal, animal_id)
    db.session.delete(animal)
    db.session.commit()
    return "Item deleted from the database"


@app.route("/animal/<int:animal_id>", methods=["POST"])
def update_animal(animal_id):
    """
    Updates an animal in the database with the provided data based on the given animal ID.

    Args:
        animal_id (int): The ID of the animal.

    Returns:
        Redirect: Redirects to the homepage after successfully updating the animal.
        If the provided data is invalid, returns an error message with a status code of 400.
    """
    data = request.form

    # Test to see if the animal has all the required properties
    for key in [
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
        "supplier",
        "purchase_price",
        "diet",
        "notes",
        "image_url",
    ]:
        if key not in data:
            return f"The JSON provided is invalid (missing: {key})", 400

    # Update the animal object with the provided data
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
    animal.supplier = data["supplier"]
    animal.purchase_price = data["purchase_price"]
    animal.diet = data["diet"]
    animal.notes = data["notes"]
    animal.image_url = data["image_url"]

    db.session.commit()
    return redirect("http://127.0.0.1:5000/")


@app.route("/invoice/<int:invoice_id>", methods=["POST"])
def update_invoice(invoice_id):
    """
    Updates an invoice in the database with the provided data based on the given invoice ID.

    Args:
        invoice_id (int): The ID of the invoice.

    Returns:
        Redirect: Redirects to the invoice page after successfully updating the invoice.
        If the provided data is invalid, returns an error message with a status code of 400.
    """
    data = request.form

    if "status" not in data:
        return "The JSON provided is invalid (missing: 'status')", 400

    invoice = db.session.get(Invoice, invoice_id)

    # Update the invoice's status with the provided data
    invoice.status = data["status"]

    db.session.commit()
    return redirect("http://127.0.0.1:5000/invoice")


@app.route("/invoice/all", methods=["GET"])
def get_all_invoices():
    """
    Retrieves all invoices from the database.

    Returns:
        list: List of dictionaries representing each invoice's data.
    """
    invoice_data = Invoice.query.all()
    return [item.to_dict() for item in invoice_data]


if __name__ == "__main__":
    app.run(debug=True)