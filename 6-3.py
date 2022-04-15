from utils.timer import timer

class Solution:
    @timer
    def merge(self, intervals: list) -> list:
        result = []
        intervals.sort(key=lambda x: x[0])
        pointer = 0
        tmp_min, tmp_max = intervals[pointer]
        pointer += 1
        while pointer < len(intervals):
            if tmp_max >= intervals[pointer][0]:
                tmp_max = max(tmp_max, intervals[pointer][1])
            else:
                result.append([tmp_min, tmp_max])
                tmp_min = intervals[pointer][0]
                tmp_max = intervals[pointer][1]
            pointer += 1
        result.append([tmp_min, tmp_max])
        return result


inputs = [[1,4],[0,4]]
# Output: [[0,4]]
S = Solution()
S.merge(inputs)
