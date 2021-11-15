# Write a function named "l33t" that receives a parameter named "text" (a string) 
# and returns a version of "text" with the following characters replaced:
# "a" should be replaced with "@", "e" should be replaced with "3", "i" should be replaced with "1", "o" should be replaced with "0" 
# and "u"... should just be left as is. Or replaced with "(_)" if you want to get fancy.
# e.g. if you give the function text of "omg super hacker", 
# it should return a string of "0mg sup3r h@ck3r" or "0mg s(_)p3r h@ck3r"

def l33t(text: str):
    text= text.replace('a', '@').replace('e', '3').replace('o', '0').replace('u', '(_)')
    print(text)
text='omg super hacker'
l33t(text)

