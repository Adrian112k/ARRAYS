# Dwuwymiarowa tablica
arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Inicjalizacja zmiennych dla najmniejszej i największej wartości
min_value = arr[0][0]  # Pierwszy element jako początkowa najmniejsza wartość
max_value = arr[0][0]  # Pierwszy element jako początkowa największa wartość
min_position = (0, 0)  # Początkowa pozycja najmniejszej wartości
max_position = (0, 0)  # Początkowa pozycja największej wartości

# Iteracja przez wiersze i kolumny tablicy
for i in range(len(arr)):
    for j in range(len(arr[i])):
        value = arr[i][j]  # Bieżąca wartość w tablicy
        if value < min_value:  # Jeżeli wartość jest mniejsza niż obecna najmniejsza
            min_value = value
            min_position = (i, j)  # Aktualizujemy pozycję najmniejszej wartości
        if value > max_value:  # Jeżeli wartość jest większa niż obecna największa
            max_value = value
            max_position = (i, j)  # Aktualizujemy pozycję największej wartości

# Drukowanie wyników
print(f"Najmniejsza wartość: {min_value} znajduje się w wierszu {min_position[0] + 1}, kolumnie {min_position[1] + 1}")
print(f"Największa wartość: {max_value} znajduje się w wierszu {max_position[0] + 1}, kolumnie {max_position[1] + 1}")
