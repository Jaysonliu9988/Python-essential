# You have been asked to write a simple program involving calculating income tax, and have been provided with this table of information from the Australian Tax Office website:

# A) Write either pseudocode or a flowchart (your choice) that illustrates the design of a function which receives an income as a parameter and returns the amount of tax, calculated using the information in the table above.

# B) Write Python code for a function named “calculate_tax()” which implements your design. The function must:
#    Accept an “income” parameter (assume that it is a float).
#    Calculate the appropriate amount of tax.
#    Return the amount of tax as a float, rounded to two decimal places.

# C) Write a program that does the following (and uses your function as needed):
#    Prompt the user to enter their old income and attempt to convert it to
#       a float (re-prompt the user for input until they enter a float).
#    Prompt the user to enter their new income and attempt to convert it to
#       a float (re-prompt the user for input until they enter a float).
#       Hint: Use exception handling and a loop to re-prompt until a float is entered.
#    Calculate and store the amount of tax for the old and new incomes.
#    If their new income is more than their old income, print messages saying how much more they now earn and how much more tax they must pay.
#    Otherwise, if their new income is less than their old income, print messages saying how much less they now earn and how much less tax they must pay.


def get_tax(income: float):
    if 0 < income <= 18200:
        tax = 0
    elif 18200 < income <= 37000:
        tax = (income - 18200) * 0.19
    elif 37000 < income <= 90000:
        tax = 3572 + (income - 37000) * 0.325
    elif 90000 < income <= 180000:
        tax = 20797 + (income - 90000) * 0.37
    else:
        tax = 54097 + (income - 180000) * 0.45
    return tax

while True:
    try:
        old_income = float(input('What is your old taxable income?: '))
        break
    except:
        print('You should input a float num.')
while True:
    try:
        new_income = float(input('What is your new taxable income?: '))
        break
    except:
        print('You should input a float num.')

old_income_tax = get_tax(income=old_income)
new_income_tax = get_tax(income=new_income)
dif_income = abs(new_income - old_income)
dif_tax = abs(new_income_tax - old_income_tax)
if new_income > old_income:
    print('Your income has increase ${:.2f}'.format(dif_income))
    print('The tax you have to pay is increase ${:.2f}'.format(dif_tax))

else:
    print('Your income has decreased ${:.2f}'.format(dif_income))
    print('The tax you have to pay is reduced ${:.2f}'.format(dif_tax))














