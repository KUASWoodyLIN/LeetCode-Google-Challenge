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
import itertools
from utils.timer import timer


# ==================================================================================================================== #
# ===================================================== Solution1 ==================================================== #
# ==================================================================================================================== #
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


# ==================================================================================================================== #
# ===================================================== Solution2 ==================================================== #
# ==================================================================================================================== #
@timer
def solution2(seats: list) -> int:
    last_index = len(seats) - 1
    left_right_tmp, right_left_tmp = [-1]*len(seats), [len(seats)]*len(seats)
    left_right_tmp[0] = 0 if seats[0] else -1
    right_left_tmp[-1] = last_index if seats[last_index] else len(seats)
    for i, j in zip(range(1, len(seats)), range(len(seats)-2, -1, -1)):
        if seats[i] == 1:
            left_right_tmp[i] = i
        else:
            left_right_tmp[i] = left_right_tmp[i-1]
        if seats[j] == 1:
            right_left_tmp[j] = j
        else:
            right_left_tmp[j] = right_left_tmp[j+1]

    max_distance = max(right_left_tmp[0]-0, last_index-left_right_tmp[-1])
    for now in range(1, len(seats)-1):
        if seats[now]:
            continue
        if left_right_tmp[now-1] == -1:
            max_distance = max(max_distance, right_left_tmp[now+1]-now)
        elif right_left_tmp[now+1] == len(seats):
            max_distance = max(max_distance, now-left_right_tmp[now-1])
        else:
            max_distance = max(max_distance, min(now-left_right_tmp[now-1], right_left_tmp[now+1]-now))
    return max_distance


# ==================================================================================================================== #
# ===================================================== Solution3 ==================================================== #
# ==================================================================================================================== #
# Next Array
@timer
def solution3(seats: list) -> int:
    N = len(seats)
    left, right = [N] * N, [N] * N

    for i in range(N):
        if seats[i] == 1:
            left[i] = 0
        elif i > 0:
            left[i] = left[i-1] + 1

    for i in range(N-1, -1, -1):
        if seats[i] == 1:
            right[i] = 0
        elif i < N-1:
            right[i] = right[i+1] + 1

    # return max(min(left[i], right[i])
    #            for i, seat in enumerate(seats) if not seat)
    return max(min(l, r) for l, r in zip(left, right))

# ==================================================================================================================== #
# ===================================================== Solution4 ==================================================== #
# ==================================================================================================================== #
# Two Pointer
@timer
def solution4(seats: list) -> int:
    people = (i for i, seat in enumerate(seats) if seat)
    prev, future = None, next(people)

    ans = 0
    for i, seat in enumerate(seats):
        if seat:
            prev = i
        else:
            while future is not None and future < i:
                future = next(people, None)

            left = float('inf') if prev is None else i - prev
            right = float('inf') if future is None else future - i
            ans = max(ans, min(left, right))

    return ans


# ==================================================================================================================== #
# ===================================================== Solution5 ==================================================== #
# ==================================================================================================================== #
# Group by Zero
@timer
def solution5(seats: list) -> int:
    ans = seats.index(1)
    seats.reverse()
    ans = max(ans, seats.index(1))
    for seat, group in itertools.groupby(seats):
        if not seat:
            K = len(list(group))
            ans = max(ans, (K + 1) / 2)

    return ans


# solution1([1,0,0,0,1,0,1])      # Output: 2
# solution1([1,0,0,0])            # Output: 3
# solution1([0,1])                # Output: 1
# solution1([0,0,1])                # Output: 2


# solution2([1,0,0,0,1,0,1])      # Output: 2
# solution2([1,0,0,0])            # Output: 3
# solution2([0,1])                # Output: 1
# solution2([0,0,1])              # Output: 2
# solution2([0,1,0,1,0])          # Output: 1

solution3([1,0,0,0,1,0,1])      # Output: 2
solution3([1,0,0,0])            # Output: 3
solution3([0,1])                # Output: 1
solution3([0,0,1])              # Output: 2
solution3([0,1,0,1,0])          # Output: 1

# solution4([1,0,0,0,1,0,1])      # Output: 2
# solution4([1,0,0,0])            # Output: 3
# solution4([0,1])                # Output: 1
# solution4([0,0,1])              # Output: 2
# solution4([0,1,0,1,0])          # Output: 1


# solution5([1,0,0,0,1,0,1])      # Output: 2
# solution5([1,0,0,0])            # Output: 3
# solution5([0,1])                # Output: 1
# solution5([0,0,1])              # Output: 2
# solution5([0,1,0,1,0])          # Output: 1