students = { '31232':[], '1233':[5,3] }


def give_5(student_number):
    students[student_number].append(5)
    return f"new notes for student '{student_number}' are '{', '.join(map(str, students[student_number]))}'"
    
student = give_5('31232')
print(student)