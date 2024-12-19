###
# Raport stacji pogodowej
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]

# Liczba pomiarów
measurements = len(temperatures)

# Obliczanie średniej temperatury
temp_total = 0
for temp in temperatures:  # Iteracja przez wszystkie temperatury
    temp_total += temp  # Dodawanie każdej temperatury do sumy
avg_temp = temp_total / measurements  # Obliczanie średniej przez podzielenie sumy przez liczbę pomiarów

# Obliczanie minimalnej i maksymalnej temperatury
min_temp = min(temperatures)  # Minimalna temperatura
max_temp = max(temperatures)  # Maksymalna temperatura

# Obliczanie liczby dni z temperaturą ujemną
negative_temp = 0
i = 0
while i < measurements:  # Iteracja przez indeksy temperatur
    if temperatures[i] < 0:  # Sprawdzanie, czy temperatura jest ujemna
        negative_temp += 1  # Zwiększenie licznika ujemnych temperatur
    i += 1  # Przejście do następnego dnia

# Wydruk raportu miesięcznego
print('RAPORT TEMPERATUR')
print('Miesiąc: Marzec')
print('Liczba pomiarów:', measurements)
print('Średnia temperatura w miesiącu:', f'{avg_temp:.2f}')  # Wyświetlanie z dokładnością do dwóch miejsc
print('Minimalna temperatura:', min_temp)
print('Maksymalna temperatura:', max_temp)
print('Liczba dni z temperaturą ujemną:', negative_temp)
