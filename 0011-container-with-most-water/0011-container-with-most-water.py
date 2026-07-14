class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while l<r:
            width=r-l
            h=min(height[l],height[r])
            area=width*h
            m=max(m,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m