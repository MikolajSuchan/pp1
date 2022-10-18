count=0
sum=0
a=int(input("Wprowadź liczbę\nLiczba 0 zakończy działanie programu jeśli nie była wprowadzona jako pierwsza:"))
if a==0:
    print("Muisz wprowadzić liczbę inną niż 0")
while a!=0:
    sum=sum+a
    count+=1
    a=int(input("Wprowadź liczbę:"))
    if a==0:
        break
print("Ilość",count,"Suma",sum,"Średnia",sum/count)