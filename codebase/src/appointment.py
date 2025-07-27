from doctor_database import doctor_records
from patient_database import patient_records



def get_list_of_doctors_fullname():
    list_of_doctors = [f"{doctor.get_first_name()} {doctor.get_last_name()}" for doctor in doctor_records.values()]
    return list_of_doctors

def assign_doctor_to_patient(patient_id, doctor_id):
    pass