# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isMirror(self, left_root, right_root):
        if left_root is None and right_root is None:
            return True

        if left_root is not None and right_root is not None:
            if left_root.val == right_root.val:
                return self.isMirror(right_root.left, left_root.right) and self.isMirror(left_root.right, right_root.left)
        return False
 

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)
