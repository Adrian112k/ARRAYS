# Funkcja, która zwraca ciąg gwiazdek odpowiadający podanej liczbie
def star(n):
    return '*' * n

# Tablica zawierająca liczby
numbers = [2, 6, 4, 9, 7]

# Pętla, która wypisuje liczbę i odpowiadające jej gwiazdki
for number in numbers:
    print(f"{number}: {star(number)}")
