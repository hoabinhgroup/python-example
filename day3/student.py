class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        print(f"Xin chào, tôi là {self.name}, {self.age} tuổi và tôi đang học tại {self.school}.")


student = Student("Nam", 22, "Hanoi University")
student.introduce()