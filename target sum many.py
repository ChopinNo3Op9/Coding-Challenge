'''
Find the all possible combinations of two numbers from a list of numbers so that they add up to the target sum.
'''


def find_combinations(nums, target):
    combinations = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                combinations.append((nums[i], nums[j]))

    return combinations

# Example usage:
numbers = [2, 7, 11, 15, 3, 6]
target_sum = 9

result = find_combinations(numbers, target_sum)
print(result)
