# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorder = deque(preorder)
        
        mapper = {}
        
        for i, n in enumerate(inorder): mapper[n] = i

        def helper(low, high):
            
            
            if low > high: return
            
            root = TreeNode(preorder.popleft())
            middle = mapper[root.val]
            root.left = helper(low, middle-1)
            root.right = helper(middle+1, high)
            return root
            
        return helper(0, len(inorder)-1)
     
