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

user = User('semenenko', 'oleksandr', 33, 'man')
user.increment_login_attempts(1)
user.attempts_login()

user.increment_login_attempts(1)
user.attempts_login()

user.increment_login_attempts(1)
user.attempts_login()

user.reset_login_attempts(0)
user.attempts_login()

user.increment_login_attempts(1)
user.attempts_login()

# user_0 = User('oleksandr', 'semenenko', 33, 'man')
# user_0.describe_user()
# user_0.greet_user()
#
# user_1 = User('nadiia', 'semenenko', 30, 'woman')
# user_1.describe_user()
# user_1.greet_user()
#
# user_2 = User('dmitriy','semenenko', 5, 'man')
# user_2.describe_user()
# user_2.greet_user()

