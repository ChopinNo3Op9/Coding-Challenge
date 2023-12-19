'''
Write a program that takes a positive floating-point value and outputs an approximate integer value of that value. 
If the value after the decimal point is greater than or equal to 0.5, round up; If the value is less than 0.5, round down.
'''

def custom_round(value):
    integer_part = int(value)
    decimal_part = value - integer_part

    if decimal_part >= 0.5:
        return integer_part + 1
    else:
        return integer_part

# Example usage
result = custom_round(2.3)
# result = custom_round(2.5)
print(result)