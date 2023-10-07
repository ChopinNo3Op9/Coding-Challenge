'''
Find the maximum sum by transforming one plus sign to a multiplication sign in the given list of numbers.
'''

def max_sum_with_one_multiplication(numbers):
    n = len(numbers)

    max_sum = sum(numbers)
    
    for i in range(n - 1):
        # Try changing the operation at position i from addition to multiplication
        modified = numbers[:]
        modified[i] = numbers[i] * numbers[i + 1]
        modified.pop(i + 1)
        
        current_sum = sum(modified)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# test
input_list = [1, 1, 4, 5, 1, 4]
result = max_sum_with_one_multiplication(input_list)
print(result)
