class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        x=0
        y=0
        for i in range(len(nums)):
            y = total - x - nums[i]
            if x==y:
                return i
            x+=nums[i]
        return -1