#Static method

class Mathutils:
    @staticmethod
    def add(a,b):
        return a+b

    def multiply(a,b):
        return a * b
    

print(Mathutils.add(5,3))
print(Mathutils.multiply(5,3))


#Class method
class Studentinfo:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    @classmethod
    def from_string(cls, student_str):
        name, grade = student_str.split('-')
        return cls(name,grade)


s1 = Studentinfo("Bob" , "4th")
s2 = Studentinfo.from_string("Tom-6th")


print(s1.name, s1.grade)
print(s2.name, s2.grade)