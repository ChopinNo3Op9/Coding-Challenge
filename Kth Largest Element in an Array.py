'''
215. Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''
import heapq

def findKthLargest(nums, k):
        maxHeap = []
        for x in nums:
            heapq.heappush(maxHeap, -x)
        for i in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]
# test
nums = [3,2,3,1,2,4,5,5,6]
print(findKthLargest(nums, 4))
