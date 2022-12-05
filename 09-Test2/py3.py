def f(array2D):
    lista=[sum(i) for i in zip(*array2D)]
    
    return lista
print(f([ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]) )