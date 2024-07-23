class Employee:
    company="Wipro"
    location="Bangloor"
    
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def __str__(self):
        return f'{self.name} {self.id} {self.salary} {Employee.company} {Employee.location}'
s1=Employee('ramu',1002,100000)   # s1 is a obj
print(s1)