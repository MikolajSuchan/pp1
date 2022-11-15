arr1=[5,1,9,6,1]
arr3=sorted(set(arr1))
max=0
druga=None
for i in arr3:
    if i>max:
        druga=max
        max=i
print(druga)