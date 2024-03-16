'''
Generate all possible intervals without using nested loops is to use a recursive function.
Calculate the sum of each interval mode, and if multiple numbers occur the most, choose the smallest number
'''

from collections import Counter

def get_mode_sum(arr):
    # Calculate the occurrence count of each number in the array
    counter = Counter(arr)
    # Find the number with the highest occurrence count
    most_common = counter.most_common()
    # print(most_common)
    max_count = most_common[0][1]
    min_most_common = min(num for num, count in most_common if count == max_count)
    return min_most_common

def get_intervals_with_mode_sum(arr):
    intervals = []
    n = len(arr)
    # Generate all possible intervals of the array
    for i in range(n):
        for j in range(i, n):
            # Calculate the mode sum for each interval
            intervals.append((arr[i:j+1], get_mode_sum(arr[i:j+1])))
    return intervals

# Define the array
arr = [2, 1, 2]
# Get intervals with their mode sums
intervals = get_intervals_with_mode_sum(arr)
# Calculate the sum of mode sums for all intervals and print the result
print(sum(item[1] for item in intervals))
