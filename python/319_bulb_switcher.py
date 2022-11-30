class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''
           1 2 3 4 5 6 7 8 9
        1: o o o o o o o o o
        2: o x o x o x o x o
        3: o x x x o o o x x
        4: o x x o o o o o x
        5: o x x o x o o o x
        6: o x x o x x o o x
        7: o x x o x x x o x
        8: o x x o x x x x x
        9: o x x o x x x x o
        '''
        return int(n**0.5)
