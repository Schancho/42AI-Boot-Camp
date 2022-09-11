import sys
import string



def text_analyzer(arg):
    """    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""
    if not isinstance(arg, str):
        print("AssertionError: argument is not a string")
        return
    upper = 0
    lower = 0
    num = 0
    punc = 0
    space = 0
    
    for i in arg:
        if i.isupper():
            upper = upper + 1
        if i.islower():
            lower = lower + 1
        if i in string.punctuation:
            punc = punc + 1
        if i == ' ':
            space = space + 1
    print("The text contains " + str(len(arg)) + " character(s):")
    print("- " + str(upper) +" upper letter(s)")
    print("- " + str(lower) + " lower letter(s)")
    print("- " + str(punc) + " punctuation mark(s)")
    print("- " + str(space) + " space(s)")

if len(sys.argv) > 2:
    print("Usage: please Enter just one argument!")
    exit()
if __name__ == "__main__":
    text_analyzer(str(sys.argv[1]))