class Doctor:
    def __init__(self, first_name, last_name, specialization):
        self.first_name = first_name
        self.last_name = last_name
        self.specialization = specialization

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_specialization(self):
        return self.specialization

    def view_specialization(self):
        print(self.specialization)