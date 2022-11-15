arr=[6,8,1,9,2,5,3,4,10,7]
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
       if arr[j]%2!=0:
        arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)