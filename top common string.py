'''
Top three most common characters in the string. 
Print the three most common characters along with their occurrence count. 
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
'''

from collections import Counter

def top_three_characters(s):
    char_count = Counter(s)
    
    # Sort characters by occurrence count in descending order and then alphabetically
    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
    
    top_three = sorted_chars[:3]
    
    return top_three


# test
ss = 'aabbbccde'
for char, count in top_three_characters(ss):
    print(f"{char} {count}")