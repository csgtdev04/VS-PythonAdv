#input
word = input("Enter a word for the palindrome checker: ")

#logic (function part)
def palindrome_checker(word):
    #logic
    # reverse string: 1) use loop 2) use index manipulation
    reversed_string = word[::-1]
    # output
    if reversed_string == word:
        return "Palindrome"
    else:
        return "Not a Palindrome"

output = palindrome_checker(word)
print(output)


#input
# word = input("Enter a word for the palindrome checker: ")

# #logic (function part)
# def palindrome_checker(word):
#     #logic
#     # reverse string: 1) use loop 2) use index manipulation
#     reversed_string = ""
#     for index in range(len(word) - 1,-1,-1):
#         reversed_string += word[index]

#     # output
#     if reversed_string == word:
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"

# output = palindrome_checker(word)
# print(output)


