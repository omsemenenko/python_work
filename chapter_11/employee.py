class Employee():
    def __init__(self, first_name, last_name, sallary):
        self.first_name = first_name
        self.last_name = last_name
        self.sallary = sallary

    def give_raise(self, dollars):
        dollars = 5000
        self.sallary += dollars
        print(f"Your new sallary {self.sallary}")

    def read_sallary(self):
        print(f"You exist sallry {self.sallary}")

employee_01 = Employee('oleksandr', 'semenenko', '500')

employee_01.read_sallary()
employee_01.give_raise()
