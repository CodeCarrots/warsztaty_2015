
def if_statement():
    name = input("Podaj swoje imię:")
    if name == "John":
        print("Hello John! How are you?")
    elif name == "Kasia":
        print("Witaj Kasia! Jak się masz?")
    else:
        print("Hola extraño! Cómo estás?")  # Google translate (TM), Don't hate.


def while_loop():
    player_choice = "c"
    while player_choice == "c":
        print("Game on!")
        # ...
        print("Do you want to play again? c - continue, q - quit")
        player_choice = input()

if_statement()
while_loop()