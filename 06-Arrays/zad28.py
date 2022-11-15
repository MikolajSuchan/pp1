def median(array):
    arr=sorted(array)
    if len(arr)%2==0:
        a=(arr[(len(arr)//2-1)]+arr[len(arr)//2])/2
        return print(a)
    else:
        return print(arr[(len(array)//2)])



median([1,2,3,4,5,6])