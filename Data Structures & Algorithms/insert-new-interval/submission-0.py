class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        intervals.sort()
        for interval in intervals:
            if newInterval[0] <= interval[1] and interval[0] <= newInterval[1]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                continue
            else:
                results.append(interval)
        results.append(newInterval)
        results.sort()
        return results
