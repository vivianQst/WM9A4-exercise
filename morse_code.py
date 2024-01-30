"""
Morse Code Translator Function

Objective:
Write a function named 'morse_translator' that translates a given string into Morse code.

Function Parameter:
text (string): The string to be translated into Morse code.

Instructions:
- Each alphabetic character in the string should be translated to its corresponding Morse code equivalent.
- The Morse code for each character should be separated by a space.
- Each word in the string should be separated by a forward slash (/).
- The function should handle both uppercase and lowercase alphabetic characters.
- The function should be case-insensitive, meaning it treats uppercase and lowercase letters the same.
- Non-alphabetic characters (like numbers or symbols) should not be translated.
- https://en.wikipedia.org/wiki/Morse_code

Example Test Cases:
1. morse_translator("HELLO WORLD") should return the Morse code for the given string.
2. morse_translator("Python") should return the Morse code for the given string.
3. morse_translator("Morse Code") should return the Morse code for the given string.
"""


def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    # Your code goes here
    text = text.upper()
    
    morse_result = []  # List to store Morse code for each word
    
    # Translate each word to Morse code
    words = text.split()  # Split text into words
    for word in words:
        morse_word = []  # List to store Morse code for each character in the word
        for char in word:
            if char.isalpha():
                morse_word.append(morse_code_dict[char])
        morse_result.append(' '.join(morse_word))  # Join Morse code of characters with space for each word
    
    # Join Morse code of words with forward slash
    morse_text = ' / '.join(morse_result)
    
    return morse_text
    # Remember to consider both upper and lower case letters, and spaces
    # The function should return the translated Morse code string


# Test cases
print("test 1:",morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print("test 2:",morse_translator("Python"))  # Expected output: ".--. -.-- - .... --- -."
print("test 3:",morse_translator("Morse Code"))  # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
