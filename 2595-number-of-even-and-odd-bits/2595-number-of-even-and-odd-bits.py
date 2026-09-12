class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        x=bin(n)[2:][::-1]
        ev=0
        od=0
        for i in range(len(x)):
            if i%2==0 and x[i]=='1':
                ev+=1
            if i%2!=0 and x[i]=='1':
                od+=1
        return [ev,od]
