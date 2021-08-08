list = [1, 2, 3, "Word", False]
list.append("Appended Item")
print(list)
list.append(5)
print(list)

list.insert(1, 1.5)
print(list)

del list[1]
print(list)


del list[len(list) - 1]

[1, 2, 3, 'Word', False, 'Appended Item', 5]
