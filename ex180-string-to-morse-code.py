# Dictionnaire pour convertir les caractères en code Morse.
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': ' '
}

# Chaîne de caractères à convertir en code Morse.
text = "hello world"
morse_string = ""
for char in text:
    if char.upper() in morse_code_dict:
        morse_string += morse_code_dict[char.upper()]
        if text.index(char) < len(text) - 1:
            morse_string += ' '
print(morse_string)