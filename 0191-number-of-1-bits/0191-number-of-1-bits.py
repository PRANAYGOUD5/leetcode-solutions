class Solution:
    def hammingWeight(self, n: int) -> int:
        bin=""
        while n>0:
            bin+=str(n%2)
            n//=2
        return bin.count('1')
    