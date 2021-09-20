import random
op = input('Addition or subtraction test? [enter "+" or "-"]: ')

if op == '+':
    print('Addition Test\n')
else:
    print('Subtraction Test\n')
    op = '-'

print('Name: __________\n\n')

for i in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    if op == '-' and num1 < num2:
        num1, num2 = num2, num1

    print(num1, op, num2, '= ____\n')
