# Binaire à convertir en texte.
binary_code = "01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100"

# Fonction pour convertir une chaîne binaire en texte
def binary_to_text(binary_code):
    # Séparer la chaîne binaire en octets (groupes de 8 bits)
    binary_values = binary_code.split(' ')

    # Convertir chaque octet en caractère
    text = ''.join(chr(int(b, 2)) for b in binary_values)

    return text

print(binary_to_text(binary_code))