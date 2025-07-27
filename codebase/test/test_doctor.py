from doctor import Doctor
import unittest

class TestDoctor(unittest.TestCase):

    def test_validate_doctor_creation(self):
        doctor = Doctor("DR232", "jayjus23", "Justine", "Babatunde", "Gynecologist", "09021885123")
        self.assertEqual(doctor.get_doctor_id(), "DR232")
        self.assertEqual(doctor.get_first_name(), "Justine")
        self.assertEqual(doctor.get_last_name(), "Babatunde")
        self.assertEqual(doctor.get_specialization(), "Gynecologist")
        self.assertEqual(doctor.get_phone_number(), "09021885123")

    def test_invalid_first_name_with_a_character(self):
        with self.assertRaises(ValueError):
            Doctor("DR232", "jayjus23", "J/ustine", "Babatunde", "Gynecologist", "09021885123")

    def test_invalid_password_with_a_password_less_than_8_character(self):
        with self.assertRaises(ValueError):
            Doctor("DR232", "jay7", "Justine", "Babatunde", "Gynecologist", "09021885123")

    def test_invalid_last_name_with_a_space_in_between_the_name(self):
        with self.assertRaises(ValueError):
            Doctor("DR232", "jayjus23","Justine", "Baba tunde", "Gynecologist", "09021885123")

    def test_invalid_specialization_with_a_number(self):
        with self.assertRaises(ValueError):
            Doctor("DR232", "jayjus23", "Justine", "Babatunde", "Gy45necologist", "09021885123")

    def test_invalid_phone_number_with_an_empty_string(self):
        with self.assertRaises(ValueError):
            Doctor("DR232", "jayjus23","Justine", "Babatunde", "Gynecologist", "")



if __name__ == '__main__':
    unittest.main()
