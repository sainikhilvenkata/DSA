# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root,val):
            if not root:
                return 0
            val+=1
            p=dfs(root.left,val)
            q=dfs(root.right,val)
            val =max(val,p,q)
            return val
        return dfs(root,0)
        