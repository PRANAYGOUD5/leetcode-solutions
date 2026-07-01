class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        if len(set(freq.values()))==1:
            return True
        return False

        