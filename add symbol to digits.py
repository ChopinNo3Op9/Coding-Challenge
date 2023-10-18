'''
Add the symbol "*" to all integers in a string, leaving all other characters unchanged. A consecutive number is treated as an integer.
'''

import re

def add_asterisk_to_integers(input_string):
    # consecutive digits (integers)
    pattern = r'\d+'
    
    def replace(match):
        matched_integer = match.group(0) # entire matched substring
        return f'*{matched_integer}*'
    
    # replace function that is called for each match found in the input_string.
    result = re.sub(pattern, replace, input_string)
    
    return result

# Test the function
# input_string = "Hello, 123 and 4567 are integers."
input_string = 'Jkdi234klowe90a3'
output_string = add_asterisk_to_integers(input_string)
print(output_string)
