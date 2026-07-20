class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        l=[]
        x=(num//3)-1
        l.append(x)
        l.append(x+1)
        l.append(x+2)
        if sum(l)==num:
            return l
        return []