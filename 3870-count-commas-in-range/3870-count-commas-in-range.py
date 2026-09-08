class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<=3:
            return 0
        c=0
        for i in range(n+1):
            if i>999:
                c+=1
        return c
