class TwoSum:

    def __init__(self):
        self.sum_map = defaultdict(lambda: 0)

    def add(self, number: int) -> None:
        self.sum_map[number] += 1

    def find(self, value: int) -> bool:
        for number in self.sum_map:
            complement = value - number
            if complement not in self.sum_map:
                continue
            if complement != number or self.sum_map[complement] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
