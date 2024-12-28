arr=[1,1,0,1,0,1,0]
s=[]
s1=[]
for i in arr:
    if i==0:
        s.append(i)
    elif i==1:
        s1.append(i)
s.extend(s1)
print(s)


#it only fix for 0 and 1
result=[]
for i in arr:
    if i==0:
        result.insert(i,0)
    else:
        result.append(i)
print(result)