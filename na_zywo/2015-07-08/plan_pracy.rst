Plan pracy
==========

#. Punktem wyjścia są główne elementy składowe *formularza* czyli:
   * `klasa definiująca <https://docs.djangoproject.com/en/dev/topics/forms/#more-on-fields>`_ w ``forms.py``

     .. code:: python

      # ...
      class NoteForm(forms.Form):
          title = forms.CharField(label='Title', max_length=100)
          text = forms.CharField(widget=forms.Textarea, max_length=1000)

   * `kod HTML szablonu <https://docs.djangoproject.com/en/dev/topics/forms/#the-template>`_ w ``create.html``

     .. code:: html

      <h2>create</h2>
      <form action="" method="post">
          {% csrf_token %}
          {{ form.as_p }}
          <input type="submit" value="Send"/>
      </form>

   * widok renderujący formularz (a jednocześnie przyjmujący dane) we ``views.py``

     .. code:: python

      # ...
      def create(request):
          form = NoteForm()
          return render(request, 'create.html', {'form': form})
      # ...

   Końcowym efektem powinno być zapisywanie się pojedynczych przesyłanych notatek do bazy i wyświetlanie ich przy pomocy widoku ``views.notes``.

   Zapis powinien być poprzedzony sprawdzeniem czy w ogóle nastąpiło przesłanie notatki i czy dostarczone dane są prawidłowe.

#. Pierwszy krok to `sprawdzenie <https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.method>`_ czy wywołanie metody ``create()`` jest związane z wejściem na stronę z formularzem (metoda ``GET``) czy też z przesłaniem formularza (metoda ``POST``). Do sprawdzenia użyć można atrybutu ``method`` z obiektu ``request`` czyli ``request.method``.

   W każdym przypadku - czy to wyświetlenia czy odbierania danych - powinna być tworzona instancja obiektu klasy ``NoteForm``.

   .. code:: python

    # ...
    print('Dane w POST-cie:', request.POST)
    if request.method == 'POST':
        form = NoteForm()
    else:
        form = NoteForm()
    # ...

#. Odebrane dane notatki trzeba `przekazać do instancji formularza <https://docs.djangoproject.com/en/dev/topics/forms/#the-view>`_ celem walidacji:

   .. code:: python

    # ...
    if request.method == 'POST':
        form = NoteForm(request.POST)
        print('Poprawne?', form.is_valid())
    else:
        # ...

#. Jeśli dane będą niepoprawne - *wrócą* do formularza a obok pola z błędnymi danymi wyświetli się komunikat błędu.

#. Jeśli dane są poprawne możne je wydobyć (``form.cleaned_data``) i gdzieś zapisać - na początku niech będzie to zwykła tablica:

   .. code:: python

    # ...
    NOTES = []
    # ...
    def create(request):
        # ...
        if request.method == 'POST':
            form = NoteForm(request.POST)
            if form.is_valid():
                NOTES.append(form.cleaned_data)
        else:
    # ...

#. Zebrane notatki możemy wyświetlić przy pomocy osobnego widoku (``views.notes``):

     .. code:: python

      # ...
      def notes(request):
          notki = NOTES
          return render(request, 'notes.html', {'notes': notki})
      # ...

   oraz odpowiedniego szablonu (``notes.html``):

     .. code:: html

      <h2>notki</h2>
      {% for item in notes %} {# pętla iterująca po liście notes #}
      <p>
          Tytuł: {{ item.title }}<br>
          Tekst: {{ item.text }}
      </p>
      {% endfor %}

   gdzie ``item`` w `pętli <https://docs.djangoproject.com/en/dev/ref/templates/builtins/#for>`_ jest słownikiem a ``title`` i ``text`` jego kluczami.

#. Jeśli nie chcemy aby przesłane, poprawne i zapisane dane *wracały* do formularza na stronie wystarczy nadpisać instancję formularza.

#. Po restarcie serwera notki giną i aby je zachować powinniśmy je *utrwalić* - np. przy pomocy bazy danych. To z kolei wymaga stworzenia `modelu <https://docs.djangoproject.com/en/dev/topics/db/models/#quick-example>`_ (w ``models.py``) oraz przeprowadzenia migracji (``makemigrations`` + ``migrate``).

   Sam model powinien, przynajmniej w zakresie długości zapisywanych pól, być zgodny z formularzem a najlepiej dać pewien zapas:

   .. code:: python

    class Notes(models.Model):
        title = models.CharField(max_length=150)
        text = models.CharField(max_length=1100)

#. Gotowego modelu możemy użyć do `zapisu danych <https://docs.djangoproject.com/en/dev/topics/db/models/#field-options>`_:

   .. code:: python

    # def create():
    # ...
    if form.is_valid():
        # tego już nie potrzebujemy
        #NOTES.append(form.cleaned_data)
        n = Notes.objects.create(
            # atrybut_modelu = wartość_ze_słownika_formularza
            title=form.cleaned_data['title'],
            text=form.cleaned_data['text']
        )
        # właściwy zapis
        n.save()
        # "czyszczenie" formularza
        form = NoteForm()
    else:
    # ...

   oraz ich wyciągania:

   .. code:: python

    # def notes():
    # ...
    # tego też już nie potrzebujemy
    #notki = NOTES
    notki = Notes.objects.all()
    # ...

#. Stworzone notki można teraz przeglądać, edytować i kasować z poziomu panelu administracyjnego.

