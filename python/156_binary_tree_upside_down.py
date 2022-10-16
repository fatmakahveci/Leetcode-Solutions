# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or (not root.left and not root.right):
            return root
        new_root = self.upsideDownBinaryTree(root.left) # 4
        root.left.left = root.right
        root.left.right = root
        root.left = None
        root.right = None
        return new_root
        '''
                                    1 [l=2, r=3]
                                
                2 [l=4, r=5]                            3 [l=N, r=N]
        
        4 [l=N, r=N]          5 [l=N, r=N]
        
                                
                    4 [l=5, r=2]                    
        
            5 [l=N, r=N]              2 [l=3, r=1]
            
                            3 [l=N, r=N]        1 [l=N, r=N]
        
        
        
                                    4 [l=5, r=2]
                                
                5 [l=N, r=N]                            2 [l=3, r=1]
        
                                           3 [l=N, r=N]          1 [l=N, r=N]

        f(1) <=4 f(2) <=4 f(4)
        '''
    
