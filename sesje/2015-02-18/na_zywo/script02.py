# str
a = 'abcdef'
b = 'GHIJK'
print(a, b)

x = a + b
print(x)

x = a
x = x + b
print('a+b (v1):', x)

x = a
x += b
print('a+b (v2):', x)

print()

# multiplikacja
a = 'aBcD'
N = 5
x = a * N
print('x=a*N:', x)

print()

# łamanie vel kawałkowanie (ang. slice)
a = 'aBcDe'
#    0123   len(a)==4
print('len(a)=', len(a))
print('len(a) == 4 ?', len(a) == 4)

print('a =', a)
print('a[0]=', a[0])
print('a[3]=', a[3])

print('a[-1]=', a[-1])
print('a[-2]=', a[-2])
print('a[-4]=', a[-4])

#!!! a[0] = 'x'

# all
print('a[0:]=', a[0:])
print('a[:]=', a[:])
# frag.
x = 1
y = 3
print('a[x:y+1]=', a[x:y+1])

print('a[x:]=', a[x:])

#!!! print('a[9]=', a[9])

print()

a = 'Ala ma kota a reszta?'
print('a=', a)
print('len(a)=', len(a))

# fragment od pocz. do elem. na indeksie 9
print('a[0:10]=', a[0:10])
# fragment od pocz. do elem. na indeksie 9, co drugi znak
print('a[0:10:2]=', a[0:10:2])

# polowa ciagu (int obcina czesc ulamkowa)
p = int(len(a) / 2)
# znak na indeksie p
print('a[p]=', a[p])

# nieprawidowe indeksy:
print('!!! a[p:0:-2]=', a[p:0:-2])
print('!!! a[p:-1:-2]=', a[p:-1:-2])
print('!!! a[p:21:-2]=', a[p:21:-2])

# wyciecie wstecz od indeksu p, co drugi znak
print('a[-(p+1)::-2]=', a[-(p+1)::-2])
print('a[p::-2]=', a[p::-2])

# odwracanie ciagu
print('a[::-1]=', a[::-1])

# łamanie wyświetlanego tekstu znakiem kontrolnym \n
print('tekst pierwszej linii\ntekst drugiej linii...')

