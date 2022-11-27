import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
count=0
sum=0
for i in temperatures:
    sum=sum+int(i)
    count+=1
print(f"Średnia to:{sum/count}")