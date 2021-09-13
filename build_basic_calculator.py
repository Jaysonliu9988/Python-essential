num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operator = input('Enter the operator(+ - * /): ')

if operator == '+':
    print(f'The additon is {num1+num2}.')
elif operator == '-':
    print(f'The substraton is {num1-num2}.')
elif operator == '*':
    print(f'The multiplication is {num1*num2}')
elif operator == '/':
    print(f'The division is {num1/num2}')
else:
    print('Invalid operator')
    