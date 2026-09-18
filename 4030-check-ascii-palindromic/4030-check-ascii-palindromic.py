class Solution:
    def isPalindromic(self, s: str) -> bool:
        ns=""
        for i in s:
            x=ord(i)
            binn=bin(x)[2:]
            ns+="0"+binn
        return ns==ns[::-1]