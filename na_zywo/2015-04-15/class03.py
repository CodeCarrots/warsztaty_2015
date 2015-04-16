# definicja klasy Liczba pochodnej od klasy int
class Liczba(int):
    pass

# klasa pochodna z klasy pochodnej :)
class LiczbaMagiczna(Liczba):

    def negacja(self):
        print('self:', self, id(self))
        return -self

#    def negacja(self, x):
#        print('self:', self, id(self), x)
#        return -self

#    def zaneguj(self):
#        self.numerator *= -1

liczba_magiczna = LiczbaMagiczna(123)
print('LM:', liczba_magiczna, id(liczba_magiczna))

print('Klasa LM:', LiczbaMagiczna)
print('Negacja LM:', liczba_magiczna.negacja())
#x = 1
#x.negacja()

#liczba_magiczna.negacja('?')

liczba_x = Liczba(12)

