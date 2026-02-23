# Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Employee class (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        self.display_person()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


# Manager class (inherits from Person and Employee)
class Manager(Employee, Person):
    def __init__(self, name, age, employee_id, salary, department):
        Employee.__init__(self, name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        self.display_employee()
        print("Department:", self.department)


# Creating object of Manager class
manager1 = Manager("Sakshi", 19, 101, 50000, "IT")

# Display manager details
manager1.display_manager()