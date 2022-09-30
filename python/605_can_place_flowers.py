class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i, k = 0, 0
        
        while i < len(flowerbed)-1:
            if flowerbed[i] == 1:
                i += 2
            else:
                if flowerbed[i+1] == 1:
                    i += 3
                elif flowerbed[i+1] == 0:
                    k += 1
                    i += 2
        if i == len(flowerbed)-1 and flowerbed[i] == 0:
            k += 1
        
        if n <= k:
            return True
        return False
        
