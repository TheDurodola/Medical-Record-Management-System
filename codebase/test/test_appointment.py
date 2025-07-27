import unittest
from administration import Admin
from appointment import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.admin = Admin()

    def test_thatListOfDoctorsFullnameCanBeExtracted(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Victoria%",  "Fiyinfoluwa","Oginni", "Oncology", "08148260470")
        self.admin.register_doctor("MoneyMan12",  "John", "Doe","Cardiology", "08123456789")
        expected_fullnames = ["Oginni Fiyinfoluwa", "Doe John"]
        self.assertEqual(expected_fullnames, get_list_of_doctors_fullname())

    def test_thatDoctorCanBeAssignedToPatient(self):
        self.admin.clear_doctor_database()
        self.admin.register_doctor("Victoria%",  "Fiyinfoluwa","Oginni", "Oncology", "08148260470")
        self.admin.register_patient("Mr.", "John", "Doe", 1990, 1, 1, "08123456789")
        self.admin.assign_doctor_to_patient()
        self.assertEqual("Dr. Oginni Fiyinfoluwa", self.admin.retrieve_all_patient_records()["PT1"].get_assigned_doctor())
        self.admin.register_doctor("DmanFlex", "Abolaji", "Durodola", "Oncology", "08148260470")
        self.admin.register_patient("Ms.", "Jane", "Doe", 1995, 2, 2, "08123456789")
        self.admin.assign_doctor_to_patient()
        self.assertEqual("Dr. Durodola Abolaji", self.admin.retrieve_all_patient_records()["PT2"].get_assigned_doctor())
        self.admin.register_patient("Mr.", "Michael", "Smith", 1985, 3, 3, "08123456789")
        self.admin.assign_doctor_to_patient()
        self.assertEqual("Dr. Oginni Fiyinfoluwa", self.admin.retrieve_all_patient_records()["PT3"].get_assigned_doctor())
        self.admin.register_doctor("DrSmith!", "Alice", "Johnson", "Pediatrics", "08148260470")
        self.admin.assign_doctor_to_patient()
        self.assertEqual("Dr. Johnson Alice", self.admin.retrieve_all_patient_records()["PT3"].get_assigned_doctor())





if __name__ == '__main__':
    unittest.main()
