wzrost=int(input("Podaj swój wzrost w centymetrach:\n"))
waga=int(input("Podaj swoją wagę w kilogramach:\n"))
wz=wzrost/100
bmi=round(waga/wz**2,0)
print(f"Twój wskaźnik bmi wynosi {bmi}")