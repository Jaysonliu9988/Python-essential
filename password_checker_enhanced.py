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
    else:
        return False

    if len(pword) >= 8:
        longEnough = True
    else:
        return False
    
    for char in pword:
        if not hasUpper and char.isupper():
            hasUpper = True
        if not hasLower and char.islower():
            hasLower = True
        if not hasNumber and char.isdigit():
            hasNumber = True
        if not hasSpecial and char in specialChars:
            hasSpecial = True
        if shortEnough and longEnough and hasUpper and hasLower and hasNumber and hasSpecial:
            return True
    return False

password = input('Enter your password: ')
if checkPassword(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')
