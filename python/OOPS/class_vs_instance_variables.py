class Company:
    name = "NASA"   #class variable, changing this will reflect in all instances
    
    def __init__(self, dept, employee_name):
        self.dept = dept
        self.employee_name = employee_name

    
Employee1 = Company("IT", "Mat") #instance variable , change will be reflected on this particular instance
Employee2 = Company("HR", "Kendrick")

print(Employee1.name)
print(Employee2.name)
        