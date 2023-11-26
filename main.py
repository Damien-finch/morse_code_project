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


def abc_to_Morse():
    user_string = input("Enter the string you would like to convert to Morse: ").strip()

    key_compatible_list = [element.upper() if element.isalpha() and element.islower()
                           else element for element in user_string]

    return "    ".join([element if element in (" ", "!")
                        else MORSE_CODE_DICT.get(element, "##undefined char##") for element in key_compatible_list])


continue_input = True

while continue_input:
    print(abc_to_Morse())
    ask_continue = input("Convert another string? Type 'N' to end, any other key to continue: ").lower()
    if ask_continue == 'n':
        continue_input = False
