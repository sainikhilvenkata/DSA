# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left,right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.val== right.val:
                a=dfs(left.left,right.right)
                b=dfs(left.right,right.left)
            else:
                return False
            if a and b:
                return True
            else:
                False
                
        return dfs(root.left,root.right)
            
            
        