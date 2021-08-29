list = [1, 2]
list.append(3)

print(list)

list.insert(1, 1.5)
print(list)

list.remove(1)
print(list)

popped_item = list.pop(0)

if popped_item > 1:
    list.append(popped_item)

print(list)


list2 = ['hi', 'bye', 'apple', 'banana', 'hi', 'b']
print(list2.index('hi', 2))

print(list2.count('hi'))

list2.reverse()
print(list2)