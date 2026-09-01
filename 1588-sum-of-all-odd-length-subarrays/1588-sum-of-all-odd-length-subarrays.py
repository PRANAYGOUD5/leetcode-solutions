class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)+1):
                if len(arr[i:j])%2!=0:
                    l+=sum(arr[i:j])
        return l