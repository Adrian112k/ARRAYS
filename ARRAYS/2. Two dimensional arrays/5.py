# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

# Funkcja obliczająca łączną liczbę miejsc
def seats_total(seats):
   return sum(len(row) for row in seats)

# Funkcja obliczająca liczbę dostępnych miejsc
def seats_available(seats):
   return sum(row.count('A') for row in seats)

# Funkcja obliczająca liczbę zarezerwowanych miejsc
def seats_booked(seats):
   return sum(row.count('B') for row in seats)

# Funkcja zwracająca status miejsca na podstawie wiersza i miejsca
def seat_status(seats, row, place):
   return seats[row - 1][place - 1]

# Wydrukowanie tabeli z informacjami o kinie
print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
