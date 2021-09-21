import random
op = input('Addition or subtraction test? [enter "+" or "-"]: ')
output = open('output.txt', 'w')


if op == '+':
    output.write('Addition Test\n')
else:
    output.write('Subtraction Test\n')
    op = '-'

output.write('Name: __________\n\n')

for i in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    if op == '-' and num1 < num2:
        num1, num2 = num2, num1

    output.write(f'{num1} {op} {num2} = ____\n')

output.close()
print('Test saved in output.txt file.')