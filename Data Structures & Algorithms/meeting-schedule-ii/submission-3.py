"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        intervals.sort(key = lambda x:x.start)

        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        i = 0
        j = 0
        count = 0
        largest = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                count +=1
                largest = max(count, largest)
                i+=1
            else:
                j+=1
                count -=1

        return largest