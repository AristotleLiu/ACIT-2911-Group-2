import random
from dates import string_to_date
from app import app, db
from models import Animal, Invoice, AnimalInvoice

with app.app_context():
    # Create a list of invoices
    invoice_list = [
        Invoice(
            status="Paid",
            date=string_to_date("2023-06-10"),
            name="Tim",
            city="Victoria",
            province="BC",
            postal_code="U8E 9B2",
            phone="601-153-1355",
            street="9000 Great White St.",
        ),
        Invoice(
            status="Unpaid",
            date=string_to_date("2023-07-05"),
            name="Jane",
            city="Toronto",
            province="ON",
            postal_code="M5V 2J4",
            phone="905-123-4567",
            street="002 Dino St.",
        ),
        Invoice(
            status="Paid",
            date=string_to_date("2023-08-15"),
            name="Michael",
            city="Calgary",
            province="AB",
            postal_code="T2P 3G6",
            phone="403-789-0123",
            street="1333 Turkey St.",
        ),
        Invoice(
            status="Void",
            date=string_to_date("2023-09-20"),
            name="Sarah",
            city="Montreal",
            province="QC",
            postal_code="H2Y 1T1",
            phone="514-555-7890",
            street="264 Raptor St.",
        ),
        Invoice(
            status="Unpaid",
            date=string_to_date("2023-10-25"),
            name="David",
            city="Vancouver",
            province="BC",
            postal_code="V6B 4N9",
            phone="604-987-6543",
            street="13851 Animal St.",
        ),
    ]

    # Create a list of associations between invoices and animals
    invoice_animals_list = [[12, 5, 6], [1, 5, 20, 21], [24, 25], [7], [10, 11, 15]]

    # Iterate over the invoice list
    for inv in invoice_list:
        # Add the invoice to the database session and commit the changes
        db.session.add(inv)
        db.session.commit()
        print("New invoice, with ID", inv.id)

        # Iterate over the animal IDs associated with the current invoice
        for ani_id in invoice_animals_list[invoice_list.index(inv)]:
            # Retrieve the animal from the database session
            ani = db.session.get(Animal, ani_id)
            print("+", end="")

            # Create an association between the animal and the invoice
            association = AnimalInvoice(animal=ani, invoice=inv)
            ani.is_in_invoice = True
            ani.sold_date = inv.date
            db.session.add(association)
        print()

    # Commit the changes made to the database session
    db.session.commit()
