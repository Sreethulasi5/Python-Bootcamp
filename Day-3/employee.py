class Employee:
    company="Wipro"
    location="Bangloor"
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def show(self):                 # it is a fun to display
        print('Name :',self.name)
        print('ID no :',self.id)
        print('salary :',self.salary)
        print('company :',Employee.company)
        print('location :',Employee.location)

s1=Employee('ramu',1002,100000)   # s1 is a obj
s1.show()