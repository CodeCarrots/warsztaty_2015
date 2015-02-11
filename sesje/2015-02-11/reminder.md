Przypomnienie:

Instrukcja warunkowa `if` i jej warianty:
```python
name = input("Podaj swoje imię:")
if name == "John":
    print("Hello John! How are you?")
elif name == "Kasia":
    print("Witaj Kasia! Jak się masz?")
else:
    print("Hola extraño! Cómo estás?")  # Google translate (TM), Don't hate.
```

Pętla `while`:
```python
player_choice = "c"
while player_choice == "c":
    print("Game on!")
    # ...
    # Zwóć uwagę że wpisanie dowolnej innej wartosci niż `c` (nie tylko `q`)
    # skutkuje zakończeniem programu.
    print("Do you want to play again? c - continue, q - quit")
    player_choice = input()
```
