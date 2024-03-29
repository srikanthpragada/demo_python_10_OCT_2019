class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Special method
    def __str__(self):
        return f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age


p1 = Person("Abc", 25)
p2 = Person("Abc", 20)
print(p1 > p2)
print(p1 == p2)
print(str(p1))
