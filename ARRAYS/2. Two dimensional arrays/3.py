# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Inicjalizacja zmiennych do sumowania wydatków
food_total = 0
transport_total = 0
utilities_total = 0
week_totals = []

# Obliczanie wydatków dla każdej kategorii oraz dla każdego tygodnia
for week in monthly_expenses:
    food_total += week[0]
    transport_total += week[1]
    utilities_total += week[2]
    week_totals.append(sum(week))  # Suma wydatków dla danego tygodnia

# Obliczanie całkowitych wydatków na miesiąc
total_expenses = food_total + transport_total + utilities_total

# Wydrukowanie wyników
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total_expenses)
