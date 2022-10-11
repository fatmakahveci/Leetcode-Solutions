# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if not node:
            return 0
        height_l = self.height(node.left)
        height_r = self.height(node.right)
        if height_l > height_r:
            return height_l + 1
        return height_r + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.left) - self.height(root.right)) > 1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)
