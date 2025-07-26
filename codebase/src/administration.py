from patient_database import patient_records
from doctor_database import doctor_records

from doctor import Doctor
# from patient import Patient

class Admin:

    def check_doctor_database_size(self):
        return len(doctor_records)

    def check_patient_database_size(self):
        return len(patient_records)

    def retrieve_all_patient_records(self):
        return patient_records

    def register_patient(self, new_patient):
        id_number = self.check_patient_database_size() + 1
        id_number = "PT" + str(id_number)
        # new_patient = Patient(id_number, first_name, last_name, date_of_birth, phone_number)
        patient_records[id_number] = new_patient

    def register_doctor(self, firstname, lastname, specialization, phone_number):
        id_number = self.check_doctor_database_size() + 1
        id_number = "DR" + str(id_number)
        new_doctor = Doctor(id_number, firstname, lastname, specialization, phone_number)
        doctor_records[id_number] = new_doctor

    def clear_doctor_database(self):
        doctor_records.clear()
    # def add_doctor(self, first_name, last_name, specialization, phone_number):
    #     id_number = len(doctor_records) + 1
    #     new_doctor = Doctor(id_number, first_name, last_name, specialization, phone_number)
    #     doctor_records.update(id_number = new_doctor)
    #
    # def add_new_patient(self, first_name, last_name, date_of_birth, phone_number):
    #     id_number = len(patient_records) + 1
    #     new_patient = Patient(id_number, first_name, last_name, date_of_birth, phone_number)
    #     patient_records.update(id_number = new_patient)


    def update_doctor_record(self, id_number, first_name, last_name, specialization, phone_number):
        pass