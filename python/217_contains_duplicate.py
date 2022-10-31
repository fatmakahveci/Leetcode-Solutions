class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        1 2 3 1
        
        hash_map = {1: 1, 2: 1, 3: 1} -> if num in hash_map return False
        
        1 2 3 4
        
        hash_map = {1: 1, 2: 1, 3:1, 4: 1} -> return True
        
        1 1 1 3 3 4 3 2 4 2
        
        '''
        from collections import Counter
        
        for num, cnt in Counter(nums).items():
            if cnt >= 2:
                return True

        return False
