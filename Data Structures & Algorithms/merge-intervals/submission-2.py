class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()
        if len(intervals) == 0:
            return []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            prevstart = prev[0]
            prevend = prev[1]
            curstart = intervals[i][0]
            curend = intervals[i][1]
            if prevend >= curstart:
                prev[1] = max(prevend, curend)
            else:
                result.append(prev)
                prev = intervals[i]
        result.append(prev)
        return result