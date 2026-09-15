class Solution:
    def countSubstrings(self, s: str) -> int:
        l=[]
        c=0
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                l.append(s[i:j])
        for i in l:
            if i==i[::-1]:
                c+=1
        return c