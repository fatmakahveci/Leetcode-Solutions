class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [ self.bisect(nums, target, 'left'), self.bisect(nums, target, 'right') ]
    
    def bisect(self, nums: List[int], target: int, side: str) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                if side == 'left':
                    if mid == low or nums[mid - 1] < target:
                        return mid
                    high = mid - 1
                else:
                    if mid == high or nums[mid + 1] > target:
                        return mid
                    low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
