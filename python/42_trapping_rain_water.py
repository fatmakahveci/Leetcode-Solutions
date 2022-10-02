class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for i, h in enumerate(height):
            while stack and h >= stack[-1][0]:
                popped, _ = stack.pop()
                if stack:
                    left_border, j = stack[-1]
                    water += min(left_border-popped, h-popped)*(i-j-1)
            stack.append((h,i))
        return water
