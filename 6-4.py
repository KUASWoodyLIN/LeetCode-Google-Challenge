from utils.timer import timer


class SolutionV1:
    @timer
    def insert(self, intervals: list, newInterval: list) -> list:
        new_s, new_e = newInterval
        if not intervals:
            return [newInterval]
        elif new_e < intervals[0][0]:
            return [newInterval] + intervals
        elif new_s > intervals[-1][1]:
            return intervals + [newInterval]
        elif new_s < intervals[0][0]:
            start_idx = -1
        else:
            start_idx = 0
            for i in range(len(intervals)-1, -1, -1):
                s, e = intervals[i]
                if new_s <= e:
                    if new_s <= s and new_s <= intervals[i-1][1]:
                        start_idx = i -1
                    else:
                        start_idx = i
                else:
                    break

        if new_e >= intervals[-1][1]:
            end_idx = len(intervals)
        else:
            end_idx = start_idx
            for i in range(len(intervals)):
                s, e = intervals[i]
                if new_e >= s:
                    if (new_e >= e) and (new_e >= intervals[i+1][0]):
                        end_idx = i + 1
                    else:
                        end_idx = i
                else:
                    break

        insert_vals = [
            [
                min(intervals[start_idx][0], newInterval[0]) if start_idx != -1 else newInterval[0],
                max(intervals[end_idx][1], newInterval[1]) if end_idx != len(intervals) else newInterval[1]
            ]
        ]
        if start_idx != -1:
            return intervals[:start_idx] + insert_vals + intervals[end_idx + 1:]
        else:
            return insert_vals + intervals[end_idx + 1:]

# input1 = [[1,3],[6,9]]
# input2 = [2,5]
input1 = [[1,5],[6,8]]
input2 = [0,9]

S = SolutionV1()
S.insert(input1, input2)