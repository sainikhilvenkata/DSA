# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.res=0
        
        def dfs(root,left_side):
            
            if not root:
                return 0
            left=dfs(root.left,True)
            
            right=dfs(root.right,False)
            if not root.left and not root.right and left_side:
                self.res+=root.val
            return self.res
        return dfs(root,False)
        