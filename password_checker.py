# A maximum of 16 characters
# A minimum of 8 characters
# A minimum of 1 upper case character
# A minimum of 1 lower case character
# A minimum of 1 number
# A minimum of 1 special character: '~!#$%^*()_+-={}|[]\:<>?,./

def checkPassword(pword):
    shortEnough = False
    longEnough = False
    hasUpper = False
    hasLower = False
    hasNumber = False
    hasSpecial = False

    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'

    if len(pword) <= 16:
        shortEnough = True
    if len(pword) >= 8:
        longEnough = True

    for char in pword:
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
        if char.isdigit():
            hasNumber = True
        if char in specialChars:
            hasSpecial = True
    if shortEnough and longEnough and hasUpper and hasLower and hasNumber and hasSpecial:
        return True
    else:
        return False

password = input('Enter your password: ')

    

if checkPassword(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')