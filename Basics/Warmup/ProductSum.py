# functions are blocks of code

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

# Given two integer numbers return their product. If the product is greater than 1000, then return their sum
def calculate_multiplication_or_sum(num1, num2):    
    product = num1 * num2
    sum = num1 + num2
    if product > 1000:
        return sum
    else:
        return product


result_from_function = calculate_multiplication_or_sum(num1, num2) 
print(result_from_function)

