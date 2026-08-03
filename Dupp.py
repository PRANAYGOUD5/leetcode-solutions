class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c=Counter(nums)
        for num,freq in c.items():
            if freq>1:
                return num
