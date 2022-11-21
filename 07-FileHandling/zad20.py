import random
file=open("rand.txt","a")
for i in range(50):
    a=random.randrange(100,999)
    file.write(f"{a}\n")

file.close()