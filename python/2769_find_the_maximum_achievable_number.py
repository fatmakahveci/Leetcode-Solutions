class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        '''
        num=4 t=1
        x-1   num+1
        6     5

        x-1   num+1
        x-1   3+1
        x-1   4+1
        x-2 = num + t
        x = num + 2t
        '''
        return num + 2 * t
