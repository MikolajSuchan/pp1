i=1
a=input("Podaj numer PIN:\n")
if a == '0805':
  print ("Podałeś prawidłowy PIN.")
else:
  while (a != '0805') and (i < 3):
    i += 1
    print ("Podałeś nieprawidłowy PIN. Spróbuj jeszcze raz!")
    a = input ("Podaj nr PIN: ")
if i == 3:
  print ("Wprowadzono trzy razy błędnie nr PIN. Karta została zablokowana.")