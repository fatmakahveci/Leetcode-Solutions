class Solution:
    def numberOfSteps (self, num: int) -> int:
        no_steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

            no_steps += 1

        return no_steps
