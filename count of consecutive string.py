'''
Count the consecutive occurrences of characters in a string.
'''

from itertools import groupby

def compress_string(s):
    compress = []

    for char, group in groupby(s):
        count = len(list(group))
        compress.append(f'({count}, {char})')
    
    return ' '.join(compress)


# test
s = '12223111'
print(compress_string(s))
