grade = int(input("What grade are you in?"))

if grade >= 1 and grade <= 5:
    print("You are in elemenrary school.")
elif grade >= 6 and grade <= 8:
    print("You are in middle school.")
elif grade >= 9 and grade <= 12:
    print("You are in high school.")
else:
    print("Invalid Input")
