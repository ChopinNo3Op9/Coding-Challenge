'''
Remove the smallest number among numbers which are greater than a given number.
'''

def remove_smallest_larger_than(numbers, target):
    smallest_larger = float('inf')
    index_to_remove = None

    # Find the smallest number that is larger than the target
    for i, num in enumerate(numbers):
        if num > target and num < smallest_larger:
            smallest_larger = num
            index_to_remove = i

    # If a suitable number is found, remove it from the list
    if index_to_remove is not None:
        # del numbers[index_to_remove]
        numbers.pop(index_to_remove)

    return numbers

# test
my_list = [1, 3, 5, 7, 9, 11]
# my_list = [1, 3, 5, 6, 9, 11]
target_number = 6
result = remove_smallest_larger_than(my_list, target_number)
print(result)

