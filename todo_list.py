# --- getList(filename), returns a list of strings ---
# (open/create file and return lines of text as a list of strings)
def getList(filename):
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        f = open(filename, 'w+')
    data = f.readlines() # this line is a placeholder
    f.close()
    return data



# --- showList(data), returns nothing ---
# (receive list of strings and display them, or "nothing in list" message)
def showList(data):
    if len(data) == 0:
        print('Your To Do List is empty.')
    else:
        print('To Do List:')
        itemNum = 1
        for item in data:
            print('  ' + str(itemNum) + ') ' + item.rstrip('\n'))
            itemNum += 1



# --- addToList(filename, data), returns a list of strings ---
# (prompt for an item to add to the list of strings and append to the file)
def addToList(filename, data):
    item = input('Add: ')
    item = item + '\n'

    data.append(item)

    f = open(filename, 'a')
    f.write(item)
    f.close()

    print('Item added to list.\n')
    return data



# --- deleteFromList(filename, data), returns a list of strings ---
# (prompt for item number to delete from the list of strings and write list to the file)
def deleteFromList(filename, data):
    num = input('Item number to delete: ')
    try:
        num = int(num)
        num -= 1
        del data[num]
    except:
        print('Invalid input - Nothing deleted.\n')
        return data        

    f = open(filename, 'w')
    f.writelines(data)
    f.close()

    print('Item deleted from list.\n')
    return data
        

# --- main part of program ---
FILENAME = 'list.txt' # define the filename used to store the list
lineList = getList(FILENAME) # call the getList function to read the file into a list

while True: # this endless loop displays the list and prompts the user for a command

    showList(lineList) # call showList to show the current content of the list

    # show the instructions for the possible commands - [a]dd, [d]elete, e[x]it
    print('\nType "a" to add an item.')

    if len(lineList) > 0: # only show the delete instruction if the list has items
        print('Type "d" to delete an item.')

    print('Type "x" to exit.')

    command = input('> ') # prompt for a command

    # if "a", calladdToList to prompt for item and add to list
    if command == 'a': 
        lineList = addToList(FILENAME, lineList)

    # if "d", call deleteFromList to prompt for item number and delete from list        
    elif command == 'd' and len(lineList) > 0:
        lineList = deleteFromList(FILENAME, lineList)

    elif command == 'x': # if "x", break out of the loop to end the program
        print('Goodbye!')
        break

    else: # if anything else, show an error message
        print('Invalid command.\n')
