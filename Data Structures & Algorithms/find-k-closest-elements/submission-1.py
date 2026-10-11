class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        answer = []
        closest_index = 0
        closest = float('inf')

        for i in range(len(arr)):
            if abs(arr[i]-x) < closest:
                closest = abs(arr[i]- x)
                closest_index = i
        
        answer.append(arr[closest_index])
        left = closest_index-1
        right = closest_index+1

        while left >= 0 and right < len(arr) and len(answer) != k:
            num_left = arr[left]
            diff_left = abs(num_left-x)
            num_right = arr[right]
            diff_right = abs(num_right-x)

            if diff_left < diff_right:
                answer.append(num_left)
                left-=1
            
            elif diff_left > diff_right:
                answer.append(num_right)
                right+=1
            
            elif diff_left == diff_right:
                answer.append(num_left)
                left-=1
        
        while left >= 0 and len(answer) != k:
            answer.append(arr[left])
            left-=1
        
        while right < len(arr) and len(answer) !=k:
            answer.append(arr[right])
            right +=1
        answer.sort()
        return answer
            