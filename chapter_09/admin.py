class User():
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print("\nWe have next info about user:")
        print(f"{self.first_name.title()}")
        print(f"{self.last_name.title()}")
        print(f"{self.age}")
        print(f"{self.sex}")

    def attempts_login(self):
        print(f"{self.login_attempts}")

    def greet_user(self):
        print(f"Hello {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self, login):
        self.login_attempts += login

    def reset_login_attempts(self, log_in):
        self.login_attempts = log_in


# class Privileges():
#     def __init__(self, privileges = ["разрешено добавлять сообщения",
#                         "разрешено удалять пользователей",
#                             "разрешено банить пользователей"]):
#         self.privileges = privileges
#
#     def show_privileges(self):
#         print(self.privileges)
# #

# class Admin(User):
#     def __init__(self, first_name, last_name, age, sex):
#         super().__init__(first_name, last_name, age, sex)
#         self.privileges = Privileges()
        # self.privileges = ["разрешено добавлять сообщения",
        #                    "разрешено удалять пользователей",
        #                    "разрешено банить пользователей"]

    # def show_privileges(self):
    #     print(self.privileges)


# admin_0 = Admin('oleksandr', 'semenenko', 33, 'man')
# admin_0.privileges.show_privileges()
