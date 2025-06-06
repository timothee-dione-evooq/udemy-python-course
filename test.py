def my_decorator(func):
    def wrapper():
        print("Début de l'exécution de la fonction")
        func()
        print("Fin de l'exécution de la fonction")
    return wrapper

@my_decorator
def hello():
    print("Hello, World!")

def hello_decorator(func):
    def wrapper(name):
        return "Hello, " + func(name)
    return wrapper

@hello_decorator
def get_name(name):
    return name

# Appel de la fonction décorée
hello()

# Appel de la fonction décorée
print(get_name("John"))
