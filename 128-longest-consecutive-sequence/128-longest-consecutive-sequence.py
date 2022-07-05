class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)==1:
            return 1
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        max=0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
                if count>max:
                    max=count
            else:
                count=1
        if count>max:
            max=count
        return max
        