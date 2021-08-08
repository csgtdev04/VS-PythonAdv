# Accessing elements of a list
list = ["Phone", "Computer", "Watch", [2, 3, 4, [True, False]]]
print(list[1])
print(list[3][3][0])

# Accessing every element of the list
games = ["Game1", "Game2", "Game3", "Game4"]

for number in range(1, 10, 2):
    print(number)

print("Exited for loop")
len(games)

for index in range(0, len(games)):
    print(games[index])

for game in games:
    print(game)

# Ask user for email, password, name, age, status (active/inactive), add their properties to a list and go thru that list
# and print everything out

