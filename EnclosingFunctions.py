#Enclosing functions maybe another words for nested functions.
#Nested functions are functions that are defined inside another function.
def hello():
    name = "John"
    def nicer_display():
        print("Hello {}".format(name.upper()))
    nicer_display()

hello()