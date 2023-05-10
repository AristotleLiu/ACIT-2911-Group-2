import random
from dates import string_to_date
from app import app, db
from animal import Animal, Invoice, AnimalInvoice

with app.app_context():
    inv = Invoice(
        status="paid",
        date=string_to_date("2022-06-10"),
        name="Tim",
        city="Edmonton",
        province="Alberta",
        postal_code="U8E 9B2",
        phone="901-153-1355",
    )
    db.session.add(inv)
    db.session.commit()

    print("New invoice, with ID", inv.id)

    # Let's add five random products with random quantities to the order
    animals = random.sample(Animal.query.all(), k=5)

    for ani in animals:
        print("Animal added, with ID", ani.id)
        association = AnimalInvoice(animal=ani, invoice=inv)
        ani.is_in_invoice = True
        db.session.add(association)

    db.session.commit()
