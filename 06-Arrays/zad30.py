def minmax(array):
    arr=sorted(array)
    a=[]
    a.append(arr[0])
    a.append(arr[(len(arr)-1)])
    return print(a)

minmax([4,2,8,4,7,9,5])