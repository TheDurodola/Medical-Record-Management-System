import unittest

from patient import Patient


class MyTestCase(unittest.TestCase):
    def setUp(self):
        student = Patient(1,"Mr.", 'John','Doe', 1990, 5, 15,'12345678901')

  # add assertion here


if __name__ == '__main__':
    unittest.main()
