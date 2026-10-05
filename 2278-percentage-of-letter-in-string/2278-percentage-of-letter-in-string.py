class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c=Counter(s)
        n=len(s)
        if letter not in s:
            return 0
        else:
            x=c[letter]/n
            y=int(x*100)
            return y