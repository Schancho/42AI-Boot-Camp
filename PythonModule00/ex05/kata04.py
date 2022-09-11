kata = (23, 94, 132.42222, 10000, 12345.67)

arg  = ""
arg += "module_" + str(kata[0]).zfill(2) + ", "
arg += "ex_" + str(kata[1]).zfill(2) + " : "
arg += str(format(kata[2], ".2f")) + ", "
arg += str(format(kata[3], "4.2e")) + ", "
arg += str(format(kata[4], "4.2e"))
print(arg)