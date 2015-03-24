# Uzupełnij ciało funkcji find_by_isbn_part tak, aby zwracała tytuły książek zawierające podany fragment numeru ISBN

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

# POPRAW PONIŻSZĄ FUNKCJĘ
def find_by_isbn_part(books, isbn_part):
    result = []
    # PODPOWIEDZI:
    # - użyj for
    # - isbn_part in isbn to warunek, który sprawdza czy ciąg znaków isbn_part zawiera się w isbn
    # - dodawanie elementów do listy, gdzie x to lista, a e to element, który chcesz dodać: x.append(e)
    return result

# TEGO PONIŻEJ NIE ZMIENIAJ
def test(books):
    single_test(books, '020', ['The Pragmatic Programmer: From Journeyman to Master', 
                               'Art of Computer Programming',
                               'Design Patterns: Elements of Reusable Object-Oriented Software',
                               'The Mythical Man-Month: Essays on Software Engineering'])
    single_test(books, '18', ['The Mythical Man-Month: Essays on Software Engineering'])
    single_test(books, '22', ['The Pragmatic Programmer: From Journeyman to Master',
                              'Artificial Intelligence: A Modern Approach'])
    single_test(books, '0735619670', ['Code Complete'])

def single_test(books, input, expected_output):
    output = find_by_isbn_part(books, input)
    if set(output) != set(expected_output) or len(output) != len(expected_output):
        print("ŹLE! DLA '"+input+"' WYNIK TO: '"+str(output)+"', OCZEKIWANO: '"+str(expected_output)+"'")
    else:
        print("OK! DLA '"+input+"'")

test(books)
