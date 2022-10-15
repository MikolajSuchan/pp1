import random
rzut=random.randrange(1,7)
a=int(input("Postaraj się zgadnąć liczbę od 1 do 6 którą wylosował komputer;\n"))
if rzut==a:
    print(True)
else:
    print("Nie tym razem")