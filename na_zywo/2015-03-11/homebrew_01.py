# quiz

#resp = input('Jaka jest pierwsza litera alfabetu?')
#if resp in ['a', 'A']:
#    print('Odpowiedź OK.')
#else:
#    print('Zła odpowiedź!')

#resp = input('Jaka jest ostatnia litera alfabetu?')
#if resp in ['z', 'Z']:
#    print('Odpowiedź OK.')
#else:
#    print('Zła odpowiedź!')


def print_result(resp, choices):
    # resp - wartosc odp. usera
    # choices - prawidłowe odp.
    if resp in choices:
        print('Odpowiedź OK.')
    else:
        print('Zła odpowiedź!')

resp = input('Jaka jest pierwsza litera alfabetu?')
print_result(resp, ['a', 'A'])
resp = input('Jaka jest ostatnia litera alfabetu?')
print_result(resp, ['z', 'Z'])


def quiz(question, proper_answers):
    # Zadaje pytanie, sprawdza odp., wyświetla wynik testu
    # question - pytanie do usera
    # proper_answers - prawidłowe odp.
    user_response = input(question)
    print_result(user_response, proper_answers)

quiz('Jaka jest pierwsza litera alfabetu?', ['a', 'A'])
quiz('Jaka jest ostatnia litera alfabetu?', ['z', 'Z'])

