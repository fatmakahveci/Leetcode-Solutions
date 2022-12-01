class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        1 2 3 4 5 6 7 8 9 10 ...
        single 5 = one trailing zero 
        n = 5 => 1
        n = 10 => 2
        n = 15 => 3
        ...
        n = 100 => 20
        ...
        '''
        counter = 0
        while n > 0:
            n //= 5
            counter += n
        return counter
