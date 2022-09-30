class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first, second, third = nums[0], float('-inf'), float('-inf')
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            for num in nums:
                if (first < num):
                    third, second, first = second, first, num
                elif(second < num and num < first):
                    third, second = second, num
                elif(third < num and num < second):
                    third = num
                        
        return third if third != float('-inf') else first
