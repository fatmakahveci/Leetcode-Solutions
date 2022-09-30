class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 0
        is_increasing, is_decreasing = False, False
        while i < len(arr)-1:
            if arr[i] < arr[i+1]:
                is_increasing = True
            else:
                break
            i += 1
        if is_increasing:
            while i < len(arr)-1:
                if arr[i] > arr[i+1]:
                    is_decreasing = True
                else:
                    return False
                i += 1
        else:
            return False
        if not is_decreasing:
            return False
        return True
