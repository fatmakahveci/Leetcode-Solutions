# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level_l = 1
        l = root.left
        while l:
            l = l.left
            level_l += 1
        
        level_r = 1
        r = root.right
        while r:
            r = r.right
            level_r += 1
        
        if level_l == level_r: # if it is a complete tree
            return 2**level_l - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
