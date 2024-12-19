import matplotlib.pyplot as plt
import numpy as np

# Tworzymy listę kątów od 0 do 360 stopni
x_degrees = np.linspace(0, 360, 361)  # 361 punktów, ponieważ chcemy włączyć 360 stopni

# Konwertujemy kąty z stopni na radiany
x_radians = np.radians(x_degrees)

# Obliczamy wartości y = sin(x) dla każdego kąta
y = np.sin(x_radians)

# Rysujemy wykres
plt.plot(x_degrees, y)

# Ustawiamy etykiety i tytuł wykresu
plt.xlabel("Kąt (stopnie)")
plt.ylabel("y = sin(x)")
plt.title("Wykres funkcji y = sin(x)")

# Wyświetlamy wykres
plt.grid(True)
plt.show()
