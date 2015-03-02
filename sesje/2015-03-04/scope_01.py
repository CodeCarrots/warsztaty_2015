# testy wg kolejności:
# `ok == True` jeśli wiek jest prawidłowy (1 rok to minimum)
# `adult == True` jeśli dorosły
# `teen == True` jeśli nastolatek
ok = False
while not ok:
    age = int(input('Podaj swój wiek w latach: '))

    teen = False
    if age <= 0:
        ok = False
    else:
        ok = True
        if age >= 13:
            teen = True
        elif age >= 18:
            adult = True

    if ok:
        if adult:
            print('Jesteś dorosła/ły.')
        elif teen:
            print('Jesteś nastolatką/kiem.')
        else:
            print('Jesteś dzieckiem.')
    else:
        print('Podałaś/łeś nieprawidłowy wiek.')

