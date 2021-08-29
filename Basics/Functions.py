# input
# function - logic
# output


for i in range(0, 11, 1):
    print(i)



for j in range(0, 11, 2):
    print(j)

word = "Appple"
count = 0

for index in range(0, len(word)):
    if word[index] == "p":
        count += 1

print(count)


# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))

# def add(num1, num2):
#     return num1 + num2


# output = add(num1, num2)
# print(output)


# pass keyword
# default value parameter


fname = input("enter firstname: ")
lname = input("enter lastname: ")
country = input("enter country: ")

def person(first_name, last_name="Last Name", country="US"):
    print(first_name, last_name, "lives in", country)


# positional arguments vs keyword
# 1 positional argument
person("sai")

# 3 positional argument
person("sai", "maddy", "india")

# 2 positional arguments
person("sai", "maddy")

person(fname)




def multiply(num1, num2=4):
    print(num1 * num2)


multiply(7, 3)


def addition(num1, num2=3, num3=6) :
    print(num1+num2+num3)
addition(9)


def koolkid(num1, num2 = "bye"):
    print(num1+num2)

koolkid("My name is sumanth.")