coun_file = open('/Users/jayson/Linkedin Course/Python-essential/countries.txt', 'r')

# print(coun_file.readline())
# print(coun_file.readlines())
# print(coun_file.readlines()[1])


for files in coun_file.readlines():
    print(files)




coun_file.close()

