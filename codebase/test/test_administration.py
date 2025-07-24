import unittest

from administration import Admin


class MyTestAdmin(unittest.TestCase):


    def test_that_admin_can_add_a_doctor_to_the_doctor_database(self):
        admin = Admin()
        admin.add_doctor("Akintunde", "Ojo", "Cardiology", "070123456789")
        self.assertEqual(1, admin.check_doctor_database_size())


if __name__ == '__main__':
    unittest.main()
