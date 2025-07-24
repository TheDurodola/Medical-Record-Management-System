import unittest
import patient_database





class TestPatientDatabase(unittest.TestCase):
    def test_patient_database_is_zero_initially(self):
        self.assertEqual(0, patient_database.check_database_size())

    def test_add_patient_record_database_size_is_1(self):
        patient_database.add_patient_record(Patient("1", "John", "Doe", "1990-01-01", "1234567890"))
        self.assertEqual(1, patient_database.check_database_size())



if __name__ == '__main__':
    unittest.main()
