# Wypisz zawartość słownika w formacie:
# "TYTUŁ" by "AUTOR" is on shelf "NUMER PÓŁKI" (ISBN: "NUMER ISBN")
#
# Słownik books przechowuje pary (klucz : wartość) - "ISBN" : 3 ELEMENTOWA KROTKA ("tytuł książki", "imię głównego autora", "numer półki")
#
# PRZYKŁAD (jedna linijka oczekiwanego wyjścia):
# Introduction to Algorithms by Thomas H. Cormen is on shelf 34 (ISBN: 0262032937)

books = {'0262510871' : ('Structure and Interpretation of Computer Programs', 'Harold Abelson', 1),
         '0262032937' : ('Introduction to Algorithms', 'Thomas H. Cormen', 34),
         '0131103628' : ('The C Programming Language', 'Brian W. Kernighan', 23),
         '020161622X' : ('The Pragmatic Programmer: From Journeyman to Master', 'Andrew Hunt', 12),
         '0201485419' : ('Art of Computer Programming', 'Donald Ervin Knuth', 4),
         '0201633612' : ('Design Patterns: Elements of Reusable Object-Oriented Software', 'Erich Gamma', 586),
         '0130803022' : ('Artificial Intelligence: A Modern Approach', 'Stuart Russell', 32),
         '0534950973' : ('Introduction to the Theory of Computation', 'Michael Sipser', 98),
         '0735619670' : ('Code Complete', 'Steve McConnell', 77),
         '0201835959' : ('The Mythical Man-Month: Essays on Software Engineering', 'Frederick P. Brooks Jr.', 3)}

# ZMIEŃ PONIŻSZY KOD TAK BY ZADZIAŁAŁ ZGODNIE Z POLECENIEM
for isbn in books:
    pass
