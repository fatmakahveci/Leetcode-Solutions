class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        '''
        stack: push(5)
        
        1 2 3 4
        
        4
        3
        2
        1
             
        q: push(5)
        
        4 3 2 1
        |
        v
        5 4 3 2 1 => 1 2 3 4 5
        
        '''
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
