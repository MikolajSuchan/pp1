def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubblesort([1,8,3,5,7,2]))
print(bubblesort([8,76,4,345,534,5]))
print(bubblesort([23,345,2,245,64]))