student = {"name": "Selim","age":19}
student2 = {"name": "Peter","age":20}
student3 = {"name": "Mark","age":21}

if student["age"] > 20:
    print("Old student")
else:
    print("Young student")

print("\n***************\n")

def tell_me_if_student_id_old(x):
    if x["age"] > 20:
        print("Old student")
    else:
        print("Young student")

tell_me_if_student_id_old(student)
tell_me_if_student_id_old(student2)
tell_me_if_student_id_old(student3)

def greeting(name):
    print("Hello", name)

print("\n***************\n")

greeting("Ege")