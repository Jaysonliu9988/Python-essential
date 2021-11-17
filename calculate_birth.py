import datetime

current_year = datetime.datetime.now().year
while True:
    birth_year = input('What is your year of birth? ')
    try:
        birth_year = int(birth_year)
    except:
        print('The input must be numbers ')
        continue
    if 1900 < birth_year < current_year:
        break
    else:
        print('birth_year should from 1900 to {0}'.format(current_year))
while True:
    bday = input('Have You had your birthday this year (y/n)? ')
    if bday == 'y' or bday == 'n':
        break
    else:
        print('Please input y/n')

age = current_year - birth_year

if bday.lower() == 'n':
    age = age - 1

print('You are', age, 'years old.')

