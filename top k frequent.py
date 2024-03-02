'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
'''

def topKFrequent(nums, k):
    # Count the occurrences of each number in the array
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Sort the dictionary by the values (occurrences) in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print(sorted_counts)

    # Return the first k keys (numbers)
    return [x[0] for x in sorted_counts[:k]]
# Test cases
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(topKFrequent([1], 1))            # Output: [1]
