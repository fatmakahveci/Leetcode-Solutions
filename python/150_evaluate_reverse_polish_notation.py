class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['*','/','+','-']:
                y = stack.pop()
                x = stack.pop()
                stack.append(int(eval(f"{x}{token}{y}")))
            else:
                stack.append(int(token))
        return stack.pop()
