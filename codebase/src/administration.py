from itertools import cycle

from patient_database import patient_records
from doctor_database import doctor_records
from appointment import *

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
        return f"{title} {first_name} {last_name} has been registered successfully as a patient with ID: {id_number}"

    def register_doctor(self, password, firstname, lastname, specialization, phone_number):
        id_number = self.check_doctor_database_size() + 1
        id_number = "DR" + str(id_number)
        new_doctor = Doctor(id_number, password,firstname, lastname, specialization, phone_number)
        doctor_records[id_number] = new_doctor
        return f"{firstname} {lastname} has been registered successfully as a doctor with ID: {id_number}"

    def clear_doctor_database(self):
        doctor_records.clear()

    def update_doctor_first_name(self, id_number, new_first_name):
        if id_number.upper() in doctor_records:
            doctor_records[id_number].set_first_name(new_first_name)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_last_name(self, id_number, new_last_name):
        if id_number.upper() in doctor_records:
            doctor_records[id_number].set_last_name(new_last_name)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_specialization(self, id_number, new_specialization):
        if id_number.upper() in doctor_records:
            doctor_records[id_number].set_specialization(new_specialization)
        else:
            raise ValueError("Doctor ID not found")

    def update_doctor_phone_number(self, id_number, new_phone_number):
        if id_number.upper() in doctor_records:
            doctor_records[id_number].set_phone_number(new_phone_number)
        else:
            raise ValueError("Doctor ID not found")

    def find_doctor_by_id(self, id_number):
        if id_number.upper() in doctor_records:
            return doctor_records[id_number]
        else:
            raise ValueError("Doctor ID not found")

    def assign_doctor_to_patient(self):
        list_of_doctors = get_list_of_doctors_fullname()
        for key, value in zip(patient_records, cycle(list_of_doctors)):
            patient_records[key].set_doctor_assigned(value)
        for doctor in doctor_records.values():
            list_of_patients = []
            for patient in patient_records.values() :
                if patient.get_assigned_doctor() == doctor.get_full_name():
                    list_of_patients.append(f"{patient.get_title()} {patient.get_first_name()} {patient.get_last_name()}")
        doctor.set_list_of_patients(list_of_patients)

    def clear_patient_database(self):
        patient_records.clear()

    def update_patient_last_name(self, id_number, new_value):
        if id_number.upper() in patient_records:
            patient_records[id_number].set_last_name(new_value)
        else:
            raise ValueError("Patient ID not found")

    def update_patient_first_name(self, id_number, new_value):
        if id_number.upper() in patient_records:
            patient_records[id_number].set_first_name(new_value)
        else:
            raise ValueError("Patient ID not found")

    def update_patient_phone_number(self, id_number, new_value):
        if id_number.upper() in patient_records:
            patient_records[id_number].set_phone_number(new_value)
        else:
            raise ValueError("Patient ID not found")

    def find_patient_by_id(self, id_number):
        if id_number.upper() in patient_records:
            return patient_records[id_number]
        else:
            raise ValueError("Patient ID not found")

    def print_schedule_report(self):
        report = "Schedule Report:\n"
        for doctor in doctor_records.values():
            report += f"\nDoctor: {doctor.get_full_name()}\n"
            report += "Patients:\n"
            if doctor.get_list_of_patients():
                for patient in doctor.get_list_of_patients():
                    report += f"- {patient}\n"
            else:
                report += "No patients assigned.\n"
        return report

    def authenticate_doctor(self, doctor_id, password):
        if doctor_id.upper() in doctor_records:
            doctor = doctor_records[doctor_id.upper()]
            if doctor.get_password() == password:
                return True
            else:
                raise ValueError("Incorrect password")
        else:
            raise ValueError("Doctor ID not found")
