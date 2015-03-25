# 1) Uzupełnij funkcję remove_book
# 2) Dodaj funkcję wyszukiwania po ISBN (patrz poprzednie zadanie)
# 3) Dodaj funkcję edytowania istniejącego rekordu (edit_book)
#
# Słownik books przechowuje pary (klucz : wartość) - "ISBN" : 3 ELEMENTOWA KROTKA ("tytuł książki", "imię głównego autora", "numer półki")
#
# Ten skrypt to prosta aplikacja konsolowa umożliwiająca wpisywanie komend i weryfikowanie ich efektów (komenda "help" wypisze wszystkie możliwe komendy).

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

def list_books():
    print("====================")
    for isbn, record in books.items():
        title, author, shelf = record
        print("-",title,"by",author,"(ISBN:"+isbn+")","is on shelf",shelf)
    print("====================")

def add_book():
    isbn = input("Input ISBN number of the book to add:")
    if isbn in books:
        print("Book with given ISBN number already exists")
        return
    title = input("Input title of the book to add:")
    author = input("Input author of the book to add:")
    shelf = input("Input shelf number for the book to add:")

    books[isbn] = (title, author, shelf)
    print("Book successfully added!")

def remove_book():
    print("Not implemented yet!")

def search_book():
    print("Not implemented yet!")

command = None

while command != 'exit':
    command = input("Command:")
    if command == "list":
        list_books()
    elif command == "add":
        add_book()
    elif command == "remove":
        remove_book()
    elif command == "help":
        print("Available commands are: list, add, remove, exit, help")
    elif command != "exit":
        print("Unknown command")

