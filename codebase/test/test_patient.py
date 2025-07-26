import unittest

from patient import Patient


class MyTestCase(unittest.TestCase):
    def setUp(self):
        student = Patient(1,'John','Doe', 1990, 5, 15,'1234567890')

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
