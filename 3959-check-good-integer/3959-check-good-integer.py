class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        dgsu=0
        st=str(n)
        sqsu=0
        for i in st:
            dgsu+=int(i)
            sqsu+=int(i)**2
        if (sqsu-dgsu)>=50:
            return True
        return False

