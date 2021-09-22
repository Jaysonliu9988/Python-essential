def getList(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        f = open(filename, 'w+')

    data = f.readlines()
    f.close()
    return data 

def showList(data):

    if len(data) == 0:
        print('Your To Do List is empty')
    else:
        print('To Do List: ')
        itemnum = 1
        for item in data:
            print(' ' + str(itemnum) + ')' + item.rstrip('\n'))
            itemnum += 1


def addToList(filename, data):
    item = input('Add: ')
    item = item + '\n'

    data.append(item)

    f = open(filename, 'a')
    f.write(item)
    f.close()

    print('Item added to list: ')
    return data    

def deleteFromList(filename, data):
    num = input('Item number to delete: ')

    try:
        num = int(num)
        num -= 1
        del data[num]

    except ValueError:
        print(f'Invalid input - Nothing deleted.\n')
        return data

    f = open(filename, 'w')
    f.writelines(data)
    f.close()

    print('Item deleted from list.\n')
    return data


FILENAME = 'list.txt' 
lineList = getList(FILENAME) 

while True: 

    showList(lineList)

    print('\nType "a" to add an item.')

    if len(lineList) > 0: 
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ')

    if command == 'a': 
        lineList = addToList(FILENAME, lineList)   

    elif command == 'd' and len(lineList) > 0:
        lineList = deleteFromList(FILENAME, lineList)

    elif command == 'x':
        print('Goodbye!')
        break

    else:
        print('Invalid command.\n')