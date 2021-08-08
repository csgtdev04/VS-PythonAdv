def prod_or_sum():
    num1 = int(input("number: "))
    num2 = int(input("number: "))
    product = num1 * num2
    if product > 1000:
        return num1 + num2
    else:
        return product


# output = prod_or_sum()
# print(output)


# Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string
n = (int(input("Type a number ")))
word = (input("give a word "))

# 1. input
# 2. logic
# 3. output

def removeCharacters(word, n):
    ans = (n + 1)

    string2 = (word[ans:])

    return string2

output2 = removeCharacters(word, n)
print(output2)


