# definicja klasy bazowej Wielokat z metodami
class Wielokat:

    def suma_katow(self):
        print('<nieokreslona>')

    def odcinki(self):
        print('<dużo>')


# definicja klasy Czworokat pochodnej od klasy Wielokat
class Czworokat(Wielokat):

    def suma_katow(self):
        print('360 stopni')

    def odcinki(self):
        print('a, b, c, d')


wk = Wielokat()

print('Suma kątów wielokąta:')
wk.suma_katow()
print('Odcinki wielokąta:')
wk.odcinki()

ck = Czworokat()

print('Suma kątów czworokąta:')
ck.suma_katow()
print('Odcinki czworokąta:')
ck.odcinki()

