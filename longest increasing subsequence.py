'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
'''

def lengthOfLIS(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
nums1 = [10, 11, 13, 4, 8, 12]
print("Example 1:")
print("Input:", nums1)
print("Output:", lengthOfLIS(nums1))

# nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
# print("Example 1:")
# print("Input:", nums1)
# print("Output:", lengthOfLIS(nums1))

# nums2 = [0, 1, 0, 3, 2, 3]
# print("\nExample 2:")
# print("Input:", nums2)
# print("Output:", lengthOfLIS(nums2))

# nums3 = [7, 7, 7, 7, 7, 7, 7]
# print("\nExample 3:")
# print("Input:", nums3)
# print("Output:", lengthOfLIS(nums3))
