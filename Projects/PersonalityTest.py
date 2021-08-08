# Build an Interactive Quiz.
# Which Avenger are you? 
# Build a personality or recommendation quiz that can asks users some questions, 
# stores their answers, and then perform some kind of calculation to give the user a 
# personalized end result that's based on their answers


name = input("Welcome to the personality quiz. What's your name? ")
answer1 = int(input(name + ", what's your favorite number from 1 - 10? "))
answer2 = input(name + ", what color is your favorite, green or brown? ")
answers = [answer1, answer2]

def personality_quiz(answers):
    if (answers[0] > 1 and answers[0] < 6) and answers[1] == "green":
        return "You are calm during stressful situations"
    elif (answers[0] > 5 and answers[0] < 11) and answers[1] == "green":
        return "You are an over-thinker"
    elif (answers[0] > 1 and answers[0] < 6) and answers[1] == "brown":
        return "You are a broad thinker"
    else:
        return "You are a good person, overall"


output = personality_quiz(answers)
print(name, "here is your output:", output)
