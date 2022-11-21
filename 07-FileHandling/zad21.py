file=open("liczby.txt","a")
for i in range(1,11):
    file.write(f"{i},{i*i},{i*i*i}\n")
file.close()