# to reduce the memory allocation
class Student:
    # we are 
    branch="CSE"
    def __init__(self,name,roll,email):
        self.name=name
        self.roll=roll
        self.email=email
    def display(self):
        print('name is :',self.name)  # str->8
        print('roll is : ',self.roll)  #int->4
        print('branch is : ',Student.branch)   # str->8
        print('email is :', self.email)  #str->8
s1=Student('thulasi',523,'thulasi@gmail.com')
s1.display()