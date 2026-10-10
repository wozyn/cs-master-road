class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        
        print(f"My name is {self.name}, age is {self.age}")
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score
    def show_score(self):
        print(f"Score: {self.score}")
student = Student("Alice", 23, 90)
student.introduce()
student.show_score()