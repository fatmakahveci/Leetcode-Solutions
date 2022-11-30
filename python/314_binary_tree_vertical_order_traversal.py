# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        BFS: level order traversal
        '''
        
        from collections import defaultdict, deque

        if not root:
            return []
        
        vertical_nodes = defaultdict(list)
        
        min_x, max_x = float('inf'), float('-inf')
        
        q = deque([(0, root)])
        visited = []
        
        while q:
            x, node = q.popleft()
            vertical_nodes[x].append(node.val)
            
            min_x, max_x = min(min_x, x), max(max_x, x)

            if node.left:
                q.append((x-1, node.left))
            if node.right:
                q.append((x+1, node.right))
        
        for level in range(min_x, max_x+1):
            visited.append(vertical_nodes[level])

        return visited
