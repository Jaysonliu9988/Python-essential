def my_function():
    return 3+4
print(my_function())

def my_function1():
    return 3+4
    print('Hello')
print(my_function1())
print()

def my_function2():
    print('Hello')
    return 3+4
print(my_function2())
print()


def add_numbers(num1, num2):
    return num1+num2
print(add_numbers(4, 6))

def add_numbers_input(num1, num2):
    return num1+num2
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
print(add_numbers_input(num1, num2))

def add_numbers_input_int(num1, num2):
    return num1+num2
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
print(add_numbers_input_int(num1, num2))
