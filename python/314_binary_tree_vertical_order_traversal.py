# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        level_dict = defaultdict(list)
        while q:
            node, level = q.popleft()
            if node:
                level_dict[level].append(node.val)
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level-1))
        return [ level_dict[k] for k in sorted(level_dict.keys(), reverse=True) ]
