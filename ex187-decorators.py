def my_decorator(func):
    def wrapper():
        print("Début de l'exécution de la fonction")
        func()
        print("Fin de l'exécution de la fonction")
    return wrapper

@my_decorator
def hello():
    print("Hello, World!")

# Appel de la fonction décorée
hello()
