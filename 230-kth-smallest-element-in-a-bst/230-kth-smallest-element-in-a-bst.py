# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    
        count=0
        stack=[]
        cur = root
        while cur or stack :
            while cur:
                stack.append(cur)
                cur=cur.left

            cur=stack.pop()
            count+=1
            if count== k:
                return cur.val
            cur=cur.right
        