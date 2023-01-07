import math

a = int(input("Podaj a\n>"))
b = int(input("Podaj b\n>"))
c = int(input("Podaj c\n>"))

if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie toższamościowe, nieskończona liczba rozwiązań")
        else:
            print("Brak rozwiązań")
    else:
        x = ((c/b) * (-1))
        print(f"Jedno rozwiązanie, x = {x}")
else:
    delta = (b**2 - (4 * a * c))
    if delta < 0:
        print("Brak rozwiązań")
    elif delta == 0:
        x = ((b / 2 * a) * (-1))
        print(f"Jedno rozwiązanie, x = {x}")
    elif delta > 0:
        x1 = ((b * (-1)) + math.sqrt(delta)) / (2 * a)
        x2 = ((b * (-1)) - math.sqrt(delta)) / (2 * a)
        print(f"Dwa rozwiązania, x1 = {x1}, x2 = {x2}")
