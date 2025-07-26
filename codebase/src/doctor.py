from patient_database import patient_records
from patient import Patient



def validate_name(name):
    if name.startswith(' ') or name.endswith(' '):
        name.trim()
    if name.isnumeric() or ' ' in name:
        raise ValueError('Invalid name! Name must contain only letters and no spaces.')
    if not name or not name.replace(' ', '').isalpha():
        raise ValueError('Invalid name! Name must contain only letters and not empty.')
    for char in name:
        if not char.isalpha() and char != ' ':
            raise ValueError('Invalid name! Name must contain only letters and no special characters.')

    return name


def validate_phone_number(number):
    if not number.isdigit() or len(number) != 11:
        raise ValueError('Invalid phone number! Phone number must contain only digits and be eleven digits long.')
    if not number:
        raise ValueError('Phone number cannot be empty!')


def validate_password(password):
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long.')



class Doctor:
    def __init__(self, doctor_id, password, first_name, last_name, specialization, phone_number):
        first_name = validate_name(first_name)
        last_name = validate_name(last_name)
        validate_name(specialization)
        validate_phone_number(phone_number)
        validate_password(password)
        self.__doctor_id = doctor_id
        self.__first_name = first_name.title()
        self.__last_name = last_name.title()
        self.__specialization = specialization.title()
        self.__phone_number = phone_number

    def retrieve_all_patient_records(self):
        return patient_records

    def get_doctor_id(self):
        return self.__doctor_id


    def set_password(self, password):
        validate_password(password)
        self.__password = password

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        validate_name(first_name)
        self.__first_name = first_name.title()

    def get_last_name(self):
        return self.__last_name


    def set_last_name(self, last_name):
        validate_name(last_name)
        self.__last_name = last_name.title()

    def get_specialization(self):
        return self.__specialization


    def set_specialization(self, specialization):
        validate_name(specialization)
        self.__specialization = specialization.title()


    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        validate_phone_number(phone_number)
        self.__phone_number = phone_number

    def get_doctor_info(self):
        return f"Doctor ID: {self.__doctor_id}\nFull-name: Dr. {self.__first_name} {self.__last_name}\nSpecialization: {self.__specialization}\nPhone No: {self.__phone_number}"

