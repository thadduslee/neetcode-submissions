"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
    
        count = 0
        largest = 0
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        i = 0
        j= 0
        while i < len(start):
            if start[i] < end[j]:
                count +=1
                largest = max(largest, count)
                i+=1
            else:
                j+=1
                count -=1
        return largest
            
