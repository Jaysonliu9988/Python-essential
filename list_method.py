list1 = [1, 2, 3, 4, 5]
list2 = ['banana', 'apples', 'mango', 'oranges', 'mango']
list3 = [4, 3, 1, 5, 2]
list1.extend(list2)
list4 = list2.copy()
print(list1)

list2.append('cherry')
print(list2)
print(len(list2))

list2.insert(0, 'pear')
print(list2)

list2.remove('pear')
print(list2)

# list2.clear()
# print(list2)

print(list2.index('oranges'))
print(list2.count('mango'))

list3.sort()
print(list3)

list3.reverse()
print(list3)

print(list4)
list4.pop()
print(list4)
list4.pop(3)
print(list4)
del list4[2]
print(list4)
