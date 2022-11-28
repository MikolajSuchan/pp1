countries=[{"country":"Poland","population": 30000000},{"country":"Germany","population":40000000},{"country":"China","population":90000000},{"country":"Ekwador","population":15000000},{"country":"USA","population":100000000},]
count=0
while count<len(countries):
    for key,value in countries[count].items():
        print(value,end=" ")
    print()
    count+=1