class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        i = 0
        while i < len(arr):
            j = 0
            while j < len(arr):
                if arr[i] == arr[j] * 2 and i != j:
                    return True
                j += 1
            i += 1
        return False
