def isPrime(n):
    if(n==1 or n==0):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True
n=int(input("Wprowadź liczbę do której mają zostać znalezione liczby pierwsze:\n"))
for i in range(1,n+1):
    if(isPrime(i)):
        print(i,end=" ")
