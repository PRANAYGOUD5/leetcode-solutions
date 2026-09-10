class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        l=[]
        while len(l)<=k:
            if i not in arr:
                l.append(i)
            if len(l)==k:
                break
            i+=1
        return l[k-1] if l else 0
