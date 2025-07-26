class Doctor:
    def __init__(self, doctor_id, first_name, last_name, specialization, phone_number):
        self.doctor_id = doctor_id
        self._first_name = first_name
        self._last_name = last_name
        self._specialization = specialization
        self._phone_number = phone_number

    def get_doctor_id(self):
        return self.doctor_id


    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, specialization):
        self._specialization = specialization

    def get_doctor_info(self):
        return f"Doctor ID: {self.doctor_id}\nFull-name: Dr. {self.first_name} {self.last_name}\nSpecialization: {self.specialization}\nPhone No{self.phone_number}"