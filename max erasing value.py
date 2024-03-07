'''
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).


Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
'''

def maximumUniqueSubarray(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    max_score = 0
    curr_score = 0
    unique_set = set()
    left = 0
    
    for right in range(n):
        while nums[right] in unique_set:
            curr_score -= nums[left]
            unique_set.remove(nums[left])
            left += 1
        
        unique_set.add(nums[right])
        curr_score += nums[right]
        max_score = max(max_score, curr_score)
    
    # print("Unique set:", unique_set)
    return max_score

nums = [1, 3, 4, 4, 2, 4, 5, 6, 7, 6]
result = maximumUniqueSubarray(nums)
print("Maximum unique subarray score:", result)

