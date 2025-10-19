
grade_list = []
student_num=int(input("Enter the number of students:"))

for i in range(student_num):
    
    name = input(f"Enter name of student {i+1}: ")
     
    gpa = float(input(f"Enter CSE110 GPA of {name}: "))
    
    student = [name, gpa]

    grade_list.append(student)
    
    print(grade_list)
