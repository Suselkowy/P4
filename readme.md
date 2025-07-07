# Odtworzenie eksperymentów opisanych w artykule "MAP4: A Pragmatic Framework for In-Network Machine Learning Traffic Classification" w środowisku zwirtualizowanym

Laboratorum pokazujące możliwość zastosowania drzewa decyzyjnego w P4, które pozwoli na odfiltrowywanie pakietów przenoszących złośliwe dane.

### Zawartość:

- Lab.ipnyb - notatnik jupyter, w którym na podstawie danych uczących tworzymy drzewo które zostanie wykorzystane w języku P4
- m4_ex/ - pliki, które powinny zostać wgrane na maszynę wirtualną obsługującą P4. Zawiera kod P4, który należy uzupełnić wygenerowanym przez nas drzewem, oraz skrypty `send.py` oraz `recieve.py` pozwalające na przetestowanie rozwiązania.
- filtered_packet_fields.zip - odpowiednio przygotowany zestaw danych 
- PrepareDataSet.ipynb - Skrypt, który posłużył do wygenerowania `filtered_packet_fields.zip` z datasetu CIC-IDS2017.