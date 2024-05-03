class Employee:
    def __init__(self, type_of_employee:str, base_salary:int=3000):
        self.type_of_employee = type_of_employee
        self.base_salary = base_salary


class PermanentSalary(Employee):
    def __init__(self):
        super().__init__("Permanent")

    def calculate_salary(self):
        return self.base_salary +1000

class TemporarySalary(Employee):
    def __init__(self):
        super().__init__("Temporary")

    def calculate_salary(self):
        return self.base_salary + 500


class InternSalary(Employee):
    def __init__(self):
        super().__init__("Intern")

    def calculate_salary(self):
        return self.base_salary + 200


permanent_employee = PermanentSalary()
print(permanent_employee.calculate_salary())

temporary_employee = TemporarySalary()
print(temporary_employee.calculate_salary())

intern_employee = InternSalary()
print(intern_employee.calculate_salary())