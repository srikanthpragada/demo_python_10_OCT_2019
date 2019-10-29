class Employee:
    # constructor
    def __init__(self, name, salary=0):
        # Object attributes
        self.name = name
        self.salary = salary

    # method
    def print_details(self):
        print("Name    : ", self.name)
        print("Salary  : ", self.salary)


if __name__ == '__main__':
    e1 = Employee("Mr. Abc", 100000)  # create an object
    e1.print_details()  # call methods

    e2 = Employee("Mr.Joe")
    e2.print_details()
