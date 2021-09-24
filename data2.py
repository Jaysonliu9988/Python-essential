import json # import the json module

f = open('data2.txt', 'r') # open the file in read mode
data = json.load(f) # read the json data into the 'data' variable 
f.close()

# change some details
data['isMember'] = False
data['address']['street'] = '456 Demonstration Avenue'
# delete children with age over 18
for child in data['children'][:]:
    if child['age'] > 18:
        data['children'].remove(child)
f = open('data.txt', 'w') # open the file in write mode 
json.dump(data, f) # encode 'data' to json and write to file 
f.close()