import unittest

from administration import Admin


class MyTestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()

    def test_thatDoctorDatabaseIsInitiallyZero(self):
        self.admin.clear_doctor_database()
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
        self.admin.clear_doctor_database()
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

    def test_that_doctor_last_name_update_fails_for_invalid_id(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Feyifoluwa", "Oncology", "08148260470")
        with self.assertRaises(ValueError):
            self.admin.update_doctor_last_name("DR999", "Fiyinfoluwa")

    def test_that_doctor_specialization_can_be_updated(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.admin.update_doctor_specialization("DR1", "pediatrics")
        self.assertEqual("Pediatrics", self.admin.retrieve_all_doctor_records()["DR1"].get_specialization())

    def test_that_doctor_specialization_update_fails_for_invalid_id(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        with self.assertRaises(ValueError):
            self.admin.update_doctor_specialization("DR999", "Pediatrics")

    def test_that_doctor_phone_number_can_be_updated(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        self.admin.update_doctor_phone_number("DR1", "08123456789")
        self.assertEqual("08123456789", self.admin.retrieve_all_doctor_records()["DR1"].get_phone_number())

    def test_that_doctor_phone_number_update_fails_for_invalid_id(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        with self.assertRaises(ValueError):
            self.admin.update_doctor_phone_number("DR999", "08123456789")

    def test_get_doctor_info_using_doctor_id_number(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        doctor_info = self.admin.retrieve_all_doctor_records()["DR1"].get_doctor_info()
        expected_info = (
            """Doctor ID: DR1
Full-name: Dr. Oginni Fiyinfoluwa
Specialization: Oncology
Phone No: 08148260470"""
        )
        self.assertEqual(expected_info, doctor_info)

    def test_find_doctor_by_id(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Oginni", "Fiyinfoluwa", "Oncology", "08148260470")
        doctor = self.admin.find_doctor_by_id("DR1")
        self.assertIsNotNone(doctor)
        self.assertEqual("Oginni", doctor.get_first_name())
        self.assertEqual("Fiyinfoluwa", doctor.get_last_name())
        self.assertEqual("Oncology", doctor.get_specialization())
        self.assertEqual("08148260470", doctor.get_phone_number())


    def test_that_doctor_can_be_created_with_empty_string(self):
        self.admin.clear_doctor_database()
        with self.assertRaises(ValueError):
            self.admin.register_doctor("", "", "", "")













if __name__ == '__main__':
    unittest.main()
