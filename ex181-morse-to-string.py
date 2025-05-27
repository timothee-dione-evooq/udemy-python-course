# Dictionnaire pour convertir les caractères en code Morse.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

# Chaîne de caractères à convertir en code Morse.
morse_code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
morse_chars = morse_code.split()
normal_text = ""

for char in morse_chars:
    if char == '/':
        normal_text += ' '
    else:
        for key, value in morse_code_dict.items():
            if value == char:
                normal_text += key
                break
print(normal_text)

