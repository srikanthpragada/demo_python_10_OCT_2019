class Student:
    # class attributes
    pythonfee = 10000
    javafee = 15000

    def __init__(self, name, course, feepaid=0):
        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    def total_fee(self):
        return Student.javafee if self.course == 'j' else Student.pythonfee

    def get_due(self):
        if self.course == 'j':
            return Student.javafee - self.feepaid
        else:
            return Student.pythonfee - self.feepaid


s = Student("Larry","j",5000)
s.payment(5000)
print(s.get_due())