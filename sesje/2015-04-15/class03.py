# definicja klasy Liczba pochodnej od klasy int
class Liczba(int):
    pass

# klasa pochodna z klasy pochodnej :)
class LiczbaMagiczna(Liczba):

    def negacja(self):
        return -self

#    def zaneguj(self):
#        self.numerator *= -1

liczba_a = Liczba(11)
liczba_b = Liczba(22)

print('Klasa L:', Liczba)
print('Typy a i b:', type(liczba_a), type(liczba_b))
print('Instancje a i b:', liczba_a, liczba_b)
print('Suma a i b:', liczba_a + liczba_b)

liczba_magiczna = LiczbaMagiczna(123)

print('Klasa LM:', LiczbaMagiczna)
print('Negacja LM:', liczba_magiczna.negacja())

