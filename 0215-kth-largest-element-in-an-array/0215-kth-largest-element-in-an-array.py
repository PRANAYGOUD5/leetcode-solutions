class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        ny=nums[::-1]
        return ny[k-1]