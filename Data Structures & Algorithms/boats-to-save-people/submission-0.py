class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        left = 0
        right = len(people)-1
        people.sort()
        while left <= right:
            total = people[left] + people[right]
            if total <= limit:
                count +=1
                left +=1
                right -=1
            elif total > limit and people[right] <= limit:
                right -=1
                count+=1
        return count
                