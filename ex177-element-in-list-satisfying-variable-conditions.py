def find_first_index(lst, condition):
    for i, val in enumerate(lst):
        if condition(val):
            return i
    return -1  # Retourne -1 si aucun élément ne vérifie la condition

# Test avec la condition "divisible par 4"
lst = [1, 3, 7, 9, 12, 15, 18]
condition = lambda x: x % 4 == 0

index = find_first_index(lst, condition)
print(index)