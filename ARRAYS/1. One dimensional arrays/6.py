###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[n - 1]  # Odejmujemy 1, aby dopasować indeks (1=poniedziałek to indeks 0)

# Print the day names for the given day numbers
day_numbers = [1, 4, 7]
for day_number in day_numbers:
    print(f'Day {day_number}: {weekday(day_number)}')  # Wyświetlanie nazwy dnia tygodnia dla każdego numeru
