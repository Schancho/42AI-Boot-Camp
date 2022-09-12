# Make a program that takes a string as argument and encode it into Morse code.
# • The program supports space and alphanumeric characters
# • An alphanumeric character is represented by dots . and dashes -:
# • A space character is represented by a slash /
# • Complete morse characters are separated by a single space
# If more than one argument are provided, merge them into a single string with each
# argument separated by a space character.
# If no argument is provided, do nothing or print an usage.

import sys

morse = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '/'
    }

def morse_code(s):
    for i in s:
        print(morse[i], end=' ')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        mrse = ' '.join(sys.argv[1:])
        for i in mrse:
            if i not in morse:
                print('ERROR')
                exit()
        morse_code(mrse)
        print()

    else:
        print('ERROR')


