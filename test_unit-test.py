import unittest
import dates
from datetime import datetime
from animal import Animal
from datetime import date
from app import app, db

class Test_animal(unittest.TestCase):
    

    # Date Format Checker 
    def test_date(self):
        date_format = '%Y-%m-%d'
        datetime_obj = datetime.strptime("2023-08-21", date_format)
        self.assertEqual(dates.string_to_date("2023-08-21"),datetime(year=2023,month=8,day=21).date())

    def test_to_dict(self):
    # Gets an instance of one of the animal object in the database
        animal = Animal(
            name='Fluffy',
            age=3,
            gender='female',
            species='cat',
            price=50.0,
            weight=4.0,
            height=8.0,
            health='good',
            color='white',
            purchase_date=date.today(),
            sold_date=None,
            supplier='Pet Store',
            purchase_price=25.0,
            diet={'morning': 'kibble', 'afternoon': 'wet food'},
            notes='likes to play with toys',
            image_url=None
    )


    # Convert it from a string to a dictionary
        diet_dict = {'morning': 'kibble', 'afternoon': 'wet food'}
        animal.set_diet(diet_dict)

    # New dict of the expected result with correct values
        expected_dict = {
            'id': animal.id,
            'name': 'Fluffy',
            'age': 3,
            'gender': 'female',
            'species': 'cat',
            'price': 50.0,
            'weight': 4.0,
            'height': 8.0,
            'health': 'good',
            'color': 'white',
            'purchase_date': date.today(),
            'sold_date': None,
            'supplier': 'Pet Store',
            'purchase_price': 25.0,
            'diet': {'morning': 'kibble', 'afternoon': 'wet food'},
            'notes': 'likes to play with toys',
            'image_url': None,
            'is_in_invoice': None,
        }

    # Run the test to check if the animal obj is same as the expected dictionary
        assert animal.to_dict() == expected_dict
        self.assertEqual(animal.to_dict(), expected_dict)

    # Create test client to run the Flask app
    def setUp(self):
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    # Removes database session 
    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Test home page by getting response using GET and checking if the status code is 200
    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response._status_code, 200)

    # Test invoice page 
    def test_home_invoice(self):
        response = self.app.get('/invoice')
        self.assertEqual(response.status_code, 200)
            

if __name__ == '__main__':
    unittest.main()
