class Student:
    def __init__(self,name,roll,branch,email):
        self.name=name
        self.roll=roll
        self.branch=branch
        self.email=email
    def display(self):
        print('name is :',self.name)  # str->8
        print('roll is : ',self.roll)  #int->4
        print('branch is : ',self.branch)   # str->8
        print('email is :', self.email)  #str->8
s1=Student('thulasi',523,'cse','thulasi@gmail.com')
s1.display()



