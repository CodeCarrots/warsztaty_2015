def print_all_points():
    '''Wyswietla liste punktow i wszystkie informacje o nich (wspolrzedne,
        etykiete oraz kolor)

    NOTE: Funkcja korzysta z globalnej listy/mapy punktów.
    '''
    pass


def get_user_point_info():
    '''Pobiera od użytkownika dane pojedynczego punktu: wspolrzedne (para liczb
        zmiennoprzecinkowych, etykiete (tekstowa, musi byc unikalna) oraz kolor
        (może byc ze zdefiniowanej listy)

    NOTE: Funkcja korzysta z globalnej listy/mapy punktów.
    '''
    pass


def move_point(point_name, point_xy_tuple):
    '''Przesuwa wskazany punkt na nowe wspolrzedne

    NOTE: Funkcja korzysta z globalnej listy/mapy punktów.
    '''
    pass


def move_point(point_name, point_xy_tuple):
    '''Przesuwa wskazany punkt na nowe wspolrzedne

    NOTE: Funkcja korzysta z globalnej listy/mapy punktów.
    '''
    pass


def add_point(point_xy_tuple, point_name, color='black'):
    '''Dodaje nowy punkt o zadanych współrzędnych, unikalnej etykiecie i kolorze;
        zwraca `True` jesli operacja sie udala

    NOTE: Funkcja korzysta z globalnej listy/mapy punktów.
    '''
    pass


# bez parametrów i użycia zwrotu
print_all_points()

# bez parametrów i ale z użyciem zwrotu
point_info = get_user_point_info()

# z parametrami (2 wymagane) ale bez użycia zwrotu
move_point('a', (0.5, -0.5))

# z parametrami (2 wymagane, 1 opcjonalny ale NIE NAZWANY) oraz użyciem zwrotu
operation_ok = add_point((0.1, -1.5), 'b', 'red')

# z parametrami (2 wymagane, 1 opcjonalny a przy tym NAZWANY) oraz użyciem zwrotu
operation_ok = add_point((0.1, -1.5), 'b', color='red')

# i tak dalej...

