## definicja i użycie funkcji przyjmującej jeden parametr

glob_lst = [12, 34]


def printx(arg):
    print("arg @ start:", arg)
    arg += " def"
    # ble!
#    glob_lst.append(100)
    print("stop (arg):", arg)
    print("stop (glob_lst):", glob_lst)


x = 'abc'
print('x, glob_lst (orig):', x, glob_lst)
printx(x)
print('x, glob_lst (orig?):', x, glob_lst)

print()
print()


## definicja i użycie funkcji przyjmującej trzy parametry

def many(arg1, arg2, arg3):
    print("arg1 @ start:", arg1)
    print("arg2 @ start:", arg2)
    print("arg3 @ start:", arg3)

y = 'frg'
many(y, 1, 3)

