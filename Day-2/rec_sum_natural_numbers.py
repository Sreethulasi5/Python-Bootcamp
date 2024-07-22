#sum of natural numbers
def sum_of_natural_no(n):
    if n==1:
        return 1
    else:
        return n+sum_of_natural_no(n-1)
n=int(input())
print(sum_of_natural_no(n))