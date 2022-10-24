def power(x,n):
    if n==1:
        return x
    y=power(x,n-1)
    return x*y
print(power(5,3))