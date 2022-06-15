# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,maxval):
            count=0
            if not root:
                return 0
            
            if root.val >=maxval:
                count+=1
           
            count+=dfs(root.left,max(maxval,root.val))
            count+=dfs(root.right,max(maxval,root.val))
            return count
        return dfs(root,root.val)
        