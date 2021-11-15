# Write a function named "print_box" that receives 2 parameters - "width" (an integer) and "height" (an integer).  
# The function should print a box/rectangle made out of "#" characters that is "width" characters wide and "height" characters high.  
# The function should not return anything - it should simply print the box.  e.g. print_box(10, 5) would print:

##########
#        #
#        #
#        #
##########

def print_box(width: int, height: int):
    char = '#'
    for _ in range(height):
        print(width * char)

print_box(10, 5)
print(' ')

# This function should involve a for loop and use Python's ability to multiply a string by an integer, 
# e.g. "#" * 10 results in "##########".  
# If you want to make this function more sophisticated, make sure that it works as intended even with small values (e.g. a 1x1 box would simply be "#", 
# and 0x0 or lower would not print anything), and allow a 3rd, 
# optional parameter (a string of 1 character) named "char" which allows the user to specify which character to use instead of "#", 
# and a 4th optional parameter (a boolean) named "fill" which determines whether the function prints an outline as seen above, or a filled box, e.g.

##########
##########
##########
##########
##########

def print_box(width: int, height: int, char='#', fill=False):
    if fill:
        for _ in range(height):
            print(width * char)
    else:
        position_height = 0
        for i in range(height):
            if position_height == 0:
                print(width * char)
            elif range(height)[-1] == position_height:
                print(width * char)
            else:
                print(char + ' ' * (width -2) + char )
            position_height += 1

print_box(10, 5)