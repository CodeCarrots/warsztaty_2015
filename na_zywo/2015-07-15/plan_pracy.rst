Plan pracy
==========

#. Tworzymy nową *aplikację* (tu: ``main``) i podpinamy ją pod *projekt* - pamiętamy o tak o ``INSTALLED_APPS`` w ``settings.py`` jak i głównym ``urls.py``.

#. Tworzymy dwa różne routingi na potrzeby dwóch widoków. Zakładając, że nasz serwis potrzebuje *strony głównej* (``/``) oraz podstrony *O nas* (```/about``) tworzymy wpisy w ``urls.py`` *aplikacji*:

   .. code:: python

     url(r'^$', views.homepage, name='homepage'),
     url(r'^about$', views.about, name='about'),

   Wartości atrybutów ``name`` mogą być oczywiście inne (byleby miały sens) - przydadzą się nam za chwilę.

#. Routing aplikacji podpinamy do głównego wpisem:

   .. code:: python

     url(r'', include('main.urls', namespace='main')),

   gdzie:

     * ``r''`` umożliwia nam posługiwanie się adresami bez prefiksów (patrz: wcześniejsza aplikacja od ``notek``)

     * ``namespace`` (tzw. przestrzeń nazw) jest nieobowiązkowe ale przydaje się do `grupowania widoków <http://django.readthedocs.org/en/latest/topics/http/urls.html#namespaces-and-include>`_.

#. Do stworzonych routingów dodajemy proste widoki i oddzielnymi templatkami. Widoki powinny używać metody ``render()`` lub podobnej, która obsługuje przekazywanie do templatek tzw. kontekstu.

#. W templatce *strony głównej* (tu: renderowanej przez metodę ``homepage`` z ``views.py``) umieszczamy link do strony *O nas*:

   .. code:: html

     <a href="/about">O nas</a>

   a w templatce stronu *O nas* - link do *Strony głównej*:

   .. code:: html

     <a href="/">O nas</a>

#. W obu templatkach zamieniamy linki wpisane na sztywno w kod na generowane przez framework. Korzystamy przy tym z `tagu templatkowego *url* <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#std:templatetag-url>`_:

   .. code:: html

     <!-- albo tak: -->
     <a href="{% url 'about' %}">O nas</a>
     <!-- albo tak: -->
     <a href="{% url 'main:about' %}">O nas</a>

   gdzie ``about`` jest nazwą routingu (parametr ``name``) a opcjonalne ``main`` (parametr ``namespace``) - przestrzenią nazw.

   Podobnie robimy dla SG (*strony głównej*) zmieniając tylko nazwę routingu.

#. Korzystając z aplikacji ``registration`` (paczka ``django-registration-redux``; patrz: pierwsze i drugie zajęcia projektowe) wyświetlamy na stronie głównej linki:

    * do strony logowania

    * do wylogowania

    * do strony z formularzem rejestracyjnym

#. Zależnie od tego `czy użytkownik jest zalogowany czy nie <https://docs.djangoproject.com/en/dev/topics/auth/default/>`_ wyświetlamy odpowiednio albo link do wylogowania albo linki do stron formularzami rejestracji oraz logowania. W templatce `warunek <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#if>`_ ten można sprawdzić przy pomocy `atrybutu is_authenticated <https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated>`_ obiektu ``request.user`.

#. Ćwiczenia samodzielne:

    #. wyświetlanie na stronie pojedynczych *notek* (`dokumentacja <http://django.carrots.pl/django_views.html#pierwszy-widok>`_)

    #. rozwinięcie modelu *notek* (konieczna migracja!) o datę dodania (pobieraną z czasu systemowego), dodanie sortowania, np. malejąco po dacie dodania, na stronie listy notek (`dokumentacja <http://django.carrots.pl/django_views.html#widok-ktory-naprawde-cos-robi>`_)

    #. stronicowanie *notek* ze stałym sortowaniem (j.w.), np. malejąco po dacie dodania (`dokumentacja <https://docs.djangoproject.com/en/dev/topics/pagination/>`_)

    #. zablokowanie możliwości dodawania wpisów przez niezalogowanych (`dokumentacja <https://docs.djangoproject.com/en/dev/topics/auth/default/#limiting-access-to-logged-in-users>`_), dodanie strony, na którą zostanie `przekierowany <https://docs.djangoproject.com/en/dev/topics/http/shortcuts/#redirect>`_ użytkownik, nie posiadający `odpowiednich uprawnień <https://docs.djangoproject.com/en/dev/topics/auth/default/#permissions>`_;

    #. po utworzeniu przy pomocy panelu administracyjnego dwóch grup użytkowników - tak zabezpieczyć formularze (dojście do widoku z formularzem oraz odbiór danych) aby jedni mogli dodawać *notki* a drudzy nie (`dokumentacja <http://stackoverflow.com/a/20110261>`_)

    #. rozwinięcie modelu *notek* o pole autora (konieczna migracja!), wyświetlanie w formularzu autora na podstawie ``request.user`` (obiekt `User <https://docs.djangoproject.com/en/dev/ref/contrib/auth/#django.contrib.auth.models.User>`_) i *zapisywanie do bazy* (nie jako daną z formularza!); login można zapisywać wprost (łatwiejsze ale niekoniecznie poprawne) albo skorzystać z tzw. referencji (lepsze, bardziej poprawne; `dokumentacja <https://docs.djangoproject.com/en/dev/ref/models/fields/#foreignkey>`_)

