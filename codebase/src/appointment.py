from doctor_database import doctor_records




def get_list_of_doctors_fullname():
    list_of_doctors = [f"{doctor.get_last_name()} {doctor.get_first_name()}" for doctor in doctor_records.values()]
    return list_of_doctors

