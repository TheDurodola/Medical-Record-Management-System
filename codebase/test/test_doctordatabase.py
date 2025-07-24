import unittest
import doctor_database
class MyTestCase(unittest.TestCase):
    def test_that_doctor_database_initial_size_is_zero(self):
        self.assertEqual(0, doctor_database.check_doctor_database_size())
if __name__ == '__main__':
    unittest.main()
