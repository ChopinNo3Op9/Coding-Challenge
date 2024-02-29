'''
Given a sequence nums that can contain duplicate numbers, return all non-duplicate full permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
,1,2 [[1],
[1, 2, 1].
,1,1 [2]]
Example 2:

Input: nums = [1,2,3]
Output: [[1, 2, 3], [31] 1,,1,3 [2], [2,3,1], [3,1,2], [3, 2, 1]]
'''

from typing import List
import collections

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, counter):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in counter:
                # print(num)
                if counter[num] > 0:
                    path.append(num)
                    counter[num] -= 1
                    backtrack(path, counter)
                    path.pop()
                    counter[num] += 1
        
        result = []
        counter = collections.Counter(nums)
        # print(counter)
        backtrack([], counter)
        return result

# Example usage
solution = Solution()
print(solution.permuteUnique([1, 1, 2]))
