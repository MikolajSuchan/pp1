a=input("Wprowadź produkt do kupienia:\n")
lista=open('shooping.txt','a')
lista.write(f"{a}\n")
lista.close()