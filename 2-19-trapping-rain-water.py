"""
Trapping Rain Water


Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""
from utils.timer import timer

@timer
def solution1(height: list) -> int:
    # left = 0
    # right = 1
    # total_water = 0
    # while right < len(height) or left < len(height)-1:
    #     if right == len(height):
    #         left += 1
    #         right = left + 1
    #     elif height[right] >= height[left]:
    #         for i in range(left+1, right):
    #             total_water += min(height[left], height[right]) - height[i]
    #         left = right
    #         right += 1
    #
    #     else:
    #         right += 1
    # return total_water
    left = 0
    right = 1
    total_water = 0
    while right < len(height):
        # if right == len(height):
        #     left += 1
        #     right = left + 1
        if height[right] >= height[left]:
            for i in range(left+1, right):
                total_water += min(height[left], height[right]) - height[i]
            left = right
            right += 1

        else:
            right += 1
    else:
        # right = left + 1
        # right_max = (height[right], right)
        # while right < len(height):
        #     right += 1
        #     if right_max[0] < height[right]:
        #         right_max = (height[right], right)
        last_left = left
        right -= 1
        while left >= last_left:
            if height[left] >= height[right]:
                for i in range(right-1, left, -1):
                    total_water += min(height[left], height[right]) - height[i]
                right = left
                left -= 1
            else:
                left -= 1
    return total_water


solution1([0,1,0,2,1,0,1,3,2,1,2,1])        # Output: 6
solution1([4,2,0,3,2,5])                    # Output: 9
solution1([4,2,3])                            # Output: 1