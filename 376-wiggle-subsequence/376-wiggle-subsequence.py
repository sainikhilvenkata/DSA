class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        pos, neg = 1,1
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                neg = pos + 1
            elif nums[i]>nums[i-1]:
                pos = neg + 1
        return max(pos, neg)
        