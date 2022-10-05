class Solution:
    
    def letterCombinations(self, digits: str) -> List[str]:
        
        letters = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9': 'wxyz' }
        
        combination = [''] if digits else []
        
        for digit in digits:
        
            combination = [ c + l for c in combination for l in letters[digit] ]
        
        return combination
