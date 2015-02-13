# Zadanie 5

Czyszczenie konsoli

## Opis:

Nasz gra strasznie śmieci w terminalu, ale możemy to zmienić. Za każdym razem gdy będziemy rozpoczynać nową rozgrywkę chcemy mieć pusty ekran z powitaniem.
Możemy wykorzystać do tego moduł `os` i jego funkcję `system` by wywołać polecenie systemowe `cls` (dla linuxa i macosx `clear`).

**UWAGA**: Poniższy kod nie zadziała gdy będzie uruchamiany z poziomu edytora IDLE (klawisz F5 lub menu Run -> Run Module). Aby poniższy kod poprawinie wyczyścił ekran, wasz program powinien być uruchomiony z poziomu konsoli systemowej. W windowsie aby uruchomić konsolę systemowa należy uruchomić polecenie `cmd.exe` lub zlokalizować w menu `Comand Prompt`/`Wiersz poleceń`, następnie wewnątrz konsoli systemowej wykonać polecenie `py C:/scieżka/do/waszego/pliku/gry.py`, zamieniająć podaną tu ścieżką na ścieżkę do waszego pliku z grą.

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
