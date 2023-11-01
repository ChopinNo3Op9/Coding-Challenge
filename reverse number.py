'''
Input an integer, the integer in the form of a string to output the program in reverse order does not consider the case of negative numbers, 
if the number contains 0, then the reverse form also contains 0, if the input is 100, the output is 001
'''

def reverse_integer_string(input_str):
    reversed_str = input_str[::-1]
    
    if not reversed_str:
        reversed_str = '0'
    
    return reversed_str

# test
input_str = '1516000'
reversed_str = reverse_integer_string(input_str)
print(reversed_str)
