"""
Kth Largest Element in an Array
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.


Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5


Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""

from utils.timer import timer
import heapq

@timer
def solution1(nums: list, k: int) -> int:
    tmp = sorted(nums, reverse=True)
    return tmp[k-1]


def heap(nums, k):
    return heapq.nlargest(k, nums)[-1]


# solution1([3,2,1,5,6,4], 2)                 # Output: 5
# solution1([3,2,3,1,2,4,5,5,6], 4)           # Output: 4

heap([3,2,1,5,6,4], 2)                 # Output: 5
heap([3,2,3,1,2,4,5,5,6], 4)           # Output: 4