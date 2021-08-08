name = input("What is your name?")
email = input("What is your email?")
age = int(input("What is your age"))

word = "word"
print(word[1:3])

user_details = [name, email, age]

print(user_details)

# If their age is greater than 18 AND their name starts with the letter “S”, tell them that they are allowed entry to the game.
# Otherwise, if their email is longer than 15 letters (including ‘@gmail.com’), they are allowed entry to the game.
# If both the above conditions don’t match, they can’t play the game (print this out).


if age > 18 and name[0] == "S":
    print("You can enter.")
elif len(email) > 15:
    print("You can enter.")
else:
    print("You can't play.")


    
