def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+sum(n-1)
x=10
print(f"Sum is {sum(x)}")