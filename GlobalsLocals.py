#How to modify global variables inside a function?
#Use the global keyword to declare that variable as global.
x = 5
def add_10():
    global x
    x += 10

add_10()
print(x)
#However, it is not recommended to use global variables inside functions. Because it makes the code harder to debug and dangerous to use.