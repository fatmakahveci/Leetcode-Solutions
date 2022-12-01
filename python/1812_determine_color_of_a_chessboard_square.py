class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x, y = ord(coordinates[0])-96, int(coordinates[1])
        return x % 2 != y % 2
