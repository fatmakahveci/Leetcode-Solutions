class MyQueue:
    '''
    3
    2
    1
    
    s: 1 2 3
    
    stack: push(4)
    
    s1: 1 2 3 4
    s1.pop() # 4
    s1: 1 2 3
    s1.pop() # 3
    s1: 1 2
    s1.pop() # 2
    s1: 1
    s1.pop() #
    s1:
    
    
    s2: _ _ _ _
    s2.append(4)
    s2: 4 _ _ _
    s2.append(3)
    s2: 4 3 _ _
    s2.append(2)
    s2: 4 3 2 _
    s2.append(1)
    s2: 4 3 2 1
    
    
    q: push(4)
    
    x 3 2 1 4
    
    4 3 2 1
    '''
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
        return x

    def pop(self) -> int:
        if self.s1:
            return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
