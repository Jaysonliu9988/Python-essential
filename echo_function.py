# Write a function named "echo" that receives 2 parameters - "text" (a string) and "dropoff" (an int), 
# and prints the "text" in the form of an echo, removing "dropoff" characters each time.
# e.g. if you give the function text of "albatross" and a dropoff of 2, the function should print:
# albatross
# batross
# tross
# oss
# s


def echo(text: str, dropoff: int):
    cur_index = 0
    while True:
        print(text[cur_index:])
        cur_index += dropoff
        if cur_index > len(text):
            break

echo(text='albatross', dropoff=2)
















