# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        q=[(root,0)]
        wid=1
        
        while q:
            
            if len(q)>1:
                wid=max(wid,q[-1][1]-q[0][1]+1)
            temp=[]
            while q:
                node,lev =q.pop(0)
                
                if node.left:
                    temp.append((node.left,2*lev))
                if node.right:
                    temp.append((node.right,2*lev+1))
            q=temp
                
        return wid
            
            
            
        