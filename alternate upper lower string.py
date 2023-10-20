'''
Transforms the case of a string such that every other letter is in uppercase.
'''

def interval_case(input_str):
    result = []
    is_upper = True

    for char in input_str:
        if char.isalpha():
            if is_upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            is_upper = not is_upper
        else:
            result.append(char)

    return ''.join(result)

# Example usage:
input_string = "All over the world"
output_string = interval_case(input_string)
print(output_string)
