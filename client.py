from person import Person


class Client(Person):
    id = 0
    def __init__(self, id, full_name, age, id_no, phone_no):
        super(Client, self).__init__(full_name = full_name,age =  age, id_no = id_no)
        self.id = id
        self.phone_no = phone_no
        list_client = [self.id, self.full_name, self.age, self.id_no, self.phone_no]

    def __str__(self):
        return f"{self.id}, {self.full_name}, {self.age}, {self.id_no}, {self.phone_no}"

    def get_id(self):
        return self.id

    def get_phone_no(self):
        return self.phone_no

