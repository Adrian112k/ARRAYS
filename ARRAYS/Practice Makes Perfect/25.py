import matplotlib.pyplot as plt

# Listy do przechowywania wartości x i y
x = []
y = []

# Tworzymy wartości x od -100 do 100
for n in range(-100, 101):
    x.append(n)

# Tworzymy wartości y według funkcji f(x) = x^2 - 3
for n in x:
    y.append(n**2 - 3)

# Rysujemy wykres
plt.plot(x, y)

# Ustawiamy etykiety dla osi x i y
plt.xlabel("x")
plt.ylabel("f(x) = x^2 - 3")

# Ustawiamy tytuł wykresu
plt.title("Wykres funkcji f(x) = x^2 - 3")

# Wyświetlamy wykres
plt.show()
