from person import Person


class Librarian(Person):
    def __init__(self, id, full_name, age, id_no, emplyment_type):
        super(Librarian, self).__init__(full_name = full_name, age = age, id_no = id_no)
        self.id = id
        self.emplyment_type = emplyment_type

    def get_id(self):
        return self.id

    def get_emplyment_type(self):
        return self.emplyment_type