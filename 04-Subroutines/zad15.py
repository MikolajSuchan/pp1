import mymath
x=mymath.read_number()
y=mymath.generate_number()
print(f"{x} and {y}")
while True:
    if x==y:
        print("You win")
        break
    else:
        print("Not this time")