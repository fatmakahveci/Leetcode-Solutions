class Solution:
    def read(self, buf: List[str], n: int) -> int:
        num_read = 0
        buf4 = [''] * 4
        EOF = False
        while not EOF and num_read < n:
            curr_read = read4(buf4)
            delta = min(curr_read, n-num_read)
            buf[num_read:num_read+4] = buf4[:delta]
            num_read += delta
            if curr_read < 4:
                EOF = True

        return num_read
