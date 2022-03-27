"""
Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:
Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.

Example 3:
Input: seats = [0,1]
Output: 1
"""
from utils.timer import timer


@timer
def solution1(seats: list) -> int:
    now = 0
    max_distance = 0
    while now < len(seats):
        if seats[now]:
            now += 1
        else:
            # tmp_distance = 1
            left_distance, right_distance = False, False
            if 1 in seats[:now]:
                left_distance = seats[:now][::-1].index(1)+1
            if 1 in seats[now:]:
                right_distance = seats[now:].index(1)
            if left_distance and not right_distance:
                tmp_distance = left_distance
            elif right_distance and not left_distance:
                tmp_distance = right_distance
            else:
                tmp_distance = min(left_distance, right_distance)
            max_distance = max(tmp_distance, max_distance)
            now+= 1
    return max_distance



# solution1([1,0,0,0,1,0,1])      # Output: 2
# solution1([1,0,0,0])            # Output: 3
# solution1([0,1])                # Output: 1
solution1([0,0,1])                # Output: 2
