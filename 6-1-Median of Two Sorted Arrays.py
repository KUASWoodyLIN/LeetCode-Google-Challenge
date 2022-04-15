"""
Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from utils.timer import timer


class Solution:
    @timer
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        # new_order = []
        # left, right = 0, 0
        # while (left_bool := left < len(nums1)) or (right < len(nums2)):
        #     right_bool = right < len(nums2)
        #     if not right_bool or (left_bool and (nums1[left] < nums2[right])):
        #         new_order.append(nums1[left])
        #         left += 1
        #     elif right_bool:
        #         new_order.append(nums2[right])
        #         right += 1
        # idx = len(new_order)//2
        # if len(new_order) % 2:
        #     return new_order[idx]
        # return (new_order[idx] + new_order[idx-1]) / 2

        new_order = []
        left, right = 0, 0
        max_overall_index = len(nums1) + len(nums2)
        while len(new_order) < max_overall_index:
            right_bool = right < len(nums2)
            if not right_bool or ((left < len(nums1)) and (nums1[left] < nums2[right])):
                new_order.append(nums1[left])
                left += 1
            else:
                new_order.append(nums2[right])
                right += 1
        idx = len(new_order) // 2
        if len(new_order) % 2:
            return new_order[idx]
        return (new_order[idx] + new_order[idx - 1]) / 2


class SolutionV2:
    @timer
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        l = len(nums1)
        if l % 2 != 0:
            median = nums1[l // 2]
        else:
            l1 = l // 2 - 1
            median = (nums1[l1] + nums1[l1 + 1]) / 2
        return median


class SolutionV3:
    @timer
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        l = len(nums1) + len(nums2)
        return self.findKth(nums1, nums2, l // 2) if l % 2 == 1 else (self.findKth(nums1, nums2, l // 2 - 1) +
                                                                      self.findKth(nums1, nums2, l // 2)) / 2.0

    def findKth(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums1:
            return nums2[k]
        if k == len(nums1) + len(nums2) - 1:
            return max(nums1[-1], nums2[-1])
        i = len(nums1) // 2
        j = k - i
        if nums1[i] > nums2[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(nums1[:i], nums2[j:], i)
        else:
            return self.findKth(nums1[i:], nums2[:j], j)


nums1 = [1,3]
nums2 = [2]
# nums1 = [1,2]
# nums2 = [3,4]
# S = Solution()
# S = SolutionV2()
S = SolutionV3()
S.findMedianSortedArrays(nums1, nums2)