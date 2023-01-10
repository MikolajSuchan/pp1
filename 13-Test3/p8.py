class C:
    def __init__(self,dic):
        self.dic=dic

    def m(self,n):
        last=[]
        students=self.dic.items()
        for student in students:
            a=sum(student[1])
            b=len(student[1])
            c=a/b
            if c>=n:
                last.append(student[0])
        bef=sorted(last)
        return print(",".join(bef))



s = C({"Peter":[4,5,4], "Harry":[2,5], "Barbara":[3,3,3,5,5,5]})
s.m(3)