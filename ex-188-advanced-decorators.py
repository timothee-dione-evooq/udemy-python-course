# Définition du décorateur
def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

# Application du décorateur
@call_counter
def sample_function():
    pass  # Fonction vide

# Appels
sample_function()
sample_function()

# Affichage du compteur
print(f"La fonction a été appelée {sample_function.call_count} fois.")
