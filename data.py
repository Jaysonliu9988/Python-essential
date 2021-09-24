import json # import the json module

f = open('data.txt', 'r') # open the file in read mode
data = json.load(f) # read the json data into the 'data' variable 
f.close()

# print the person's name
print('Loaded data for ' + data['name'])

# use some boolean and integer data
if data['isMember'] and data['age'] >= 18:
    print('18+ Member')

# print the details of the address
print('\nAddress:')
print(data['address']['street'])
print(data['address']['suburb'])
print(data['address']['state'] + ', ' + str(data['address']['pcode']))

# loop through the email addresses and print them
print('\nChildren:')
# for child in data['children']:
#     print(child['name'] + ' (' + str(child['age']) + ' years old)')

for i in data['children']:
    print(f'{i["name"]} ({i["age"]} years old)')