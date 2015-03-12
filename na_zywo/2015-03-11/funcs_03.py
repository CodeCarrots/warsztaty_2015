## funkcje bez zwrotów

def show_msg(msg_str, announce='A message to you'):
    print(announce + ': ' + msg_str)

print('Użycia funkcji z argumentami, bez zwrotów ->')

show_msg('Talk!!')

show_msg('Yo!', "Beep! Beep! I'm just saying")

print()
print()
print()

def show_msg_more(msg_str, announce='A message to you', beep=True):
    print(announce + ': ' + msg_str, beep)

show_msg_more('Talk to me!', beep=False)
show_msg_more('Talk to me!')
show_msg_more('Talk to me!', beep=False, announce='Test?')

print()
print()
print()

def show_msg_all_def(a='a', b='b2'):
    print('a, b:', a, b)

show_msg_all_def('x')
show_msg_all_def('x', 'y')
show_msg_all_def()
show_msg_all_def('z', b='r')
#show_msg_all_def(b='r', 'z')
show_msg_all_def('z')
show_msg_all_def(b='tt')
#a, b: x b2
#a, b: x y
#a, b: a b2
#a, b: z r
#(błąd)
#a, b: z b2
#a, b: a tt




#(błąd)
#def show_msg_nall_def(obo, a='a', b='b2'):
#    print('obo, a, b:', obo, a, b)

#show_msg_nall_def(a='a', b='b2')


def dito_bel(a='aaa'):
    print('a:', a)

x = "234qqq3q14"
dito_bel(a=x)
dito_bel()
#(błąd!)
#dito_bel(d='aha!')



