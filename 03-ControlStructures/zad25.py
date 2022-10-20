a=int(input("Wprowadź liczbę jednostek Szerokości:\n"))
b=int(input("Wprowadź liczbę jednostek długości:\n"))
for i in range(b):
    print("*",end="")
print()
for k in range(a-2):
    print("*"," "*(b-4),"*")
for i in range(b):
    print("*",end="")