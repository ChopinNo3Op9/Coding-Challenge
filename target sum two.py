'''
Find the all possible combinations of any numbers from a list of numbers so that they add up to the target sum.
'''


import itertools

def find_combinations(nums, target):
    result = []
    
    nums.sort()

    for r in range(1, len(nums) + 1):
        for combination in itertools.combinations(nums, r):  # size of the combinations to generate from nums
            if sum(combination) == target:
                result.append(combination)
    
    return result

# Example usage:
numbers = [2, 3, 5, 7, 1, 6]
target_sum = 7
combinations = find_combinations(numbers, target_sum)

for combo in combinations:
    print(combo)


