class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while (len(s)>k):
            new=""
            for i in range(0,len(s),k):
                grp=s[i:i+k]
                tot=0
                for j in grp:
                    tot+=int(j)
                new+=str(tot)
            s=new
        return s
