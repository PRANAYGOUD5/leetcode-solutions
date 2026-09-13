class Solution:
    def isPalindrome(self, s: str) -> bool:
        v=""
        for i in range(len(s)):
            if s[i].isalnum():
                v+=s[i]
        v=v.lower()
        return v==v[::-1]