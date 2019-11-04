class Employee:
    # class attribute (static variable)
    hraper = 30

    @staticmethod
    def set_hraper(newhraper):
        if newhraper >= 10:
            Employee.hraper = newhraper
        else:
            raise ValueError('Invalid HRA %')

    # constructor
    def __init__(self, name, salary=0):
        # Object attributes
        self.name = name
        if salary < 0:
            raise ValueError("Invalid salary. Cannot be negative!")
        self.salary = salary

    # method
    def print_details(self):
        print("Name    : ", self.name)
        print("Salary  : ", self.salary)

    def get_salary(self):
        return self.salary + self.salary * Employee.hraper / 100


if __name__ == '__main__':
    e1 = Employee("Mr. Abc", -1000)  # create an object
    print(e1.get_salary())
    Employee.set_hraper(40)  # calling static method
    print(e1.get_salary())
