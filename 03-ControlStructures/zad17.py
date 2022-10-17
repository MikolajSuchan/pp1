x=int(input("Wprowadź pierwszą współrzędną:\n"))
y=int(input("Wprowadź drugą współrzędną:\n"))
if x==0 and y==0:
    print(f"Punkt {x,y} leży na środku układu współrzędnych")
elif x==0:
    print(f"Punkt {x,y} leży na osi OY")
elif y==0:
    print(f"Punkt {x,y} leży na osi OX")
elif x>0 and y>0:
    print(f"Punkt {x,y} leży w I ćwiartce")
elif x<0 and y>0:
    print(f"Punkt {x,y} leży w II ćwiartce")
elif x<0 and y<0:
    print(f"Punkt {x,y} leży w III ćwiartce")
else:
    print(f"Punkt {x,y} leży w IV ćwiartce")