class Solution:
    def interpret(self, command: str) -> str:

        res = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                res.append("G")
            elif command[i+1] == ")":
                i += 1
                res.append("o")
            else:
                res.append("al")
                i += 3
            i += 1
        return "".join(res)
