# Połącz dwa słowniki title_to_author i title_to_shelf_number w jeden, przechowywany w zmiennej title_to_book_record
# Słownik title_to_author przechowuje pary: "tytuł książki" : "imię głównego authora"
# Słownik title_to_shelf_number przechowuje part: "tytuł książki" : "numer półki"
#
# Wynikowy słownik title_to_book_record powinien przechowywać pary: "tytuł książki" : 2 ELEMENTOWA KROTKA ("imię głównego autora", "numer półki")
#
# PRZYKŁAD:
# Dla klucza 'The C Programming Language' słownik 'title_to_book_record' powinien zwrócić krotkę: ('Brian W. Kernighan', 23)
# Czyli, w interpreterze Pythona:
# >>> title_to_book_record['The C Programming Language']
# >>>('Brian W. Kernighan', 23)

title_to_author = {'Structure and Interpretation of Computer Programs' : 'Harold Abelson',
                   'Introduction to Algorithms' : 'Thomas H. Cormen',
                   'The C Programming Language' : 'Brian W. Kernighan',
                   'The Pragmatic Programmer: From Journeyman to Master' : 'Andrew Hunt',
                   'Art of Computer Programming' : 'Donald Ervin Knuth',
                   'Design Patterns: Elements of Reusable Object-Oriented Software' : 'Erich Gamma',
                   'Artificial Intelligence: A Modern Approach' : 'Stuart Russell',
                   'Introduction to the Theory of Computation' : 'Michael Sipser',
                   'Code Complete' : 'Steve McConnell',
                   'The Mythical Man-Month: Essays on Software Engineering' : 'Frederick P. Brooks Jr.'}

title_to_shelf_number = {'Structure and Interpretation of Computer Programs' : 1,
                         'Introduction to Algorithms' : 34,
                         'The C Programming Language' : 23,
                         'The Pragmatic Programmer: From Journeyman to Master' : 12,
                         'Art of Computer Programming' : 4,
                         'Design Patterns: Elements of Reusable Object-Oriented Software' : 586,
                         'Artificial Intelligence: A Modern Approach' : 32,
                         'Introduction to the Theory of Computation' : 98,
                         'Code Complete' : 77,
                         'The Mythical Man-Month: Essays on Software Engineering' : 3}

title_to_book_record = {}

# TU WPISZ SWÓJ KOD

# TEGO PONIŻEJ NIE TRZEBA RUSZAĆ - WYPISUJE WYNIK NA EKRAN
for title,book_record in title_to_book_record.items():
    print(title," : ", book_record)
