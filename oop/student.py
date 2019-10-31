class Student:
    # class attributes
    pythonfee = 10000
    javafee = 15000


    def __init__(self, name, course, feepaid=0):
        self.name = name
        self.course = course
        self.feepaid = feepaid

    @property
    def coursename(self):
        return 'Java' if self.course == 'j' else 'Python'

    def payment(self, amount):
        self.feepaid += amount

    @property
    def totalfee(self):
        return Student.javafee if self.course == 'j' else Student.pythonfee

    def get_due(self):
        if self.course == 'j':
            return Student.javafee - self.feepaid
        else:
            return Student.pythonfee - self.feepaid


s = Student("Larry","j",5000)
s.payment(5000)
print(s.coursename)
print(s.totalfee)