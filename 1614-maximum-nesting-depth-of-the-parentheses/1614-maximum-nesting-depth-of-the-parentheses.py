class Solution:
    def maxDepth(self, s: str) -> int:
        pc=0
        tc=0
        for i in s:
            if i=='(':
                pc+=1
                if tc<pc:
                    tc=pc
            
            elif i==')':
                pc-=1
            
        return tc