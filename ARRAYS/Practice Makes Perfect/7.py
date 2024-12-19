# Tablica zawierająca polskie imiona
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# Zmienna do przechowywania najdłuższego imienia
longest_name = names[0]

# Pętla przechodząca przez tablicę i porównująca długości imion
for name in names:
    if len(name) > len(longest_name):
        longest_name = name

# Wypisanie wyników
print("Names:", *names)
print("Longest name:", longest_name)
