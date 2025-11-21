computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
lenght = len(computer_games)
i=0
computer_games.sort()

while i < lenght:
    print(f"Number {i+1} {computer_games[i]}")
    i += 1

