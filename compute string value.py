'''
Given an arithmetic expression described by a string, compute the resulting value. 
The input string length less than 100, legal characters, including "+, -, *, /, (,)", "0-9".
'''

def compute_arithmetic_expression(expression):
    try:
        # Ensure the expression contains only valid characters
        allowed_chars = set("+-*/()0123456789 ")
        if not set(expression) <= allowed_chars:
            raise ValueError("Invalid characters in the expression")

        # Use eval to compute the result
        result = eval(expression)
        return result
    
    except Exception as e:
        return str(e)

# test
# expression = "2 * (3 + 4) - 5 / 2"
expression = "400+5"
result = compute_arithmetic_expression(expression)
print(result)
