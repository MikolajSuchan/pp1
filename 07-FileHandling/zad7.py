# display text file, line by line
count=1
file= open('countries.txt','r')
for line in file:
     print(count,line,end="")
     count+=1
file.close()
