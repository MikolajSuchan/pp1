def sumofnumb(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n/10)
    return sum
x=7124
print(sumofnumb(x))