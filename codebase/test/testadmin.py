import unittest

from administration import Admin


class MyTestAdmin(unittest.TestCase):

    def SetUp(self):
        self.admin = Admin()

    def test_that_admin_can_add_a_doctor_to_the_doctor_database(self):
        self.admin.add_doctor("Dr. Smith", "Cardiology")


    def test_that_admin_can_add_a_patient_to_the_patient_database(self):
        self.admin.add_patient("John Doe", "123-456-7890")


if __name__ == '__main__':
    unittest.main()
