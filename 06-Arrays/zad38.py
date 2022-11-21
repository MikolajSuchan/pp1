def create_2d_arr(x,y):
    arr=[]
    for i in range(y):  
        arr.append(0)
    arr2=[]
    for i in range(x):
        arr2.append(arr)
    return print(arr2)

create_2d_arr(3,5)