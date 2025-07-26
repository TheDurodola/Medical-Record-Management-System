class Patient:
    def __init__(self, patient_id, first_name, last_name, date_of_birth, phone_number):
        self.__patient_id = patient_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__phone_number = phone_number
        self.__medical_history = []



    def add_medical_record(self, record):
        self.medical_history.append(record)

    def get_medical_history(self):
        return self.medical_history

    def __str__(self):
        return f"Patient(Name: {self.name}, Age: {self.age})"