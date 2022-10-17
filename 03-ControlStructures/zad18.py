kwota=int(input("Wprowadź kwotę w PLN:\n"))
five=kwota//5
two=(kwota%5)//2
one=kwota-five*5-two*2
print(f"5zł-{five}\n2zł-{two}\n1zł-{one}")