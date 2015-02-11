# Zadanie 5

Czyszczenie konsoli

## Opis:

Nasz gra strasznie śmieci w terminalu, ale możemy to zmienić. Za każdym razem gdy będziemy rozpoczynać nową rozgrywkę chcemy mieć pusty ekran z powitaniem.
Możemy wykorzystać do tego moduł `os` i jego funkcję `system` by wywołać polecenie systemowe `cls` (dla linuxa i macosx `clear`).

Przykład:
```python
import os

os.system('cls')
print("Witaj w grze!")
```

## Explore:

* Dopracuj grę by jej przebieg miał następujące `ekrany`:

```
Witaj w grze:
S - Start gry
P - Wybierz poziom komputera
Q - Wyjście
```

```
Wybierz poziom komputera:
A - Sprytny computer
B - Głupi computer
```

```
Podaj swój wybór:
K - Kamień
P - Papier
N - Nożyczki
```

```
Czy chcesz grać dalej? tak/nie:
```

Uwzględnij wszystkie funkcjonalności jakie udało ci się zbudować wcześniej. Każdy z tych ekranów powinien pojawiać się na czystej konsoli. 
