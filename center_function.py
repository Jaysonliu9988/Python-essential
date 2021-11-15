# Write a function named "center" that receives 2 parameters - "text" (a string) and "width" (an int), 
# and returns a string containing "text" centered in a string of "width" length.
# e.g. If you give the function text of "hello" and a width of 11, 
# it should return a string of " hello " (i.e. the text with 3 spaces before and 3 spaces after - a total of 11 characters).
# This function replicates Python's built in str.center() method - see the documentation for further information and examples of how it handles things, 
# and don't use this function in your solution...


def center(text: str, width: int):
    if width < len(text):
        print(text)
    else:
        new_len = []
        left_space = (width - len(text)) // 2
        right_space = width - len(text) - left_space
        for _ in range(left_space):
            new_len.append(' ')
        for i in text:
            new_len.append(i)
        for _ in range(right_space):
            new_len.append(' ')
        print(''.join(new_len))

center(text='hello', width=11)










