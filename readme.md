# Odtworzenie eksperymentów opisanych w artykule "MAP4: A Pragmatic Framework for In-Network Machine Learning Traffic Classification" w środowisku zwirtualizowanym

Laboratorium pokazujące możliwość wykorzystania drzewa decyzyjnego w języku P4, w celu odfiltrowywania złośliwych pakietów.

### Zawartość:

- Lab.ipnyb - notatnik jupyter, w którym trenujemy drzewo decyzyjne, oraz kodujemy je do języka P4.
- m4_ex/ - pliki, które powinny zostać wgrane na maszynę wirtualną obsługującą P4. Zawiera kod P4, który należy uzupełnić wygenerowanym przez nas drzewem, oraz skrypty `send.py` oraz `recieve.py` pozwalające na przetestowanie rozwiązania.
- filtered_packet_fields.zip - odpowiednio przygotowany zestaw danych zawierający pakiety oraz przyporządkowane im klasy.
- PrepareDataSet.ipynb - skrypt, który posłużył do wygenerowania `filtered_packet_fields.zip` z datasetu CIC-IDS2017.  Z każdego 'flow' został wybrany jeden pakiet, reprezentujący go.