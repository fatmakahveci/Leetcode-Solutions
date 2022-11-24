class OrderedStream:
    def __init__(self, n: int):    
        self.data = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey] = value
        if idKey == self.ptr:
            while self.ptr < len(self.data) and self.data[self.ptr]:
                self.ptr += 1
            return self.data[idKey:self.ptr]
        return []
