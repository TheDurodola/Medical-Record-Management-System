import datetime




def validate_title(title):
    if title not in ['Mr.', 'Ms.', 'Mrs.', "Miss", 'Mr', 'Ms', 'Mrs', 'Miss.', "Olamide"]:
        raise ValueError('Invalid title! Title must be one of the following: Mr., Ms., Mrs., Miss, Mr, Ms, Mrs, Miss.')


def get_gender(title):
    if title in ['Mr.', 'Mr']:
        return "Male"
    elif title in ['Ms.', 'Ms', 'Mrs.', 'Mrs', 'Miss', 'Miss.']:
        return "Female"
    else:
        return "Shemale??"

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

class Patient:
    def __init__(self, patient_id, title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number):
        validate_name(first_name)
        validate_name(last_name)
        validate_phone_number(phone_number)
        validate_title(title)
        self.__gender = get_gender(title)
        self.__title = title
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
        self.__age = datetime.date.today().year - self.__date_of_birth.year
        self.__phone_number = phone_number
        self.__doctor_assigned = None
        self.__medical_history = []


    def get_patient_id(self):
        return self.__patient_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__date_of_birth

    def set_first_name(self, first_name):
        validate_name(first_name)
        self.__first_name = first_name.title()

    def set_last_name(self, last_name):
        validate_name(last_name)
        self.__last_name = last_name.title()


    def set_phone_number(self, phone_number):
        validate_phone_number(phone_number)
        self.__phone_number = phone_number

    def get_title(self):
        return self.__title


    def get_phone_number(self):
        return self.__phone_number

    def set_doctor_assigned(self, doctor_assigned):
        self.__doctor_assigned = "Dr. " + doctor_assigned

    def get_assigned_doctor(self):
        return self.__doctor_assigned



    def add_medical_record(self, record):
        self.__medical_history.append(record)

    def get_medical_history(self):
        return self.__medical_history




    def __str__(self):
        return f"TO-SEE: {self.__doctor_assigned}\nPatient ID: {self.__patient_id}\nName: {self.__title} {self.__first_name} {self.__last_name}\nGender: {self.__gender}\nDate of Birth: {self.__date_of_birth}\nAge: {self.__age} years\nPhone No: {self.__phone_number}\nRecent Medical History: {self.__medical_history[:3] if self.__medical_history else 'No medical records available'}"