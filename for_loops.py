for letter in 'Hello':
    print(letter)

print()
for ninin in 'Hello':
    print(ninin)

my_dict = {
    'name': 'Mike',
    'age': '23'
}

for values in my_dict:
    print(values)


my_list = ['ji', 'ju', 'jk']

for values in my_list:
    print(values)
    if values == 'ju':
        break

print()
print('-------- print ji --------')
my_list2 = ['ji', 'ju', 'jk']

for values in my_list2:
    # print(values)
    if values == 'ju':
        break
    print(values)

print()
print('--------- loop 0 to 9 ----------')
for x in range(10):
    print(x)

print()
print('------ loop 3 to 7  -------')
for x in range(3, 7):
    print(x)
else: 
    print('Finished looping!')