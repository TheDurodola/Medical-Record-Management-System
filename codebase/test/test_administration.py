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

    def test_that_a_new_doctor_can_be_registered(self):
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.assertEqual(1, self.admin.check_doctor_database_size())

    def test_that_doctor_database_can_be_cleared(self):
        self.admin.clear_doctor_database()
        self.assertEqual(0, self.admin.check_doctor_database_size())
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.assertEqual(1, self.admin.check_doctor_database_size())
        self.admin.clear_doctor_database()
        self.assertEqual(0, self.admin.check_doctor_database_size())


    def test_that_multiple_doctors_can_be_registered(self):
        self.admin.clear_doctor_database()
        self.assertEqual(0, self.admin.check_doctor_database_size())
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.admin.register_doctor("Doe", "John", "Cardiology", "08123456789")
        self.assertEqual(2, self.admin.check_doctor_database_size())


    def test_that_doctor_first_name_can_be_update(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Aginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.admin.update_doctor_first_name("DR1", "Oginni")
        self.assertEqual("Oginni", self.admin.retrieve_all_doctor_records()["DR1"].get_first_name())

    def test_that_doctor_first_name_update_fails_for_invalid_id(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Aginni", "Fiyinfoluwa", "Oncology", "08148260470")
        with self.assertRaises(ValueError):
            self.admin.update_doctor_first_name("DR999", "Oginni")


    def test_that_doctor_last_name_can_be_update(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Feyifoluwa", "Oncology", "08148260470")
        self.admin.update_doctor_last_name("DR1", "Fiyinfoluwa")
        self.assertEqual("Fiyinfoluwa", self.admin.retrieve_all_doctor_records()["DR1"].get_last_name())









if __name__ == '__main__':
    unittest.main()
