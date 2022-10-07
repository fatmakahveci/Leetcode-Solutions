class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        num1 = num1[::-1]
        num2 = num2[::-1]

        ans = [0] * (len(num1) + len(num2))

        for i, n2 in enumerate(num2):
            for j, n1 in enumerate(num1):
                num_zeros = i + j
                carry = ans[num_zeros]
                
                mult = int(n1) * int(n2) + carry
                ans[num_zeros] = mult % 10
                ans[num_zeros + 1] += mult // 10
        if ans[-1] == 0:
            ans.pop()
        
        return ''.join(str(digit) for digit in reversed(ans))
