cm=int(input("Podaj ile masz centymetrów wzrostu:"))
cale=cm*0.3937
ft=int(cale)//12
cal=int(round(cale-ft*12,0))
print(f"Przeliczając masz {ft} stóp oraz {cal} cali")