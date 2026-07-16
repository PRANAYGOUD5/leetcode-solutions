class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=nums[0]
        max1=nums[0]
        for i in range(1,len(nums)):
            cs=max(cs+nums[i],nums[i])
            max1=max(cs,max1)
        return max1