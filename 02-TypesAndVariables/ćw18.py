import math
a=int(input("Podaj długość pierwszego boku:\n"))
b=int(input("Podaj długośc drugiego boku\n"))
c=int(input("Podaj długość trzeciego boku\n"))
p=int((a+b+c)/2)
s=int(math.sqrt(p*(p-a)*(p-b)*(p-c)))
print(f"Pole wynosi {s} jednostek kwadratowych")