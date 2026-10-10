class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                
                else:
                    low = mid + 1
            
            elif nums[mid] <= nums[low]:
                if nums[mid+1] <= target <= nums[high]:
                    low = mid + 1
                
                else:
                    high = mid -1
        return -1

