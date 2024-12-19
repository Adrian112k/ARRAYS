###
# Prints a list of popular computer games, sorted alphabetically and numbered
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sort the list alphabetically
computer_games.sort()

# Initialize index for numbering
index = 1
i = 0  # Iterator for while loop

# Use a while loop to print the games with numbers
while i < len(computer_games):
    print(f'{index}. {computer_games[i]}')  # Print numbered game
    index += 1  # Increment the number
    i += 1  # Move to the next game
