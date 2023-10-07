'''
Find the maximum sum by transforming one plus sign to a multiplication sign in the given list of numbers powered by their order.
'''

def max_sum_with_one_multiplication(numbers):
    n = len(numbers)
    
    # powers of each number based on their order
    powers = [num ** (i + 1) for i, num in enumerate(numbers)]
    
    max_sum = sum(powers)
    
    for i in range(n - 1):
        # Try changing the operation at position i from addition to multiplication
        modified_powers = powers[:]
        modified_powers[i] = powers[i] * powers[i + 1]
        modified_powers.pop(i + 1)
        
        current_sum = sum(modified_powers)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# test
input_list = [1, 1, 4, 5, 1, 4]
result = max_sum_with_one_multiplication(input_list)
print(result)
