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

print("\n***************\n")

def greeting(name):
    print("Hello", name)

greeting("Ege")

print("\n***************\n")

def sum(x,y):
    return x + y

result = sum(6,7)

print(result)

print("\n***************\n")

def is_dividable(x, y):
    if x % y == 0:
        return (x, "is dividable by", y)
    else:
        return (x, "is not dividable by", y)
    
print(is_dividable(10, 2))

print(is_dividable(10, 3))



