a=input("Wprowadź nazwę pliku:\n")
count=0
with open(f'{a}','r') as f:
    for i in f:
        count+=1
f.close()
print(f"File name:{a}")
print(f"Number of lines:{count}")