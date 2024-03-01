'''
Given an array nums containing n + 1 integers in the range [1, n] (including 1 and n), we know that there is at least one duplicate integer. 
Assuming nums has only one duplicate integer, return the duplicate number. The solution you design must not modify the array nums and only use the extra space of the constant level O(1). 

Example 1: Input: nums = [1,3,4,2,2] Output: 2 Example 2: Input: nums = [3,1,3,4,2] Output: 3
'''

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Suppose nums = [1, 3, 4, 2, 2]
        slow, fast = 0, 0
        
        # Finding the intersection point of slow and fast pointers
        while True:
            slow = nums[slow]           # Similar to slow = slow.next in a linked list
            fast = nums[nums[fast]]     # Similar to fast = fast.next.next in a linked list
            if fast == slow:    # Intersection point
                break
        
        fast = 0                # Move fast pointer back to the start
        while slow != fast:     # Finding the entry point of the cycle
            slow = nums[slow]
            fast = nums[fast]
        
        return fast

# Example usage
solution = Solution()
nums = [1, 3, 4, 2, 2]
print(solution.findDuplicate(nums))  # Output will be 2
