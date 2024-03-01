'''
Given an array nums containing n + 1 integers in the range [1, n] (including 1 and n), we know that there is at least one duplicate integer. 
Assuming nums has only one duplicate integer, return the duplicate number. The solution you design must not modify the array nums and only use the extra space of the constant level O(1). 

Example 1: Input: nums = [1,3,4,2,2] Output: 2 Example 2: Input: nums = [3,1,3,4,2] Output: 3
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            cnt = sum(num <= mid for num in nums)   # nums中 <=mid 的元素个数
            if cnt <= mid:      # 目标元素在mid右侧
                left = mid+1
            else:
                right = mid
        
        return left


# Example usage
solution = Solution()
nums = [1, 3, 4, 2, 2]
print(solution.findDuplicate(nums))  # Output will be 2
