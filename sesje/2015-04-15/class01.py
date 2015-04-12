# definicja klasy bazowej Wielokat
class Wielokat:
    pass


# definicja klasy Czworokat pochodnej od klasy Wielokat
class Czworokat(Wielokat):
    pass


wk = Wielokat()
ck = Czworokat()
xk = wk

print('wk:', wk)
print('ck:', ck)
print('xk:', xk)

