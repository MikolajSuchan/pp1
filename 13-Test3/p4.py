def f(d):
    incar=[]
    for i in d:
        if i[1]=="in":
            incar.append(i[0])
        elif i[1]=="out":
            incar.remove(i[0])
    return sorted(incar)
print(f([["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
["BA111","in"],["BA123","out"],["KR234","in"]]
))