class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0

        l,r = 0, len(heights)-1
        while l<r:
            water = (r-l)*min(heights[r],heights[l])
            maxwater = max(maxwater,water)

            if heights[l]>=heights[r]:
                r-=1
            if heights[l]<heights[r]:
                l+=1
        
        return maxwater


        