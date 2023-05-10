import unittest
import dates
from datetime import datetime

class Test_animal(unittest.TestCase):
    
    def test_date(self):
        date_format = '%Y-%m-%d'
        datetime_obj = datetime.strptime("2023-08-21", date_format)
        self.assertEqual(dates.string_to_date("2023-08-21"),datetime_obj.date())

if __name__ == '__main__':
    unittest.main()


