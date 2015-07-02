Plan pracy
==========

#. Dodajemy nową aplikację (tu: ``messages``; pamiętajmy o ``INSTALLED_APPS``)

   .. code:: bash

    ./manage.py startapp messages

#. Dodajemy w aplikacji routing (``urls.py`` aplikacji!) na dwie różne ścieżki (`dokumentacja <https://docs.djangoproject.com/en/1.8/topics/http/urls/>`_):

   .. code:: python

    from django.conf.urls import url

    from . import views

    urlpatterns = [
        url(r'^notes$', views.notes, name='notes'),
        url(r'^create$', views.create, name='create'),
    ]

#. Podpinamy ten routing do projektu (via ``include()`` w głównym ``urls.py``; pamiętajmy o prefiksie)

#. Uzupełniamy ``views.py`` o potrzebne metody obsługujące widoki (korzystamy np. z ``render()``; `dokumentacja <https://docs.djangoproject.com/en/1.8/topics/http/views/>`_)

#. Dodajemy szablony powiązane z widokami, wyświetlające prosty tekst, dzięki któremu odróżnimy te dwa widoki

#. Sprawdzamy czy podane URL-e działają i wyświetla się pod nimi treść z szablonów

#. Dodajemy ``forms.py`` z klasą formularza z dwoma polami tekstowymi (klasy ``CharField``; `dokumentacja <https://docs.djangoproject.com/en/1.8/topics/forms/#building-a-form-in-django>`_): krótkim na tytuł i dłuższym na tekst

#. Wyświetlamy wnętrze formularza w szablonie przekazując go tam przy pomocy dodatkowego parametru w ``render()`` (`dokumentacja <https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/>`_), renderujemy przy pomocy ``{{...}}``

#. Ponieważ pole na dłuższy tekst trudno uzupełniać kiedy ma jedną linię - zmieniamy tzw. *widget* tego pola na klasę ``Textarea`` (`dokumentacja <https://docs.djangoproject.com/en/1.8/ref/forms/widgets/>`_)

#. Uzupełniamy HTML szablonu z wnętrzem formularza o tagi ``<form ...>...</form>`` (metoda: ``POST``; akcja: pusta lub nie podana wcale) oraz ``<button>...</button>`` (`dokumentacja <https://docs.djangoproject.com/en/1.8/topics/forms/#the-template>`_)

#. Próbujemy uzupełnić i wysłać formularz - dostajemy błąd wynikający z braku taga ``{% csrf_token %}`` wewnątrz formularza. Musimy go dodać i odświeżyć stronę aby wysłać formularz.

