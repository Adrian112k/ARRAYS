###
# Bubble sort
#
def bubble_sort(arr):
    n = len(arr)
    
    # Przechodzimy przez wszystkie elementy tablicy
    for i in range(n):
        # Ostatnie i elementy są już posortowane, więc nie musimy ich porównywać
        for j in range(0, n-i-1):
            # Zamieniamy miejscami, jeśli element jest większy od następnego
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Zamiana miejscami elementów
    
    return arr

# Przykład użycia dla car_fuel_consumption
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Fuel consumption before sorting:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print("Fuel consumption after sorting:", sorted_car_fuel_consumption)

# Przykład użycia dla bank_transactions
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("Bank transactions before sorting:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Bank transactions after sorting:", sorted_bank_transactions)
