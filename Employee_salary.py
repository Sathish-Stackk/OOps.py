class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

    def get_salary(self):
        return self.__salary


employee = Employee("Arjun", 30000)

employee.increase_salary(5000)

print("Employee:", employee.name)
print("Updated Salary:", employee.get_salary())
