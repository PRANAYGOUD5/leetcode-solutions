class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        l=[]
        for i in range(len(nums)):
            c=0
            if nums[i]%2==0:
                for j in range(i+1,len(nums)):
                    if nums[j]%2!=0:
                        c+=1
            else:
                for j in range(i+1,len(nums)):
                    if nums[j]%2==0:
                        c+=1
            l.append(c)
        return l

                