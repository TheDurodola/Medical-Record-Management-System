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
        expected_fullnames = ["Fiyinfoluwa Oginni", "John Doe"]
        self.assertEqual(expected_fullnames, get_list_of_doctors_fullname())
        self.admin.register_patient("Miss", "Jane", "Doe", 1990, 5, 15, "08123456789")
        self.admin



if __name__ == '__main__':
    unittest.main()
