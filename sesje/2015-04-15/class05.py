# Mając klasy Prostokat oraz Kwadrat (patrz: class04.py) dodać do nich metody
# liczące przekątne; nie twórz klas na nowo - spróbuj je zaimportować pod inną
# nazwą z modułu `class04` i stwórz swoje "nowe" klasy Prostokat oraz Kwadrat korzystając
# z dziedziczenia

# (tu wstaw swój kod)

pk = Prostokat(2, 4)
print('Prostokąt o rozmiarach', pk.bok_a, 'x', pk.bok_b, 'i jego przekątna:', pk.przekatna())

kw = Kwadrat(4)
print('Kwadrat o boku', kw.bok, 'i jego przekątna:', kw.przekatna())

