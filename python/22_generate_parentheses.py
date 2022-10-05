class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      '''
      res = [((()))]
      s = ((
      f(0,0) -> f*(1,0) -> f**(2,0)
      '''
        if n == 0:
            return []

        res = []
        stack = []
        
        def backtrack(num_open, num_closed):
            
            if num_open == num_closed == n:
                res.append(''.join(stack))
                return

            if num_open < n:
                stack.append('(')
                backtrack(num_open+1, num_closed)
                stack.pop()

            if num_closed < num_open:
                stack.append(')')
                backtrack(num_open, num_closed+1)
                stack.pop()
            
        backtrack(0, 0)
        
        return res
