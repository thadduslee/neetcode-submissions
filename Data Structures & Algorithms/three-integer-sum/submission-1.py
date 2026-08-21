class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        for index, value in enumerate(nums):
            if value > 0:
                break
            if index > 0 and value == nums[index-1]:
                continue
            
            left, right = index+1, len(nums)-1
            while left < right:
                threesum = value + nums[left] + nums[right]
                if threesum > 0:
                    right -=1
                elif threesum < 0:
                    left +=1
                
                else:
                    answer.append([value, nums[left], nums[right]])
                    left+=1
                    right -=1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return answer