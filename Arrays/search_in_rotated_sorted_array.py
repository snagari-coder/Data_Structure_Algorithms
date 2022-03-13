# Leetcode 33
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start,end = 0, len(nums)-1
        while start <= end:
            mid = (end-start)//2 + start
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid-1
        return -1
# Time = O(log n)
# space = O(1)
        
