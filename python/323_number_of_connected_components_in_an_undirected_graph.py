class DisjointSet:
    
    def __init__(self, size):
        self.root = [ i for i in range(size) ]
        self.count = size
    
    def find(self, x):
        while x != self.root[x]:
            x = self.find(self.root[x])
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            self.root[root_y] = root_x
            self.count -= 1
    
    def get_count(self):
        return self.count

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint_set = DisjointSet(n)
        
        for edge in edges:
            disjoint_set.union(edge[0], edge[1])
        
        return disjoint_set.get_count()

		
