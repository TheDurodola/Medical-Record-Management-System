class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization, phone_number):
        self.__doctor_id = doctor_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__specialization = specialization
        self.__phone_number = phone_number

    def get_doctor_id(self):
        return self.__doctor_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_doctor_info(self):
        return f"Doctor ID: {self.__doctor_id}\nFull-name: Dr. {self.__first_name} {self.__last_name}\nSpecialization: {self.__specialization}\nPhone No{self.__phone_number}"