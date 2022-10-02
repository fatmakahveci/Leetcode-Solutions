# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []
        def BFS(root: Optional[TreeNode]) -> List[Tuple]:
            q = deque([(root, 0, 0)])
            while q:
                node, row, col = q.popleft()
                if node:
                    node_list.append((col, row, node.val))
                    if node.left:
                        q.append((node.left, row+1, col-1))
                    if node.right:
                        q.append((node.right, row+1, col+1))
        BFS(root)
        
        node_list.sort()
        
        level_dict = OrderedDict()
        for col, row, val in node_list:
            if col in level_dict:
                level_dict[col].append(val)
            else:
                level_dict[col] = [val]
        return level_dict.values()
