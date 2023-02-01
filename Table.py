class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.salary}"


class EmployeeData:
    def __init__(self, employees):
        self.employees = employees

    def sort_data(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter")
            return

    def print_data(self):
        for employee in self.employees:
            print(employee)

employee1 = Employee("Raman", 41, 56000)
employee2 = Employee("Himadri", 38, 67500)
employee3 = Employee("Jaya", 51, 82100)
employee4 = Employee("Tejas", 30, 55000)
employee5 = Employee("Ajay", 45, 44000)

employee_data = EmployeeData([employee1, employee2, employee3, employee4, employee5])

sort_key = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))

employee_data.sort_data(sort_key)
employee_data.print_data()
