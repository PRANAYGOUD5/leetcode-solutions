class Solution:
    def hasAlternatingBits(self, n: int) -> bool:   
        x=bin(n)[2:]
        s=str(x)
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                return False
        return True
        