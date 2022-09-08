# from curses.ascii import isdigit
import sys

def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

if len(sys.argv) > 2:
    print("Usage: please Enter just one argument!")
    exit()
elif len(sys.argv) == 1:
    print("Usage: there is no argument provided!")
    exit()
string = str(sys.argv[1])
if not (checkInt(string)):
    print("AssertionError: argument is not an integer")
    exit()
num = int(string)
if num %2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")

