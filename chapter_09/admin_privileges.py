class Privileges():
    def __init__(self, privileges = ["разрешено добавлять сообщения",
                        "разрешено удалять пользователей",
                            "разрешено банить пользователей"]):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)


class Admin(User):
    def __init__(self, first_name, last_name, age, sex):
        super().__init__(first_name, last_name, age, sex)
        self.privileges = Privileges()