def f(n):
    cal=n//5
    cze=n%5
    if n<=0:
        return ""
    elif n%5==0:
        return (cal-1)*"/////-"+"/////"
    else:
        return cal*"/////-"+cze*"/"

print(f(-8))