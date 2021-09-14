my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(my_list)
print(my_list[0])
print(my_list[1][1])

print()
print('------- Nested loop --------')
for lists in my_list:
    print(my_list)
    
print()
for lists in my_list:
    for row in lists:
        print(row)