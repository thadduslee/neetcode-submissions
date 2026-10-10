class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0

        while left <= right:
            if people[right] == limit:
                count +=1
                right -=1
            else:
                difference = limit - people[right]
                right-=1
                if difference <= 0:
                    continue
                if left < len(people) and difference - people[left] >= 0:
                    left +=1
                count+=1
        return count
                    