class RandomizedSet:

    def __init__(self):
        self.vals = {}

    def insert(self, val: int) -> bool:
        if self.vals.get(val):
            return False
        self.vals[val] = True
        return True

    def remove(self, val: int) -> bool:
        if self.vals.get(val):
            self.vals.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.vals.keys()))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
