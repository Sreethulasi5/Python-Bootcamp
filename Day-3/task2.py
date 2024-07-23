# password verification
'''
pwd=input()
caps="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small="abcdefghijklmnopqrstuvwxyz"
digits=1234567890
special_char="!@#$%^&*()_?"
all=caps+small+str(special_char)+str(digits)
for i in all:
    if len(pwd)>8 and all:
        print("valid password")
        break
    else:
        print("Invalid input")
'''
#2nd method
s=input()
ucount,lcount,dcount,scount=0,0,0,0
for c in s:
    if c.isupper():
        ucount+=1
    elif c.islower():
        lcount+=1
    elif c.isdigit():
        dcount+=1
    else:
        scount+=1
if len(c)>8 and ucount>0 and lcount>0 and dcount>0 and scount>0:
    print("valid password")
else:
    print("Invalid password")