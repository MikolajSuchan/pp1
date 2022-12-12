
def f(array2D):
    count=0
    last=0
    lista=[]
    for i in array2D:
        d=sum(i)
        lista.append(d)
    c=min(lista)
    for j in lista:
        if j==c:
            return count
        else:
            count+=1