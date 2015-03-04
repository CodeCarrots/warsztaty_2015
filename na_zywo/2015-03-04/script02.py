## prosta definicja funkcji i jej użycie

def printx():
    print("stop!")

printx()
print('--')
printx()
printx()
printx()
print('przed - printx')
# brak wywołania - nic się nie dzieje
printx
print('po - printx')

x = 1
print('przed - x')
# brak wywołania (wywołanie niemożliwe bo to `int`) - też nic się nie dzieje
x
print('po - x')
