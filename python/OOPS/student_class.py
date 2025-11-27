class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display_info(self):
        print(f"Student name: {self.name}")
        print(f"Student grade: {self.grade}")


student1 = Student("Mat", "6th")
student2 = Student("Tom", "9th")


student1.display_info()