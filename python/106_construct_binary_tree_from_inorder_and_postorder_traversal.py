# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapper = {}
        
        for i, v in enumerate(inorder):
            mapper[v] = i

        def helper(low, high):
            if low > high: return
            root = TreeNode(postorder.pop())
            middle = mapper[root.val]
            root.right = helper(middle+1, high)
            root.left = helper(low, middle-1)
            return root
            
        return helper(0, len(inorder)-1)
