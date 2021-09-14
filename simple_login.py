print('Please create your account now.')
usename = input('Enter your usename: ')
password = input('Enter your password: ')

print('Your account has been create successfully!')
print('Please login in now ...')

usename2 = input('Enter your username: ')
password2 = input('Enter your password: ')

if usename == usename2 and password == password2:
    print('Login successfully!!')
else:
    print('Invalid infomation!')