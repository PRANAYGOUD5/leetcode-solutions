class Solution:
    def isHappy(self, n: int) -> bool:
        def hap(n):
            sq=0
            while n>0:
                rem=n%10
                sq+=rem*rem
                n=n//10
            return sq
        slow=n
        fast=hap(n)

        while fast!=1 and slow!=fast:
            slow=hap(slow)
            fast=hap(hap(fast))
        return fast==1