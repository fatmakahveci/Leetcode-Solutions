class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        num1_counter_dict = dict()
        common_nums_list = []
        
        for num1 in nums1:
            num1_counter_dict[num1] = 1 if num1 not in num1_counter_dict else num1_counter_dict[num1] + 1
                
        for num2 in nums2:
            if num2 in num1_counter_dict and num1_counter_dict[num2] != 0:
                common_nums_list.append(num2)
                num1_counter_dict[num2] -= 1

        return common_nums_list
