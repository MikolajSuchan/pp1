class C:
    def __init__(self):
        pass
    @staticmethod
    def m1(n):
        bas=str(n)
        back=[]
        for i in bas:
            if int(i)%2==0:
              back.append(i)  
        a="".join(back)
        return int(a)

    @staticmethod
    def m2(n):
        bas=str(n)
        pre=0
        for i in bas:
            if int(i)<int(pre):
                return False
            else:
                pre=i
        return True       
        
    @staticmethod
    def m3(n):
        bas =set(str(n))
        wyh=["0","1","2","3","4","5","6","7","8","9"]
        for i in bas:
            wyh.remove(i)
        a="".join(wyh)
        return str(a)
                
print(C.m1(4231564))
print(C.m1(79381))
print(C.m2(125579))
print(C.m2(4557879))
print(C.m3(23557))
print(C.m3(12340))
