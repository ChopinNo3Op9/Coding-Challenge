'''
Write a function to decide whether two strings are contained by another: 
define string inclusion relationship: string A=abc, string B=ab, string C=ac, then A contains B, and a and C have no inclusion relationship.
'''

def is_string_contained(string):

    if string[1] in string[0] or string[0] in string[1]:
        return 1
    else:
        return 0

# test
string = ["devsc", "devscdf"]
# string = ["abc", "ac"]

print(is_string_contained(string))