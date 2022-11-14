arr=[15, 8, 31, 47, 2, 19]
print(arr)
count=0
sum=0
for i in arr:
    sum=sum+i
    count+=1
print(f"{sum/count}")