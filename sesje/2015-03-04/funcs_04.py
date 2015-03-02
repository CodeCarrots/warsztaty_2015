## funkcje ze zwrotami

def ask_user(msg_str, valid_choices):
    response = ''
    while not response or response not in valid_choices:
        response = input(msg_str + ', możliwe wartości to ' + str(valid_choices) + ': ').strip()
    return response

print('Użycia funkcji z argumentami oraz zwrotami ->')
user_resp = ask_user('Wybierz symbol (1)', ('a', 'A', 'b', 'B', 'c', 'C'))
print('Odp. usera (1):', user_resp)
user_resp = ask_user('Wybierz symbol (2)', 'aAbBcC')
print('Odp. usera (2):', user_resp)

