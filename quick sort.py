'''
Quick sort.
'''
import random

def quicksort(nums, left=None, right=None):
    if left is None and right is None:
        left, right = 0, len(nums) - 1

    if left < right:
        pivot_index = partition(nums, left, right)
        quicksort(nums, left, pivot_index - 1)
        quicksort(nums, pivot_index + 1, right)

def partition(nums, left, right):
    randomIndex = left + random.randint(0, right - left)
    nums[left], nums[randomIndex] = nums[randomIndex], nums[left]
    pivot = nums[left]

    le, ge = left + 1, right

    while le <= ge:
        while le <= ge and nums[le] < pivot:
            le += 1
        while le <= ge and nums[ge] > pivot:  # until nums[le] > pivot, nums[ge] < pivot
            ge -= 1

        if le <= ge:
            nums[le], nums[ge] = nums[ge], nums[le]
            le += 1
            ge -= 1

    nums[left], nums[ge] = nums[ge], nums[left]
    return ge

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
quicksort(nums)
print(nums) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
