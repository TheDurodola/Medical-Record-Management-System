__patient_records = {}

def add_patient_record(id_number, firstname, lastname, date_of_birth, phone_number):
    id_number = "PT" + id_number
    new_patient = Patient(id_number, firstname, lastname, date_of_birth, phone_number)
    __patient_records.update(id_number = new_patient)



def delete_patient_record(String):
    __patient_records.pop(String)


def update_patient_record(id_number, firs):
