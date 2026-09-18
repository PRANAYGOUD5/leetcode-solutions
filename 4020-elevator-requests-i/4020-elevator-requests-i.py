class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:

        t=0
        if len(requests)<=1:
            return requests[0]
        for i in range(len(requests)-1):
            if i==0:
                t+=requests[i]
            t+=abs(requests[i]-requests[i+1])
        return t
