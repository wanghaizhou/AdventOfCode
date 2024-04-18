from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        end_pos = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if end_pos <= intervals[i][0]:
                count += 1
                end_pos = intervals[i][1]

        return len(intervals) - count



l =  Solution().eraseOverlapIntervals([[2,8],[3,9]])
print(l)