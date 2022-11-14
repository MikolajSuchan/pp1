arr=[1,2,3,4,5,6,7,8,9,10]
even=0
odd=0
i=0
while i!=len(arr):
    if arr[i]%2==0:
        even+=1
        i+=1
    if arr[i]%2!=0:
        odd+=1
        i+=1

print(even,odd)