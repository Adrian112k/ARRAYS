###
# Program do obliczenia wartości wszystkich towarów dostępnych w sklepie
#
# Ceny 10 produktów w sklepie komputerowym (w jednostkach waluty)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Liczba jednostek dostępnych dla każdego produktu
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# Obliczanie całkowitej wartości dostępnych towarów
total_value = 0
for i in range(len(product_prices)):
    total_value += product_prices[i] * product_quantities[i]

# Wypisywanie całkowitej wartości towarów
print("Całkowita wartość wszystkich towarów w sklepie:", total_value)
