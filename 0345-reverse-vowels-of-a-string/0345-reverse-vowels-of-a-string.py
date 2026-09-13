class Solution:
    def reverseVowels(self, s: str) -> str:
        l=['A','a','E','e','I','i','O','o','U','u']
        nl=[]
        s=list(s)
        for i in range(len(s)):
            if s[i] in l:
                nl.append(s[i])
        j=0
        for i in range(len(s)):
            if s[i] in l:
                s[i]=nl[::-1][j]
                j+=1
        return ''.join(s)
