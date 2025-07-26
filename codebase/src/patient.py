import datetime

from doctor import validate_phone_number, validate_name


def validate_title(title):
    if title not in ['Mr.', 'Ms.', 'Mrs.', "Miss", 'Mr', 'Ms', 'Mrs', 'Miss.']:
        raise ValueError('Invalid title! Title must be one of the following: Mr., Ms., Mrs., Miss, Mr, Ms, Mrs, Miss.')


def get_gender(title):
    if title in ['Mr.', 'Mr']:
        return "Male"
    elif title in ['Ms.', 'Ms', 'Mrs.', 'Mrs', 'Miss', 'Miss.']:
        return "Female"
    else:
        return "Unknown"


class Patient:
    def __init__(self, patient_id, title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number):
        validate_name(first_name)
        validate_name(last_name)
        validate_phone_number(phone_number)
        validate_title(title)
        self.__gender = get_gender(title)
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
        self.__age = datetime.date.today().year - self.__date_of_birth.year
        self.__phone_number = phone_number
        self.__medical_history = []



    def add_medical_record(self, record):
        self.__medical_history.append(record)

    def get_medical_history(self):
        return self.__medical_history




    def __str__(self):
        return f"Patient ID: {self.__patient_id}\nName: {self.__first_name} {self.__last_name}\nGender: {self.__gender}\nDate of Birth: {self.__date_of_birth}\nAge: {self.__age} years\nPhone No: {self.__phone_number}\nRecent Medical History: {self.__medical_history[3:] if self.__medical_history else 'No medical records available'}"