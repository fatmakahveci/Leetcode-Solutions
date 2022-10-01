class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = { '(': ')', '{': '}', '[': ']' }
        stack = []
        for ch in s:
            if ch in par_dict:
                stack.append(ch)
            elif not stack or par_dict[stack.pop()] != ch:
                return False
        return not stack
