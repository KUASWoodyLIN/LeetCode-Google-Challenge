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
def brute_force(height: list) -> int:
    total_water = 0
    for cur in range(1, len(height)-1):
        left_max = right_max = 0
        for i in height[:cur][::-1]:
            left_max = max(left_max, i)
        for j in height[cur+1:]:
            right_max = max(right_max, j)
        if (h := min(right_max, left_max)) > height[cur]:
            total_water += h - height[cur]
    return total_water


@timer
def solution1(height: list) -> int:
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

    last_left = left
    left = len(height) -2
    right = len(height) - 1
    while left >= last_left:
        if height[left] >= height[right]:
            for i in range(right-1, left, -1):
                total_water += min(height[left], height[right]) - height[i]
            right = left
            left -= 1
        else:
            left -= 1
    return total_water


@timer
def dp_solution(height: list) -> int:
    total_water = 0
    left_max = right_max = 0
    left_max_list = []
    right_max_list = []
    for i, j in zip(range(len(height)), range(len(height)-1, -1, -1)):
        left_max = max(left_max, height[i])
        right_max = max(right_max, height[j])
        left_max_list.append(left_max)
        right_max_list.insert(0, right_max)
    for i in range(1, len(height)-1):
        total_water += min(left_max_list[i], right_max_list[i]) - height[i]
    return total_water



# brute_force([0,1,0,2,1,0,1,3,2,1,2,1])        # Output: 6
# brute_force([4,2,0,3,2,5])                    # Output: 9
# brute_force([4,2,3])                            # Output: 1
#
# solution1([0,1,0,2,1,0,1,3,2,1,2,1])        # Output: 6
# solution1([4,2,0,3,2,5])                    # Output: 9
# solution1([4,2,3])                            # Output: 1

dp_solution([0,1,0,2,1,0,1,3,2,1,2,1])        # Output: 6
dp_solution([4,2,0,3,2,5])                    # Output: 9
dp_solution([4,2,3])                            # Output: 1
