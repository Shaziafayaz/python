class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Shazia", 21)
s2 = Student("Ayesha", 20)

s1.details()
s2.details()