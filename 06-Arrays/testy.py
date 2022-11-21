arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
count=1
for i in arr:
    for j in range(0,5):
        i[j]=count*(j+1)
    count+=1
    print(*i)