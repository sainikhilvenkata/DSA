class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[-1]*len(nums1)
        stack=[]
        
        hmap={n:i for i,n in enumerate(nums1)}
        
        for x in nums2:
            
            while stack and stack[-1]<x:
                k=stack.pop()
                if k in nums1:
                    res[hmap[k]]=x
            stack.append(x)
                
        return res
            
            
        
        