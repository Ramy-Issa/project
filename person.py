class Person:
    def __init__(self, full_name, age, id_no):
        self.full_name = full_name
        self.age = age
        self.id_no = id_no

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no
