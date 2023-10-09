'''
Split each input string with a length of 8 and output. 
If the length of a string is not an integer multiple of 8, fill the digit 0 after it. Empty strings are not processed.
'''

def split_and_fill(s):
    if not s:
        return []
    
    s = s[0]
    s_list = [t for t in s]

    remainder = len(s_list) % 8
    if remainder != 0:
        s += '0' * (8 - remainder)

    split_string = [s[i:i+8] for i in range(0, len(s), 8)]

    return split_string

# test
# a = ['abc']
a = ['123456789']
print('\n'.join(split_and_fill(a)))
