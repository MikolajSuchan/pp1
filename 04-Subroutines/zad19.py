n=int(input("Wprowadź liczbę:\n"))
def zakres(x,y):
    if n>x and n<y:
        return True
    else:
        return False
a=int(input("Wprowadź pierwszą liczbę zakresu:\n"))
b=int(input("Wprowadź Drugą liczbę zakresu:\n"))
zakres(a,b)
if zakres(a,b)==True:
    print(f"Liczba {n} znajduje się w zakresie <{a},{b}>")
else:
    print(f"Liczba {n} jest poza zakresem <{a},{b}>")