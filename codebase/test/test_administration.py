import unittest

from administration import Admin


class MyTestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()

    def test_thatDoctorDatabaseIsInitiallyZero(self):
        self.assertEqual(0, self.admin.check_doctor_database_size())


    def test_thatPatientDatabaseIsInitiallyZero(self):
        self.assertEqual(0, self.admin.check_patient_database_size())

    def test_that_retrieve_patient_database(self):
        self.assertEqual({}, self.admin.retrieve_all_patient_records())
        self.admin.register_patient(2)
        self.assertEqual(1, self.admin.check_patient_database_size())
        self.assertEqual({"PT1":2}, self.admin.retrieve_all_patient_records())
        self.admin.register_patient(3)
        self.assertEqual(2, self.admin.check_patient_database_size())
        self.assertEqual({"PT1":2, "PT2":3}, self.admin.retrieve_all_patient_records())

    def test_that_register_patient(self):

if __name__ == '__main__':
    unittest.main()
