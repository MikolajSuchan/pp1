import csv
with open("students.txt") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for i in csvreader:
        if int(i[2])<30:
            print(i[0],i[1],i[4])