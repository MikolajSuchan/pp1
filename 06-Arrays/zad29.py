arr=[1,2,3,4,5,6,7,8,9,10]
a=int(input("Wprowadź liczbę:\n"))
count=0
for i in arr:
    if i>a:
        count+=1
print(count)