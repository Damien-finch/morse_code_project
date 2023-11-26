MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

# Reverse the dictionary to create a mapping from Morse code to characters
MORSE_CODE_REVERSE = {value: key for key, value in MORSE_CODE_DICT.items()}


def abc_to_Morse():
    user_string = input("Enter the string you would like to convert to Morse: ").strip()

    key_compatible_list = [element.upper() if element.isalpha() and element.islower()
                           else element for element in user_string]

    return "    ".join([element if element in (" ", "!")
                        else MORSE_CODE_DICT.get(element, "##undefined char##") for element in key_compatible_list])


def morse_to_abc():
    user_morse = input("Enter the Morse code you would like to convert to text: ").strip()

    morse_list = user_morse.split("    ")  # Split Morse code by 4 spaces

    return "".join([MORSE_CODE_REVERSE.get(element, "##undefined Morse##") for element in morse_list])


continue_input = True

while continue_input:
    conversion_type = input("Choose conversion type ('abc' for text to Morse, 'morse' for Morse to text, 'exit' to end): ").lower()

    if conversion_type == 'abc':
        print(abc_to_Morse())
    elif conversion_type == 'morse':
        print(morse_to_abc())
    elif conversion_type == 'exit':
        continue_input = False
    else:
        print("Invalid choice. Please enter 'abc', 'morse', or 'exit'.")
