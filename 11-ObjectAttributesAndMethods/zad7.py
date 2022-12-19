class Student():

    uni="UEK Kraków"
    count=100000
    
    def __init__(self, name,surename,field_of_study):
        self.name=name
        self.surename=surename
        self.field_of_study=field_of_study
        self.id=Student.count
        Student.count+=1
    
    def __str__(self):
        data=f"{self.name} {self.surename} {self.id} {self.field_of_study} {Student.uni}"
        return data

student1=Student("Mikołaj","Suchan","Informatyka stosowana")
student2=Student("Marta","Styczeń","Informatyka stosowana")
student3=Student("Jakub","Wilk","Informatyka stosowana")
print(student1)
print(student2)
print(student3)