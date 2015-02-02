Instrukcje warunkowe - ściąga
-----------------------------

Uwagi ogólne
============

* w pseudo-kodzie:

  * ``IF`` / ``ELSE IF`` / ``ELSE`` - początek danego bloku (a jednocześnie koniec poprzedniego jeśli był jakiś);

  * ``<END-OF-IF>`` - oznaczenie końca bloków ``IF`` / ``ELSE IF`` / ``ELSE``;

* podstawowa konstrukcja bloku w Pythonie (znak ``|`` rozdziela opisy elementów składowych **pojedynczej linii kodu**):

  .. code::

      słowo kluczowe (s.k.): if ALBO elif ALBO else | spacja + wyrażenie warunku (nie dotyczy s.k. else) | dwukropek
      wcięcie | instrukcja nr 1 wykonywana pod warunkiem
      wcięcie | instrukcja nr 2 wykonywana pod warunkiem
      wcięcie | # (...) coś tam, coś tam... :)
      wcięcie | instrukcja nr N wykonywana pod warunkiem
      brak wcięcia! | instrukcja nr X wykonywana bezwarunkowo

* więcej info: `Conditional statements - Wikipedia (EN)`_


Przykłady
=========

Pojedynczy ``if``
*****************

+-----------------+-----------------------------------------------+
| Pseudo-kod      | Python                                        |
+-----------------+-----------------------------------------------+
|.. code::        |.. code:: python                               |
|                 |                                               |
|    IF cond_A    |    if cond_A:                                 |
|        task_A1  |        task_A1()                              |
|        task_A2  |        task_A2()                              |
|        (...)    |        # (...)                                |
|    <END-OF-IF>  |    # uwaga! cofnięcie wcięcia = koniec bloku  |
|    task_B1      |    task_B1()                                  |
|    task_B2      |    task_B2()                                  |
|    (...)        |    # (...)                                    |
+-----------------+-----------------------------------------------+


Pojedynczy ``if`` + ``else``
****************************

+--------------------------+---------------------------------------------------------------+
| Pseudo-kod               | Python                                                        |
+--------------------------+---------------------------------------------------------------+
|.. code::                 |.. code:: python                                               |
|                          |                                                               |
|    IF cond_A             |    if cond_A:                                                 |
|        task_A1           |        task_A1()                                              |
|        task_A2           |        task_A2()                                              |
|        (...)             |        # (...)                                                |
|    ELSE                  |    else: # uwaga! cofnięcie wcięcia - koniec bloku if (...):  |
|        # = (NOT cond_A)  |        # == (not cond_A)                                      |
|        task_B1           |        task_B1()                                              |
|        task_B2           |        task_B2()                                              |
|        (...)             |        # (...)                                                |
|    <END-OF-IF>           |    # uwaga! cofnięcie wcięcia = koniec bloku                  |
|    task_C1               |    task_C1()                                                  |
|    task_C2               |    task_C2()                                                  |
|    (...)                 |    # (...)                                                    |
+--------------------------+---------------------------------------------------------------+


``if`` + ``elif``
*****************

+-------------------------------------+-----------------------------------------------+
| Pseudo-kod                          | Python                                        |
+-------------------------------------+-----------------------------------------------+
|.. code::                            |.. code:: python                               |
|                                     |                                               |
|    IF cond_A                        |    if cond_A:                                 |
|        task_A1                      |        task_A1()                              |
|        task_A2                      |        task_A2()                              |
|        (...)                        |        # (...)                                |
|    ELSE IF cond_B                   |    elif cond_B: # uwaga! cofnięcie wcięcia    |
|        # = (NOT cond_A) AND cond_B  |        # == (not cond_A) and cond_B           |
|        task_B1                      |        task_B1()                              |
|        task_B2                      |        task_B2()                              |
|        (...)                        |        # (...)                                |
|    <END-OF-IF>                      |    # uwaga! cofnięcie wcięcia = koniec bloku  |
|    task_C1                          |    task_C1()                                  |
|    task_C2                          |    task_C2()                                  |
|    (...)                            |    # (...)                                    |
+-------------------------------------+-----------------------------------------------+


``if`` + K * ``elif``
*********************

+------------------------------------------------------+-------------------------------------------------------+
| Pseudo-kod                                           | Python                                                |
+------------------------------------------------------+-------------------------------------------------------+
|.. code::                                             |.. code:: python                                       |
|                                                      |                                                       |
|    IF cond_A                                         |    if cond_A:                                         |
|        task_A1                                       |        task_A1()                                      |
|        task_A2                                       |        task_A2()                                      |
|        (...)                                         |        # (...)                                        |
|    ELSE IF cond_B                                    |    elif cond_B:                                       |
|        # = (NOT cond_A) AND cond_B                   |        # == (not cond_A) and cond_B                   |
|        task_B1                                       |        task_B1()                                      |
|        task_B2                                       |        task_B2()                                      |
|        (...)                                         |        # (...)                                        |
|    ELSE IF cond_C                                    |    elif cond_C:                                       |
|        # = (NOT cond_A) AND (NOT cond_B) AND cond_C  |        # == (not cond_A) and (not cond_B) and cond_C  |
|        task_C1                                       |        task_C1()                                      |
|        task_C2                                       |        task_C2()                                      |
|        (...)                                         |        # (...)                                        |
|    (...)                                             |    # (...) opcjonalne kolejne bloki z elif            |
|    ELSE IF cond_K                                    |    elif cond_K:                                       |
|        # = (NOT cond_A) AND (...) AND cond_K         |        # == (not cond_A) and (...) and cond_K         |
|        task_K1                                       |        task_K1()                                      |
|        task_K2                                       |        task_K2()                                      |
|        (...)                                         |        # (...)                                        |
|    <END-OF-IF>                                       |    # uwaga! cofnięcie wcięcia = koniec bloków         |
|    task_L1                                           |    task_L1()                                          |
|    task_L2                                           |    task_L2()                                          |
|    (...)                                             |    # (...)                                            |
+------------------------------------------------------+-------------------------------------------------------+


``if`` + ``elif`` + ``else``
****************************

+-------------------------------------------+------------------------------------------------+
| Pseudo-kod                                | Python                                         |
+-------------------------------------------+------------------------------------------------+
|.. code::                                  |.. code:: python                                |
|                                           |                                                |
|    IF cond_A                              |    if cond_A:                                  |
|        task_A1                            |        task_A1()                               |
|        task_A2                            |        task_A2()                               |
|        (...)                              |        # (...)                                 |
|    ELSE IF cond_B                         |    elif cond_B:                                |
|        # = (NOT cond_A) AND cond_B        |        # == (not cond_A) and cond_B            |
|        task_B1                            |        task_B1()                               |
|        task_B2                            |        task_B2()                               |
|        (...)                              |        # (...)                                 |
|    ELSE                                   |    else:                                       |
|        # = (NOT cond_A) AND (NOT cond_B)  |        # == (not cond_A) and (not cond_B)      |
|        task_C1                            |        task_C1()                               |
|        task_C2                            |        task_C2()                               |
|        (...)                              |        # (...)                                 |
|    <END-OF-IF>                            |    # uwaga! cofnięcie wcięcia = koniec bloków  |
|    task_D1                                |    task_D1()                                   |
|    task_D2                                |    task_D2()                                   |
|    (...)                                  |    # (...)                                     |
+-------------------------------------------+------------------------------------------------+


``if`` + K * ``elif`` + ``else``
********************************

+------------------------------------------------------+-------------------------------------------------------+
| Pseudo-kod                                           | Python                                                |
+------------------------------------------------------+-------------------------------------------------------+
|.. code::                                             |.. code:: python                                       |
|                                                      |                                                       |
|    IF cond_A                                         |    if cond_A:                                         |
|        task_A1                                       |        task_A1()                                      |
|        task_A2                                       |        task_A2()                                      |
|        (...)                                         |        # (...)                                        |
|    ELSE IF cond_B                                    |    elif cond_B:                                       |
|        # = (NOT cond_A) AND cond_B                   |        # == (not cond_A) and cond_B                   |
|        task_B1                                       |        task_B1()                                      |
|        task_B2                                       |        task_B2()                                      |
|        (...)                                         |        # (...)                                        |
|    ELSE IF cond_C                                    |    elif cond_C:                                       |
|        # = (NOT cond_A) AND (NOT cond_B) AND cond_C  |        # == (not cond_A) and (not cond_B) and cond_C  |
|        task_C1                                       |        task_C1()                                      |
|        task_C2                                       |        task_C2()                                      |
|        (...)                                         |        # (...)                                        |
|    (...)                                             |    # (...) opcjonalne kolejne bloki z elif            |
|    ELSE IF cond_K                                    |    elif cond_K:                                       |
|        # = (NOT cond_A) AND (...) AND cond_K         |        # == (not cond_A) and (...) and cond_K         |
|        task_K1                                       |        task_K1()                                      |
|        task_K2                                       |        task_K2()                                      |
|        (...)                                         |        # (...)                                        |
|    ELSE                                              |    else:                                              |
|        # = (NOT cond_A) AND (...) AND (NOT cond_K)   |        # == (not cond_A) and (...) and (not cond_K)   |
|        task_L1                                       |        task_L1()                                      |
|        task_L2                                       |        task_L2()                                      |
|        (...)                                         |        # (...)                                        |
|    <END-OF-IF>                                       |    # uwaga! cofnięcie wcięcia = koniec bloków         |
|    task_M1                                           |    task_M1()                                          |
|    task_M2                                           |    task_M2()                                          |
|    (...)                                             |    # (...)                                            |
+------------------------------------------------------+-------------------------------------------------------+

.. _`Conditional statements - Wikipedia (EN)`: https://en.wikipedia.org/wiki/Conditional_%28computer_programming%29

