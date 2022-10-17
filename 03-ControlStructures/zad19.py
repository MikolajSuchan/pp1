wiek=int(input("Wprowadź wiek psa w ludzkich latach:\n"))
if wiek<=2:
    psie=wiek*10.5
    print(f"Wiek psa w psich latach to {psie}")
else:
    psie=(wiek-2)*4+21
    print(f"Wiek psa w psich latach to {psie}")