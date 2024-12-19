# Tworzymy tablicę o wymiarach 5x5
table = [[0 for _ in range(5)] for _ in range(5)]

# Wypełniamy tablicę wartościami zgodnymi z tablicą mnożenia
for i in range(5):  # Iterujemy po wierszach (1 do 5)
    for j in range(5):  # Iterujemy po kolumnach (1 do 5)
        table[i][j] = (i + 1) * (j + 1)  # Mnożymy odpowiednie liczby

# Drukujemy tablicę
for row in table:
    print(" ".join(map(str, row)))  # Łączymy elementy wiersza w jeden ciąg tekstowy, oddzielony spacjami
