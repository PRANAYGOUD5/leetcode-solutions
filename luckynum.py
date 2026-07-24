class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l=[]
        c=Counter(arr) 
        for num,freq in c.items():
            if num==freq:
                l.append(freq)
        return max(l) if l else -1
