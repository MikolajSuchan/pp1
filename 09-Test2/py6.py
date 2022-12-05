import json
def f(age,course,average):
    file=open("test.json")
    data=json.load(file)
    count=0
    for student in data:
        if student['age']>=age:
            if 'studies' in student:
                for student_course in student['studies']['courses']:
                    if student_course['name']==course:
                        grade_sum=sum(student_course['grades'])
                        grade_count=len(student_course['grades'])
                        av=grade_sum/grade_count
                        if av>=average:
                            count+=1
    
    file.close()
    return count
print(f(21,"statistics",4))               