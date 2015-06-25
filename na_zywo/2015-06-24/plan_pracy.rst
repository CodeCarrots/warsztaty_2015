Plan pracy
==========

#. Korzystając z `dokumentacji wdrożeniowej <https://django-registration-redux.readthedocs.org/en/latest/quickstart.html>`_ podpinamy aplikację ``registration`` do projektu edytując ``settings.py`` w tym:

   * uzupełniając krotkę ``INSTALLED_APPS``
   * dodając routing wg instrukcji (``accounts/``)
   * dodając opcjonalnie stałe ``ACCOUNT_ACTIVATION_DAYS`` i ``REGISTRATION_AUTO_LOGIN`` (lub inne, wg dokumentacji)

#. Uruchamiamy serwer. Jeśli pojawiają się komunikaty o konieczności wykonania migracji: zatrzymujemy serwer i wykonujemy ``manage.py migrate`` po czym wznawiamy pracę serwera.

#. Wchodzimy pod adres ``http://127.0.0.1:8000/accounts/`` (uwaga: ukośnik na końcu adresu jest znaczący) gdzie dostaniemy... `błąd 404 <https://en.wikipedia.org/wiki/HTTP_404>`_ ale jednocześnie zobaczymy jaki mamy routing.

#. Korzystając z nazw poszczególnych widoków (atrybut ``name``) wybieramy ``registration_register`` - on odpowiada w aplikacji za serwowanie formularza rejestracji. Odpowiadająca mu ścieżka to ``/accounts/register/``.

#. Po wejściu pod adres ``http://127.0.0.1:8000/accounts/register/`` przywita nas... `błąd 500 <https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error>`_ :) - komunikat informuje nas, że nie ma szablonu ``base.html``. Choć nie wynika to wprost z dokumentacji - ten szablon jest podstawą wszystkich widoków obsługiwanych przez aplikację.

#. Szablon możemy dodać np. do utworzonego katalogu ``<nazwa projektu>/registration/templates`` gdzie podkatalog ``registration`` - przyjęty tu tylko dla porządku - jest nazwą używanej aplikacji.

#. Wybraną ścieżkę należy dodać także do konfiguracji w ``settings.py`` tak aby Django tam w ogóle zajrzało:

   .. code:: python

    TEMPLATES = [
        {
            # (...)
            'DIRS': [
                '<nazwa projektu>/registration/templates',
            ],
            # (...)
        },
    ]

#. Szablon ``base.html``, z którego `dziedziczą kolejne widoki <https://docs.djangoproject.com/en/dev/ref/templates/language/#template-inheritance>`_ powinien zawierać co najmniej `blok <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#std:templatetag-block>`_ ``content``. To jakie bloki są używane w poszczególnych templatkach można sprawdzić zaglądając do... `szablonów wbudowanych w aplikację <https://github.com/macropin/django-registration/tree/master/registration/templates/registration>`_. Krótko mówiąc: my tworzymy *ramę*, które aplikacja wypełnia swoimi *bloczkami*. Przykład:

   .. code:: html

    <html>
        <head>
            <title>
                {% block title %}Tytuł do nadpisania{% endblock %}
            </title>
        </head>
        <body>
            {% block content %}Tu będzie formularz lub komunikat{% endblock %}
        </body>
    </html>

#. Jeśli chcemy w całości tworzyć własne szablony musimy odwołać się `dokumentacji używanego backendu <https://django-registration-redux.readthedocs.org/en/latest/default-backend.html>`_ (lub napisać własny :P) aby sprawdzić jak powinny nazywać się szablony, jakie obiekty dostarczy nam widok itp. itd.

#. Po dodaniu w nagłówku strony HTML (węzeł ``HEAD``) odpowiednich styli (np. `Bootstrap <http://getbootstrap.com/getting-started/>`_'a) możemy *hurtowo* poprawić wygląd poszczególnych widoków:

   .. code::

    /accounts/register/
    /accounts/login/
    /accounts/logout/

   itd.

#. Aby zapewnić aplikacji możliwość wysyłki maili aktywacyjnych do kont, do ``settings.py`` należy dodać `odpowiednią konfigurację <https://docs.djangoproject.com/en/dev/topics/email/#smtp-backend>`_. Przykład:

   .. code:: python

    EMAIL_HOST = 'poczta.o2.pl'
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True

    from auths import (
        DEFAULT_FROM_EMAIL,
        EMAIL_HOST_USER,
        EMAIL_HOST_PASSWORD
    )
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

   gdzie moduł ``auths`` zawiera zmienne wymienione w imporcie, zawierające kolejno: adres nadawcy (adres skrzynki pocztowej nadawcy czyli *de facto* naszego serwisu), login oraz hasło (do tej skrzynki!). Z tego też powodu plik z takimi danymi (tu: ``auths.py``) nie powinien NIGDY trafić do repozytorium.

   Nic nie stoi na przeszkodzie aby do rozsyłania powiadomień czy linków aktywacyjnych używać prywatnego maila (zamiast dedykowanego konta czy usługi) ale... nietrudno przewidzieć jak to się może skończyć :)

#. Po uruchomieniu rejestracji czy logowania można stworzyć kilka kont a potem np. zmodyfikować je z poziomu panelu administracyjnego.

