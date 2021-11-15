# Write a function named reverse that receives a parameter named "text" (a string), and returns "text" in reverse.
# e.g. if you give the function text of "hello", it should return a string of "olleh"

def reverse(text:str):
    text = text[::-1]
    print(text)
    return
reverse(text='hello')

my_string = "Hey, This is a sample text"
print(my_string[2:]) #prints y, This is a sample text
print(my_string[2:7]) #prints y, Th excluding the last index
print(my_string[2::2]) #prints y hsi  apetx
print(my_string[::-1]) #reverses the string => txet elpmas a si sihT ,yeH

s = []
for i in range(1, 20):
    s.append(i)
    print(i)
print(s)
print(s[3:])
print(s[2::2])
print(s[::-1])
print(s[::-2])
print(s[15:10:-1])