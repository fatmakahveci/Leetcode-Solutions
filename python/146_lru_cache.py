class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.nxt = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    # remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev
        
    # add to the right
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
