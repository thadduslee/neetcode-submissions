class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-1

        while right-left+1 > k:
            num_left = arr[left]
            diff_left = abs(num_left - x)
            num_right = arr[right]
            diff_right = abs(num_right-x)
        
            if diff_left < diff_right:
                right -=1
            
            elif diff_left > diff_right:
                left +=1
            
            elif diff_left == diff_right:
                right-=1
        return arr[left:right+1]