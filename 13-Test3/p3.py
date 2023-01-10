import re

def f1(t):

    data = re.findall(r'(\w+) is (\d+)', t)

    data.sort(key=lambda x: x[0])

    return {name: int(age) for name, age in data}

def f2(d):

    return sum(d.values())

print(f1("Mark is 24 and Ann is 27"))
print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!"))
print(f2(f1("Mark is 24 and Ann is 27")))
print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")))
