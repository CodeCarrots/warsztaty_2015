## przerzucanie zawatości sekwencji na zbiór indywidualnych zmiennych

# sekwencja
lista = [5, 6, 7]
print('lista (przed):', lista)

# przypisanie wartości z listy do zmiennych jedna po drugiej
a = lista[0]
b = lista[1]
c = lista[2]

print('a,b,c (przed):', a, b, c)

# zmiana jednej zmiennej
a += 1

print('a,b,c,lista (po):', a, b, c, lista)

# zapis wartości ze zmiennej z powrotem do listy
lista[0] = a
print('lista (po):', lista)

