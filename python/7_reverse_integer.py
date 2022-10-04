class Solution:
    def reverse(self, x: int) -> int:
        retval = int(str(abs(x))[::-1])

        if retval.bit_length() > 31:
            return 0

        return -1 * retval if x < 0 else retval
