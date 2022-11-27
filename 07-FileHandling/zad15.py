count=0
f=open('lorem.txt','r')
for i in f:
    print(i)
    count+=1
    if count%5==0:
        x=input("Mussz wcisnąć Enter by wyświetlić dalszą zawartość")

f.close()