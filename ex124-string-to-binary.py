# Chaîne de caractères à convertir en binaire
text = "hello world"

def repr_bin(text, encoding):
    binary_octets = []
    for v in text.encode(encoding):
        binary_octets.append(bin(v)[2:].zfill(8))
    return ' '.join(binary_octets)

# Affiche la représentation binaire avec un espace entre chaque caractère
print(repr_bin(text, 'utf-8'))