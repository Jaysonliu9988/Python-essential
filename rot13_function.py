# Write a function that receives a parameter named "rot13" (a string) and returns a version of the string encrypted using "rot13" (i.e. a basic caesar cipher with a shift of 13).
# rot13 transposes each letter of the alphabet by 13 places (wrapping back around to the start as needed), turning A into N, B into O, X into K, etc.
# e.g. if you give the function text of "HELLO WORLD", it should return "URYYB JBEYQ"
# This function is a little trickier than the others (and trickier than what you would encounter in an exam).  Consider creating a list of the letters of the alphabet and using their index numbers in your code, but there are many other approaches.
# Convert the string to uppercase and only change letters - ignore any other characters such as numbers, spaces and punctuation.

List = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rot13(rot13:str):
    return_list = []
    # length of the List
    str_table_length = len(List)
    for i in rot13:
        if i not in List:
            return_list.append(i)
        else:
            cur_str_index = List.index(i)
            decode_str_index = cur_str_index + 13
            if decode_str_index >= cur_str_index:
                decode_str_index = decode_str_index - str_table_length
            else:
                pass
            decode_str = List[decode_str_index]
            print(decode_str)
            return_list.append(decode_str)

    print(return_list)
    print(''.join(return_list))

rot13('A2 cN')