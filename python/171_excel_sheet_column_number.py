class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        sum_ = 0
        for i,ch in enumerate(columnTitle[::-1]):
            sum_ += pow(26,i) * (ord(ch)-64) # ascii to int
        return sum_
