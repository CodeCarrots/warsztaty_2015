Plan pracy
==========

#. Tworzymy nowe środowisko wirtualne
#. Instalujemy w nim Django v1.8.x (``pip install "django==1.8"``).
#. Tworzymy pusty projekt.
#. Wykonujemy wstępną migrację (``manage.py migrate``).
#. Tworzymy superusera (``manage.py createsuperuser``).
#. Odpalamy serwer (``manage.py runserver``), wchodzimy do panelu administracyjnego.
#. Tworzymy dwie grupy:

   * "administratorzy" o uprawnieniach "Can add group", "Can change group" oraz pełnej kontroli nad użytkownikami (add, change, delete)
   * "uzytkownicy"... bez uprawnień ;)

#. Tworzymy dwa dodatkowe konta (w sumie będą trzy: superusera i te dwa dodane):

   * użytkownika administratora z przypisaniem do grupy "administratorzy" (należy dodatkowo zaznaczyć checkbox "Staff status");
   * użytkownika zwykłego z przypisaniem do grupy "uzytkownicy";

   **Ważne! Oba konta powinny mieć zaznaczony checkbox "Active" :)**

#. Mamy czysty projekt - dodajemy kod do repozytorium (na razie: lokalnego repozytorium!):

   .. code:: bash

    # w katalogu z kodem!
    git init
    # "ggctstproj" jest tutaj nazwą naszego projektu
    git add manage.py ggctstproj/*.py
    # pamiętamy tylko żeby nie dodać do repozytorium pliku bazy (*.sqlite*)
    # ani plików *.pyc czy katalogów __pycache__
    git ci -m "pusty projekt"

#. Przeglądamy w Sieci `djangowe pluginy do rejestracji<https://www.djangopackages.com/search/?q=registration>`_

#. Wybraliśmy `django-registration-redux <https://pypi.python.org/pypi/django-registration-redux/>`_ - jest rozwijany oraz utrzymywany a wg `dokumentacji <https://django-registration-redux.readthedocs.org/>`_ spełnia nasz use-case.

#. Doinstalowujemy plugin do virtualenv-a:

   .. code:: bash

    pip install django-registration-redux

#. Korzystając z `dokumentacji wdrożeniowej <https://django-registration-redux.readthedocs.org/en/latest/quickstart.html>`_ - krok po kroku podpinamy plugin pod projekt.

#. Restartujemy serwer, sprawdzamy działanie routingu, zmieniamy konfigurację itd.

