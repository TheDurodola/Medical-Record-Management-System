patient_records = {}



def check_database_size():
    return len(patient_records)

def add_patient_record(id_number, firstname, lastname, date_of_birth, phone_number):
    id_number = "PT" + id_number
    new_patient = Patient(id_number, firstname, lastname, date_of_birth, phone_number)
    patient_records.update(id_number = new_patient)


def update_patient_record(id_number, firstname=None, lastname=None, date_of_birth=None, phone_number=None):
    id_number = "PT" + id_number
    if id_number in patient_records:
        patient = patient_records[id_number]
        if firstname:
            patient.firstname = firstname
        if lastname:
            patient.lastname = lastname
        if date_of_birth:
            patient.date_of_birth = date_of_birth
        if phone_number:
            patient.phone_number = phone_number
    else:
        raise KeyError("Patient record not found.")


def delete_patient_record(id_number):
    patient_records.pop(id_number)

