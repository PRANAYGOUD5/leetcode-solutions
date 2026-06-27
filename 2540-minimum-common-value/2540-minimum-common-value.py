class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1=set(nums1)
        n2=set(nums2)
        cm=n1.intersection(n2)
        return min(cm) if cm else -1