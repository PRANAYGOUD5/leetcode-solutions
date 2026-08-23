class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        y=nums[:]
        y.sort()
        x=y[::-1]
        if nums==y:
            return True
        elif nums==x:
            return True
        else:
            return False