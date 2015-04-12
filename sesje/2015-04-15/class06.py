# 1. Uzupełnij moduł `rockets` o 3 (trzy) klasy (nazwy możesz dać inne byle tylko były rozróżnialne):
# RakietaPierwszejGeneracji, RakietaDrugiejGeneracji, RakietaPiatejGeneracji
# opisującymi kolejne generacje rakiet.
# 2. Rakiety kolejnych generacji powinny spełniać następujące warunki:
# * rakieta 1. generacji (tu: RakietaPierwszejGeneracji) jest pochodną od Rocket;
# * rakieta 2. generacji (tu: RakietaDrugiejGeneracji) jest pochodną od rakiety 1. generacji;
# * rakieta 5. generacji została zbudowana "od podstaw, na bazie" Rocket;
# * rakiety kolejnych generacji powinny mieć coraz większy ciąg (ang. thrust
#   i takim atrybutem można go też opisać).
# 3. Dla uproszczenia przyjmijmy tylko dwie metody pre-definiowania ciągu,
#   który jest dodatnią, niezmienianą ("stałą") liczbą całkowitą:
#   podanie do inicjalizacji (=tworzenia jej "egzemplarza") lub jako wartość
#   wbudowaną (=ustalana podczas "projektowania" rakiety)
# 4. Obiekt rakiety powinien umożliwiać sprawdzenie ich maksymalnego ciągu przez
#   metodę `get_thrust()`;
# 5. Każda rakieta ma swój stan (np. w atrybucie `state`);
# 6. Stan możemy pobrać metodą `get_state()` a ustawić metodą `set_state()`;
# 7. Stan może się zmieniać tylko w następującej kolejności (patrz lista STATES w module `rockets`):
#   "standing" (obiekt str; rakieta stojąca na platformie; to pierwszy stan po
#   stworzeniu egzemplarza rakiety)
#   -> "starting" (rakieta startująca) -> "flying" (rakieta w locie),
#   -> "disintegrating" (dezintegracja / destrukcja rakiety),
#   -> None (co oznacza, że rakieta została "zniszczona" i już "nie istnieje").

# korzystamy z importowania kodu (nazwy klas mogą być własne)
from rockets import Rocket, RakietaPierwszejGeneracji, RakietaDrugiejGeneracji, RakietaPiatejGeneracji

# stwórzmy "egzemplarze" rakiet o rosnącym ciągu
# jeśli chcemy podawać ciąg przy inicjalizacji (tworzeniu egzemplarza):
r1 = RakietaPierwszejGeneracji(100)
r2 = RakietaDrugiejGeneracji(200)
r5 = RakietaPierwszejGeneracji(500)
# lub tak - jeśli ciąg jest parametrem wbudowanym (konstrukcyjnym):
#r1 = RakietaPierwszejGeneracji()
#r2 = RakietaDrugiejGeneracji()
#r5 = RakietaPierwszejGeneracji()

# tu sobie zróbmy trochę operacji na rakietach związanych ze zmianami stanu
print('Działamy:')
print('pobierz biażący stan:', r1.get_state())
r1.set_state('starting')
print('pobierz nowy stan:', r1.get_state())
r1.set_state('startX')
print('pobierz nowy stan:', r1.get_state())
r1.set_state(None)
print('pobierz nowy stan:', r1.get_state())
# itp. itd.

# sprawdźmy Wasze rakiety :)
import rockets_tester
classes_to_test = [RakietaPierwszejGeneracji, RakietaDrugiejGeneracji, RakietaPierwszejGeneracji]
rockets_to_test = [r1, r2, r5]
rockets_tester.test_rockets(classes_to_test, rockets_to_test)

