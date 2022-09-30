class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        # odd
        stack = []
        next_odd_jump = [0] * n
        for i,_ in sorted(enumerate(arr), key=lambda x:x[1]):
            while stack and stack[-1] < i:
                next_odd_jump[stack.pop()] = i
            stack.append(i)
        
        # even
        stack = []
        next_even_jump = [0] * n
        for i,_ in sorted(enumerate(arr), key=lambda x:x[1], reverse=True):
            while stack and stack[-1] < i:
                next_even_jump[stack.pop()] = i
            stack.append(i)
        
        odd_start_good, even_start_good = [0] * n, [0] * n
        
        odd_start_good[-1] = 1
        even_start_good[-1] = 1
        
        for i in range(n-2, -1, -1):
            i_next_odd = next_odd_jump[i]
            if i_next_odd and even_start_good[i_next_odd]:
                odd_start_good[i] = 1

            i_next_even = next_even_jump[i]
            if i_next_even and odd_start_good[i_next_even]:
                even_start_good[i] = 1

        return sum(odd_start_good)
