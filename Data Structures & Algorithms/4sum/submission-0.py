class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-3):
            num1 = nums[i]
            if i > 0 and num1 == nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)-2):
                num2 = nums[j]
                if j > i+1:
                    if num2 == nums[j-1]:
                        continue
                
                left = j+1
                right = len(nums)-1
                while left < right:
                    num3 = nums[left]
                    num4 = nums[right]
                    total = num1 + num2 + num3 + num4
                    if total == target:
                        answer.append(sorted([num1, num2,num3, num4]))
                        left += 1
                        right -=1

                        while left < right and nums[left] == nums[left-1]:
                            left +=1

                        while left < right and nums[right] == nums[right+1]:
                            right -=1
                    elif total < target:
                            left +=1
                        
                    elif total > target:
                            right -=1

        return answer

