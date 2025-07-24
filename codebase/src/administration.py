import patient_database
import doctor_database

class Admin:
    def add_doctor(self, id_number, first_name, last_name, specialization, phone_number):
        doctor_database.add_doctor_record(id_number, first_name, last_name, specialization, phone_number)

    def check_doctor_database_size(self):
        return doctor_database.check_doctor_database_size()