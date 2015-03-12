'''
Dla czytelnosci funkcje "nie uzywaja" parametru listy, na ktorej operujemy czyli de facto korzystaja z globalnej listy/mapy punktow. Nie jest to zbyt eleganckie (zasada ograniczania oeracji do zmiennych bedacych argumentami lub/i zmiennymi lokalnymi).

Aby to poprawic wystarczy dodac do wszystkich funkcji (w definicjach jak i wywolaniach; za wyjatkiem funkcji `get_user_point_info`) dodatkowy, obowiazkowy parametr do przekazywania tej listy z punktami. Przyklady:

all_our_points = []

def print_all_points(all_points):
    pass

def move_point(all_points, point_name, point_xy_tuple):
    pass

# (...)

print_all_points(all_our_points)
move_point(all_our_points, 'a', (0.5, -0.5))
'''

def print_all_points():
    '''Wyswietla liste punktow i wszystkie informacje o nich (wspolrzedne,
        etykiete oraz kolor)
    '''
    pass


def get_user_point_info():
    '''Pobiera od uzytkownika dane pojedynczego punktu: wspolrzedne (para liczb
        zmiennoprzecinkowych, etykiete (tekstowa, musi byc unikalna) oraz kolor
        (moze byc ze zdefiniowanej listy) i je zwraca w postaci krotki
    '''
    pass


def move_point(point_name, point_xy_tuple):
    '''Przesuwa wskazany punkt na nowe wspolrzedne
    '''
    pass


def add_point(point_xy_tuple, point_name, color='black'):
    '''Dodaje nowy punkt o zadanych współrzędnych, unikalnej etykiecie i kolorze;
        zwraca `True` jesli operacja sie udala
    '''
    pass


# bez parametrów i uzycia zwrotu
print_all_points()

# bez parametrów i ale z uzyciem zwrotu
point_info = get_user_point_info()

# z parametrami (2 wymagane) ale bez uzycia zwrotu
move_point('a', (0.5, -0.5))

# z parametrami (2 wymagane, 1 opcjonalny ale NIE NAZWANY) oraz uzyciem zwrotu
operation_ok = add_point((0.1, -1.5), 'b', 'red')
operation_ok = add_point(point_info[0], point_info[1], point_info[2])
#operation_ok = add_point(*point_info)

# z parametrami (2 wymagane, 1 opcjonalny a przy tym NAZWANY) oraz uzyciem zwrotu
operation_ok = add_point((0.1, -1.5), 'b', color='red')

# i tak dalej...

