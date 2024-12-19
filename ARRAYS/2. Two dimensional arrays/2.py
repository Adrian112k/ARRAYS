# 3x3 Tic-Tac-Toe board
tic_tac_toe_board = [
   ['X', 'O', 'X'],
   [' ', 'X', 'O'],
   ['O', ' ', 'X']
]

# Wyświetlenie planszy Tic-Tac-Toe
for row in tic_tac_toe_board:
    for cell in row:
        print(cell, end=" ")  # Użycie end=" " zapobiega przejściu do nowej linii po każdym znaku
    print()  # Przechodzi do nowej linii po wydrukowaniu całego wiersza
