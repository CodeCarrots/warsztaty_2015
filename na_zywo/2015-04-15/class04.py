class Czworokat:
    def __init__(self):
        self.nazwa = ''

    def pole(self):
        return '???'


class Prostokat(Czworokat):
    def __init__(self, bok_nr_1, bok_nr_2):
        self.bok_a = bok_nr_1
        self.bok_b = bok_nr_2
#        x = bok_nr_1

    def pole(self):
        return self.bok_a * self.bok_b


class Kwadrat(Prostokat):
    def __init__(self, odcinek):
        self.bok_a = self.bok_b = odcinek


ck = Czworokat()
print('Czworokąt i jego pole:', ck.pole())

pk = Prostokat(2, 4)
print('Prostokąt o rozmiarach', pk.bok_a, 'x', pk.bok_b, 'i jego pole:', pk.pole())

kw = Kwadrat(4)
print('Kwadrat o boku', kw.bok, 'i jego pole:', kw.pole())


pk.bok_a = 10
print('Prostokąt" o rozmiarach', pk.bok_a, 'x', pk.bok_b, 'i jego pole:', pk.pole())

