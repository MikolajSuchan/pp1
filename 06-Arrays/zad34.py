arr1=[2,4,6,8]
arr2=[1,2,3,4,5,6,7,8,9,10]
count=0
for i in arr1:
    if i in arr2:
        count+=1
    
if count==len(arr1):
    print(True)
else:
    print(False)