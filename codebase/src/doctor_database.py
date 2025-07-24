doctor_records = {}

def check_doctor_database_size():
    return len(doctor_records)


def add_doctor_record(id_number, first_name, last_name, specialization, phone_number):
    id_number = "DR" + id_number
    new_doctor = Doctor(id_number, first_name, last_name, specialization, phone_number)
    doctor_records.update({id_number: new_doctor})