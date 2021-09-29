students = {60254: 'John Smith', 60255: 'Gert Du-Cart', 60256: 'Sun Po',
            60257: 'Bort Woods', 60258: 'Andrew Butters', 60259: 'Betty Ho'}
usernames = {} # create empty dictionary to store usernames
for num, name in students.items():
    # convert to lower case, remove dashes, split into a list
    nameParts = name.lower().replace('-', '').split()

    # create more convenient variables using the list items
    fname = nameParts[0]
    sname = nameParts[1]

    # first letter of first name concatenated to first 4 letters of surname
    uname = fname[0] + sname[0:4]

    # pad with 0s as needed
    uname = uname.ljust(5, '0')

    usernames[num] = uname # add to usernames dictionary
    
for num, uname in usernames.items(): # print usernames 
    print(num, uname)