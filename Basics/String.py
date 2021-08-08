word = "Python"
print(word[0])
print(word[3])
print(word[5])
print(word[-1])
print(word[-2])


another_word = "Time for an Adventure"
print(another_word[2])
print(another_word[15])
print(another_word[-1])

print(another_word[5:7])
print(another_word[-9:100])
print(another_word[12:])
print(another_word[:4])
print(another_word[9:-10])

print(len(another_word))
print(another_word[12:len(another_word)])

item1 = "Soap"
item2 = "Cake"
item3 = "Toy"
                
grocery_list = [item1, item2, item3, "Bananas", "Apples", 6, [True, False, "watergun", 4]]
print(type(len(grocery_list[6][2])))


print(type(str(8)))