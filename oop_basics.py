class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show_info(self):
        print(f"Name: {self.name}, Score: {self.score}")
    def is_pass(self):
        return self.score >= 60
    def update_score(self, new_score):
        self.score = new_score


student1 = Student("Alice", 85)
student1.show_info()
student2 = Student("Bob", 92)
student2.show_info()
student3 = Student("Charlie", 78)
student3.show_info()
print(student1.is_pass())
print(student2.is_pass())
print(student3.is_pass())
student4 = Student("David", 55)
print(student4.is_pass())
student1.update_score(95)
student1.show_info()

