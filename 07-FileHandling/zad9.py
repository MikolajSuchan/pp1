sum=0
file=open('numbers.txt','r')
for i in file:
    sum=sum+int(i)

file.close()
print(sum)