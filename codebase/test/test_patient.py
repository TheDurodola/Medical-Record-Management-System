import unittest

from patient import Patient


class MyTestCase(unittest.TestCase):
    def setUp(self):
        student = Patient(1,"Mr.", 'John','Doe', 1990, 5, 15,'12345678901')

    def test_add_to_medical_history(self):
        patient = Patient("PT001", "Mr.", "John", "Doe", 1990, 5, 15, "12345678901")
        patient.add_medical_record("Flu symptoms")
        self.assertEqual(['Flu symptoms'], patient.get_medical_history())


if __name__ == '__main__':
    unittest.main()
