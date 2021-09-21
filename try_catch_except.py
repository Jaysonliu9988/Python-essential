try:
    filename = input('File name to open: ')
    f = open(filename, 'r') # FileNotFoundError will occur if the file does not exist
    
    lineList = f.readlines()
    f.close()    
    print('File contains', len(lineList), 'lines.')
        
    lineNum = int(input('View which line?: ')) # ValueError will occur if input is not an int

    print(lineList[lineNum - 1]) # IndexError will occur if the number is not a valid index number

except FileNotFoundError:
    print('File not found. Check spelling.')

except ValueError:
    print('Invalid input. Int required.')

except IndexError:
    print('Invalid line number.')

except:
    print('Something went wrong.')
