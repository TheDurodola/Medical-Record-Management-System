import unittest


class MyTestAdmin(unittest.TestCase):

    def SetUp(self):
        admin = Admin()

    def test_that_admin_can_add_a_doctor_to_the_doctor_database(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
