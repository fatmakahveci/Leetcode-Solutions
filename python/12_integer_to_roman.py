class Solution:
    def intToRoman(self, num: int) -> str: 

        roman = ""
        for r, i in zip(['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'], [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]):
            
            if num >= i:
                roman += int(num / i) * r
                num %= i
        return roman
