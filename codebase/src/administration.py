from patient_database import patient_records
from doctor_database import doctor_records

from doctor import Doctor
from patient import Patient

class Admin:

    def check_doctor_database_size(self):
        return len(doctor_records)

    def check_patient_database_size(self):
        return len(patient_records)

    def retrieve_all_patient_records(self):
        return patient_records

    def retrieve_all_doctor_records(self):
        return doctor_records

    def register_patient(self, title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number):
        id_number = self.check_patient_database_size() + 1
        id_number = "PT" + str(id_number)
        new_patient = Patient(id_number, title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number)
        patient_records[id_number] = new_patient

    def register_doctor(self, password, firstname, lastname, specialization, phone_number):
        id_number = self.check_doctor_database_size() + 1
        id_number = "DR" + str(id_number)
        new_doctor = Doctor(id_number, password,firstname, lastname, specialization, phone_number)
        doctor_records[id_number] = new_doctor

    def clear_doctor_database(self):
        doctor_records.clear()

    def update_doctor_first_name(self, id_number, new_first_name):
        if id_number in doctor_records:
            doctor_records[id_number].set_first_name(new_first_name)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_last_name(self, id_number, new_last_name):
        if id_number in doctor_records:
            doctor_records[id_number].set_last_name(new_last_name)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_specialization(self, id_number, new_specialization):
        if id_number in doctor_records:
            doctor_records[id_number].set_specialization(new_specialization)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_phone_number(self, id_number, new_phone_number):
        if id_number in doctor_records:
            doctor_records[id_number].set_phone_number(new_phone_number)
        else:
            raise ValueError("Doctor ID not found")

    def find_doctor_by_id(self, id_number):
        if id_number in doctor_records:
            return doctor_records[id_number]
        else:
            raise ValueError("Doctor ID not found")