class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        l=[]
        c=0
        
        for i in range(len(nums)):
            if max(nums)>=nums[i]*2 or nums[i]==max(nums):
                c+=1
        if c==len(nums):
            return nums.index(max(nums))
        return -1    
            
        