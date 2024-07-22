# keys are ages,values are votes
congress={
    7:5,
    18:22,
    32:8,
    71:5,
    66:6
}
bjp={
    7:15,
    18:20,
    32:4,
    71:9,
    66:2
}
c_sum=0
b_sum=0
for age,votes in congress.items():
    if age>=18:
        c_sum+=votes
print("total congress votes are:",c_sum)
for age,votes  in bjp.items():
    if age>=18:
        b_sum+=votes
print("total BJP votes are:",b_sum)
diff=abs(c_sum-b_sum)
if c_sum>b_sum:
    print('congress win by:', diff)
else:
    print('Bjp win by', diff)
print() 
