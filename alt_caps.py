# Write a function named "alt_caps" that receives 2 parameters - "text" (a string) and "upFirst" (a boolean value, default of True), 
# and returns a version of "text" with AlTeRnAtInG CaPiTaL LeTtErS.If the upFirst parameter is True, 
# the first character of "text" should be capitalised (and the second character in lowercase, and so on). 
# If upFirst is False, the first character of "text" should be in lowercase (and the second character in uppercase, and so on).
# e.g. if you give the function text of "potato" and upFirst of True, it should return a string of "PoTaTo". 
# If you give it text of "potato" and upFirst of False, it should return a string of "pOtAtO"

def alt_caps(text: str, upFirst=False):
    rstr = ''

    while (upFirst == True):
        for i in range(len(text) ):
            if i % 2 == 0 :
                rstr = rstr + text[i].upper()
            else:  
                rstr = rstr + text[i].lower()
        return rstr    

    while (upFirst == False):
        for i in range(len(text) ):
            if i % 2 == 0 :
                rstr = rstr + text[i].lower()
            else:  
                rstr = rstr + text[i].upper()
        return rstr  
print(alt_caps('potato'))
