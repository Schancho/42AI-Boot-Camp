import sys

def checkInt(str):
    if str[0] in ('-', '+'):
        return str[1:].isdigit()
    return str.isdigit()

if len(sys.argv) < 3 or len(sys.argv) == 1:
    print("Error: please Enter 2 digits!")
    exit()
if len(sys.argv) > 3:
    print("Error: Too many arguments!")
    exit()
if (not checkInt(str(sys.argv[1]))) or (not checkInt(str(sys.argv[2]))):
    print("Error: please enter valid integers!")
    exit()
print("Sum:         " + str(int(sys.argv[1]) + int(sys.argv[2])))
print("Difference:  " + str(int(sys.argv[1]) - int(sys.argv[2])))
print("Product:     " + str(int(sys.argv[1]) * int(sys.argv[2])))
if int(sys.argv[2]) != 0:
    print("Quotient:    " + str(int(sys.argv[1]) / int(sys.argv[2])))
else:
    print("Quotient:    ERROR (division by zero)")
if int(sys.argv[2]) != 0:
    print("Remainder:   " + str(int(sys.argv[1]) % int(sys.argv[2])))
else:
    print("Remainder:   ERROR (division by zero)")
