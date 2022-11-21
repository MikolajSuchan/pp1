count=0
f=open('lorem.txt','r')
a=f.read()
for i in a:
    print(i)
    count+=1
        

f.close()