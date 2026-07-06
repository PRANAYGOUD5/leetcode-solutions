class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l=[]
        for i in range(len(nums)+1):
            for j in combinations(nums,i):
                l.append(tuple(j))
        return [list(x) for x in set(l)]
