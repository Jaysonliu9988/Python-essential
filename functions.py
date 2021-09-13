def greetings_function(name):
    print('Hello '+name)
# greetings_function()
greetings_function('Jayson')

def greetings_function2(name):
    print(f'Hello {name}')
    print('Hello ' + str(name))
# greetings_function()
greetings_function2(34)

def greetings_function3(name, age):
    print('Hello ' + name + '. You are ' + str(age) + ' years old now.') # normal 
    print(f'Hello {name}. You are {age} years old now.') # f-string => much much better!!!
greetings_function3('Jayson', 34)


def greetings_function4(*names):
    print('Hello '+names[2])
# greetings_function()
greetings_function4('Jayson', 'Tim', 'Mike')

def greetings_function5(name, age):
    print(f'Hello {name}. You are {age} years old now.') # f-string => much much better!!!
name = input('Enter your name: ')
age = input('Enter your age: ')
greetings_function5(name, age)