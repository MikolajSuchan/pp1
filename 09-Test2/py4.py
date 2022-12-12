def f(dictionary,x,y):
    sum=0
    for i in dictionary:
        p=dictionary.get(i)
        for j in p:
            if j>=x and j<=y:
                sum+=j
    return sum




print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10) )