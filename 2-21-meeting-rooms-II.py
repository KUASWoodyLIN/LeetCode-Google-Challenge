"""
Meeting Rooms II
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.



Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:
1 <= intervals.length <= 104
0 <= starti < endi <= 106

"""
from utils.timer import timer
import heapq

@timer
def solution1(intervals: list) -> int:
    time = []
    for i in intervals:
        time.append(i[0])
        time.append(-i[1])
    time = sorted(time, key=abs)

    max_room = 0
    cur_room = 0
    i = 0
    while i < len(time)-1:
        if time[i] == -time[i+1]:
            i += 1
        elif time[i] >= 0:
            cur_room += 1
            max_room = max(max_room, cur_room)
        else:
            cur_room -= 1
        i += 1
    return max_room

@timer
def solution2(intervals: list) -> int:
    if not intervals:
        return 0

    start_order = sorted([i[0] for i in intervals])
    end_order = sorted([i[1] for i in intervals])
    start_pointer = end_pointer = 0
    used_rooms = 0
    while start_pointer < len(intervals):
        if start_order[start_pointer] >= end_order[end_pointer]:
            used_rooms -= 1
            end_pointer += 1
        start_pointer += 1
        used_rooms += 1
    return used_rooms


@timer
def priority_queues(intervals: list) -> int:
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    # The heap initialization
    free_rooms = []

    # Sort the meetings in increasing order of their start time.
    intervals.sort(key=lambda x: x[0])

    # Add the first meeting. We have to give a new room to the first meeting.
    heapq.heappush(free_rooms, intervals[0][1])

    # For all the remaining meeting rooms
    for i in intervals[1:]:

        # If the room due to free up the earliest is free, assign that room to this meeting.
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)

        # If a new room is to be assigned, then also we add to the heap,
        # If an old room is allocated, then also we have to add to the heap with updated end time.
        heapq.heappush(free_rooms, i[1])

    # The size of the heap tells us the minimum rooms required for all the meetings.
    return len(free_rooms)


# solution1([[0,30],[5,10],[15,20]])      # Output: 2
# solution1([[7,10],[2,4]])               # Output: 1
# solution1([[13,15],[1,13]])             # Output: 1
# solution1([[1,5],[8,9],[8,9]])          # Output: 2

solution2([[0,30],[5,10],[15,20]])      # Output: 2
solution2([[7,10],[2,4]])               # Output: 1
solution2([[13,15],[1,13]])             # Output: 1
solution2([[1,5],[8,9],[8,9]])          # Output: 2

# priority_queues([[0,30],[5,10],[15,20]])      # Output: 2
# priority_queues([[7,10],[2,4]])               # Output: 1
# priority_queues([[13,15],[1,13]])             # Output: 1
# priority_queues([[1,5],[8,9],[8,9]])          # Output: 2
