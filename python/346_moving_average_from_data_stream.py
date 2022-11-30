class MovingAverage:

    def __init__(self, size: int):
        self.queue = []
        self.count = 0
        self.capacity = size

    def next(self, val: int) -> float:
        if self.count >= self.capacity:
            self.queue.pop(0)
        else:
            self.count += 1
        self.queue.append(val)
        return sum(self.queue) / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
