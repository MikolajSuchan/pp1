arr=[-15,8,-31,47,-2,19]
big=0
small=0
for i in arr:
    if i>big:
        big=i
    if i<small:
        small=i

print(big,small)