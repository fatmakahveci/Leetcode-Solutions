class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                low = i+1
                high = len(nums)-1
                third_num = -nums[i]
                while low < high:
                    if nums[low] + nums[high] == third_num:
                        res.append([nums[low], nums[high], -third_num])
                        while low < high and nums[low] == nums[low+1]:
                            low += 1
                        while low < high and nums[high] == nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < third_num:
                        low += 1
                    elif nums[low] + nums[high] > third_num:
                        high -= 1

        return res
