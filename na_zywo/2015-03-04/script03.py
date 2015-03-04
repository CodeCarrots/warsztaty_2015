## definicja i użycie funkcji przyjmującej jeden parametr

g = 10

def printx(arg):
    print("arg @ start:", arg)
    arg += " def"
    print("stop:", arg)

x = 'abc'
printx(x)

print()
print()


## definicja i użycie funkcji przyjmującej trzy parametry

def many(arg1, arg2, arg3):
    print("arg1 @ start:", arg1)
    print("arg2 @ start:", arg2)
    print("arg3 @ start:", arg3)

y = 'frg'
many(y, 1, 3)

